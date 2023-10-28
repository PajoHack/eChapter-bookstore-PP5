import uuid
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Book
from profiles.models import UserProfile
from django.db.models import Sum


class Order(models.Model):
    """
    Order model for representing customer orders in the online bookstore.

    Fields:
        - order_number (CharField): A unique identifier for each order.
        - user_profile (ForeignKey): A foreign key to the UserProfile model.
        - full_name (CharField): The full name of the customer.
        - email (EmailField): The email address of the customer.
        - phone_number (CharField): The phone number of the customer.
        - country (CountryField): The country for delivery.
        - postcode (CharField): The postal code for delivery, can be null.
        - town_or_city (CharField): The town or city for delivery.
        - street_address1 (CharField): The first line of the street address for delivery.
        - street_address2 (CharField): The second line of the street address for delivery, can be null.
        - county (CharField): The county for delivery, can be null.
        - date (DateTimeField): The date and time the order was placed.
        - delivery_cost (DecimalField): The cost of delivery.
        - order_total (DecimalField): The total cost of the order without delivery.
        - grand_total (DecimalField): The total cost of the order including delivery.
        - original_bag (TextField): Original cart, stored as a text field.
        - stripe_pid (CharField): The Stripe payment identifier.

    Methods:
        - _generate_order_number: Generates a unique order number using UUID.
        - update_total: Updates the grand total and delivery cost.
        - save: Overrides the original save method to include the order number.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    OrderLineItem model represents individual line items in a customer order.

    Fields:
        - order (ForeignKey): A foreign key to the Order model.
        - book (ForeignKey): A foreign key to the Book model.
        - quantity (IntegerField): The quantity of the book ordered.
        - lineitem_total (DecimalField): The total cost of this line item, calculated as 'quantity' * 'book price'.

    Methods:
        - save: Overrides the original save method to set the lineitem_total field and to update the order's total cost.
        - __str__: String representation of the model instance.

    Relationships:
        - Related name 'lineitems' set for reverse relation from Order to OrderLineItem instances.
    """
    order = models.ForeignKey(
        Order, null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    book = models.ForeignKey(
        Book, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        self.lineitem_total = self.book.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Book "{self.book.title}" on order {self.order.order_number}'
