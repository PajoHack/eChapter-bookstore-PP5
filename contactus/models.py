from django.db import models


class Contact(models.Model):
    """
    A model to represent contact form submissions.
    
    This model stores the name, email, subject, and message entered by users 
    through the contact form. Each submission also has a timestamp indicating 
    when it was created.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
