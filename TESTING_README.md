# Testing README

[Back to Main README](README.md)

## Table Of Contents

1. [Introduction](#introduction)
2. [Code Validation](#code-validation)
3. [Browser Compatibility](#browser-compatibility)
4. [LightHouse Testing](#lighthouse-testing)
5. [Performance Testing](#performance-testing)
6. [Manual Testing](#manual-testing)
7. [User Stories Testing](#user-stories-testing)
8. [Stripe](#manual-testing-of-stripe-integration)

## Introduction

This document outlines the various testing methods applied to ensure the functionality, accessibility, and compatibility of the eChapter application.

## Code Validation

### HTML: Validated using W3C HTML Validator & htmlhint

![Screenshot of HTMl validation](documentation/screenshot-of-w3c-html-validation.png)

![Screenshot of Htmlhint validation](documentation/screenshot-of-html-hint-results.png)

### CSS: Validated using W3C CSS Validator.

![Screenshot of CSS validation](documentation/screenshot-of-w3c-jigsaw-css-validation.png)

### JavaScript Linting

All JavaScript snippets within the project have been linted using [JSHint](https://jshint.com/). The linter was configured to recognize jQuery syntax to ensure accurate linting. During this process, several missing semicolons were identified and corrected. As a result, the project now passes JSHint validation with no errors or warnings, contributing to the overall code quality and consistency.

![Screenshot of JSHint result](documentation/screenshot-of-js-hint.png)

### Python: Checked for PEP 8 compliance.

I used flake8 to validate the python code. I ran `python3 -m flake8 --exclude=*/migrations/*,./echapter/settings.py,./checkout/webhooks.py,./checkout/webhook_handler.py,.devcontainer/build-assets/*` 

### Exclusions

- Migrations: Auto-generated and not meant to be manually altered, hence excluded.
Settings File (echapter/settings.py): Contains configurations that may not strictly adhere to PEP 8, excluded for practical reasons.
- Webhook Files (webhooks.py, webhook_handler.py): May include vendor-specific structures, leading to intentional deviations from PEP 8 guidelines.
- Build Assets: Any files under the .devcontainer/build-assets/ folder were excluded as they are not part of the application logic.

### Resolved Issues

- Line Length: Corrected lines that exceeded the recommended length limit to adhere to PEP 8 standards.
- Unused Imports: Removed unnecessary import statements that were not being utilized.
- Whitespace: Removed unnecessary trailing whitespaces.

## Browser Compatibility

The eChapter website has been tested across various browsers and operating systems to ensure a consistent user experience. Below is a list of the browsers and the operating systems on which the testing was performed:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

### Operating Systems Tested

- Windows 10
- macOS 14 Sonoma
- iOS 15
- Android 12

### Known Issues and Resolutions
- In Safari on iOS, there was a minor layout issue with the footer, which was resolved by adjusting the CSS properties.

## Lighthouse Testing

![Screenshot of lighthouse testing score](documentation/lighthouse-score-screenshot.png)

## Performance Testing

Used Google Lighthouse to analyze the performance of the website on various fronts such as Performance, Accessibility, Best Practices, and SEO.

## Manual Testing

Manual testing was conducted to ensure a thorough evaluation of the site's functionality and usability. Below are the areas and features that were manually tested:

### Navigation

1. **Header Links**
    - Tested that all header links navigate to the correct page.
    - Checked that the logo redirects to the home page.

2. **Footer Links**
    - Verified that social media links open in a new tab and go to the correct URL.
    - Checked that the "Privacy Policy" link navigates to the correct section.

### Forms

1. **Registration and Login**
    - Attempted to register with invalid and valid credentials.
    - Checked the login functionality with both incorrect and correct credentials.
    - Tested the "Forgot Password" feature.

2. **Search Bar**
    - Conducted searches using various terms to see if the relevant results are displayed.

### User Flows

1. **Adding Items to Bag**
    - Added multiple items to the bag and checked if the bag is updated correctly.

2. **Checkout Process**
    - Went through the checkout process with different payment methods to ensure the transactions are processed correctly.

3. **Profile Page**
    - Checked that the order history is displayed correctly in the profile page.

### Responsiveness

1. **Mobile, Tablet, and Desktop**
    - Checked the website's responsiveness on various devices using both real devices and browser tools for emulation.

2. **Cross-Browser Compatibility**
    - Tested the site on different browsers like Chrome, Firefox, and Safari to ensure cross-browser compatibility.

![Screenshot from am I responsive website](documentation/screenshot-from-am-i-responsive.png)

### Error Handling

1. **404 and 403 Pages**
    - Tested the custom 404 and 403 error pages by manually entering incorrect URLs and trying to access restricted areas.

2. **Form Errors**
    - Checked that proper error messages are displayed when submitting forms with invalid data.

### Additional Notes:
- All tests were conducted multiple times and at different stages of development to confirm consistency.
- Where issues were found, they were addressed immediately and re-tested to confirm they were resolved.

[Back to the top](#)

## User Stories Testing

For each user story, a systematic testing approach was followed to ensure that the website meets the needs of its different types of users.

| User Story Number | User Type      | User Story                                                         | Testing Method                                                                     | Result | Additional Notes |
|-------------------|----------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|--------|------------------|
| 1                 | Shopper        | View a list of books to select books to purchase                    | Manually browsed the site as a shopper and verified that the list of books is displayed. | Passed | All books appeared as expected with relevant details. |
| 2                 | Shopper        | View individual book details to see the price, description, rating, and cover image | Clicked on individual books to view details.                                      | Passed | Details, including price and rating, were clearly visible. |
| 3                 | Shopper        | Identify items on sale to take advantage of bargain offerings       | Checked that books on sale are clearly marked.                                      | Passed | Sale items were appropriately labeled. |
| 4                 | Shopper        | Easily view total of purchases at all times                         | Checked that the total cost of items in the bag is visible at all times.            | Passed | Bag total was consistently visible. |
| 5                 | Site User      | Register for an account                                             | Attempted to register a new account.                                                | Passed | Received an email confirmation upon registration. |
| 6                 | Site User      | Quickly login & logout                                              | Successfully logged in and out of an account.                                       | Passed | Login and logout were seamless. |
| 7                 | Site User      | Reset my password if forgotten                                      | Used the "Forgot Password" feature to reset the password.                           | Passed | Received an email with reset instructions. |
| 8                 | Site User      | Have a User Profile                                                 | Checked that the profile page is available after logging in.                        | Passed | Profile page displayed order history. |
| 9                 | Site User      | Receive an email confirmation after registering                     | Checked email after registration.                                                   | Passed | Email received with verification link. |
| 10                | Shopper        | Sort the list of books                                              | Used the sorting dropdown to sort books by various criteria.                        | Passed | Sorting function worked as expected. |
| 11                | Shopper        | Sort by specific category                                           | Sorted books by selecting a specific category.                                      | Passed | Books were correctly sorted by the selected category. |
| 12                | Shopper        | Search for a book by title or description                           | Used the search function to find books by title or description.                     | Passed | Search results matched query parameters. |
| 13                | Shopper        | Easily view search results                                          | Checked that search results are easily readable and relevant.                       | Passed | Results were clear and relevant to the search term. |
| 14                | Shopper        | Select the product I want to purchase                               | Selected a product and added it to the bag.                                         | Passed | Product was successfully added to the bag. |
| 15                | Shopper        | View items in my bag                                                | Opened the bag to view items.                                                       | Passed | All items and their quantities were correctly displayed. |
| 16                | Shopper        | Adjust the amount of individual items in the bag                    | Adjusted the quantity of items in the bag.                                          | Passed | Quantities were successfully updated. |
| 17                | Shopper        | Enter my payment information                                        | Entered payment details during checkout.                                            | Passed | Payment went through successfully via Stripe. |
| 18                | Shopper        | Feel safe about entering my payment details                         | Checked that the payment form is secure (SSL, Stripe integration).                   | Passed | Site is SSL secured and Stripe is used for payments. |
| 19                | Shopper        | View an order confirmation after checkout                           | Checked that an order confirmation page is displayed after checkout.                | Passed | Order confirmation displayed with all relevant details. |
| 20                | Shopper        | Receive an email confirmation after checkout                        | Checked email after completing a purchase.                                          | Passed | Email received with order summary. |
| 21                | Store Owner    | Add a book                                                          | Added a new book via the product management page.                                    | Passed | New book appeared in the store after addition. |
| 22                | Store Owner    | Edit or update a product                                            | Edited an existing book's details.                                                  | Passed | Changes were reflected immediately. |
| 23                | Store Owner    | Delete a book                                                       | Deleted a book via the product management page.                                      | Passed | Book was successfully removed from the store. |

[Back to the top](#)

## Manual Testing of Stripe Integration

### Objective

To ensure that the Stripe payment gateway is successfully integrated and is capable of handling transactions.

### Steps Taken

1. **Placing an Order**: Went through the eChapter site's checkout process and placed an order. Used the test VISA card number `4242 4242 4242 4242` for payment.
  
2. **Confirmation**: Checked for the order confirmation on the eChapter site to make sure the transaction appears successful from the user's end.

3. **Stripe Dashboard**: Logged into Stripe's admin dashboard to confirm that the transaction was processed.
  
4. **Webhook Logs**: Reviewed webhook logs in Stripe to ensure they received the correct information and processed it as expected.

### Results

The test transaction was successful, and all data was correctly processed by Stripe.

![Screenshot of Stripe successful payment](documentation/screenshot-of-webhook-success.png)

[Back to the top](#)

[Back to Main README](README.md)
