## Testing

## Functional Testing

**Registration**

Description:

Ensure a user can successfully register on the Kidomart e-commerce website.

Steps:

1. Navigate to [KidoMart](https://kidomart-78f25893d540.herokuapp.com/) and click on the "Register" link.
2. Enter your details in the registration form (All fields are required):

- First Name: John
- Last Name: Doe
- Email Address: john.doe@example.com (must be an active email)
- Phone Number: +1 555-123-4567
- Create Password: Password123
- Confirm Password: Password123

3. Click the "Register" button.

Expected:

An activation email is sent to the user with a secure link to activate their account. Upon clicking the link in the email, user is redirected to the login page with an activation success message.

Actual:

User recieves an activation link via email. After account activation, user is redirected to the login page with a success message confirming the account registration and activation.

<hr>

**Login**

Description:

Ensure a user can successfully log in to his or her Kido account.

Steps:

1. Navigate to [KidoMart](https://kidomart-78f25893d540.herokuapp.com/) and click on the "Login" link.
2. Enter your details in the registration form (All fields are required):

- Email Address: john.doe@example.com (must be the exact email user registered with)
- Password: Password123 (user's exact password)

3. Click the "Login" button.

Expected:

User is successfully logged in to his or her account dashboard with a login success message.

Actual:

User is successfully logged in to his or her account dashboard with a login success message.

<hr>

**Logout**

Description:

Ensure a user can log out

Steps:

1. Login to the website
2. Click the logout button from the navbar or on the dashboard side bar

Expected:

User is logged out and a logout success message is displayed.

Actual:

User is logged out and a logout success message is displayed.

<hr>

**Password Reset**

Description:

Ensure a user can successfully reset their password on the Kidomart website.

Steps:

1. Navigate to the [KidoMart login page](https://kidomart-78f25893d540.herokuapp.com/accounts/login/) and click on the "Forgot Password" link on top of the login button.
2. Verify that the user is redirected to the "Password Reset" page with the heading and instructions.
3. Fill in the email address you registered with and click the "Submit" button.
4. Verify that a verification email is sent to the provided email address.
5. Check the email inbox and click on the verification link in the password reset email.
6. Verify that the user is redirected to the "Password Reset" page.
7. Enter a new password and confirm the new password.
8. Click the "Reset Password" button.
9. Verify that the user is redirected to the login page with a success message indicating the password reset was successful.
10. Log in with the new password to ensure successful login.

Expected:

The user can successfully initiate a password reset from the "Forgot Password" link.
The user receives a verification email and can click the link to reset the password.
After successfully resetting the password, the user is redirected to the login page with a success message.
The user is able to log in with the new password.

Actual:

The user can successfully initiate a password reset from the "Forgot Password" link.
The user receives a verification email and can click the link to reset the password.
After successfully resetting the password, the user is redirected to the login page with a success message.
The user can log in with the new password.

<hr>

**Change Password**

Description:

Ensure a user can successfully change their password on the Kidomart website.

Steps:

1. Navigate to the [KidoMart Dashboard](https://kidomart-78f25893d540.herokuapp.com/accounts/change_password/) and click on the "Change Password" menu on the the sidebar.
2. Enter your current password.
3. Create new password.
4. Confirem new password. (Make sure the new password is exactly what you enter here)
5. Click on the 'Change' button.

Expected:

After successfully changing the password, the user is redirected to the password change success page. The success page contains a heading and a text indicating the success of the password change.
The user can either log in or go to the home page from the success page by clicking the "Login" or the 'home' button. Logging in with the updated password is successful.

Actual:

After successfully changing the password, the user is redirected to the password change success page. The success page contains a heading and a text indicating the success of the password change.
The user can either log in or go to the home page from the success page by clicking the "Login" or the 'home' button. Logging in with the updated password is successful.

<hr>

**Edit Profile**

Description:

Ensure a user can successfully update their profile details on the Kidomart e-commerce website.

Steps:

1. Navigate to the [KidoMart Dashboard](https://kidomart-78f25893d540.herokuapp.com/accounts/edit_profile/) and click on the "Edit Profile" menu on the the sidebar.

2. On the profile update page, update the following details try to edit any or all of your profile details:

- First Name
- last Name
- Phone Number
- Profile picture
- Address Line 1
- Address Line 2
- City
- State
- Country

3. Click on the 'Save' button to save your update.

Expected:

User profile is successfully updated. User is redirected to the same page with an update success message and the updated details.

Actual:

User profile is successfully updated. User is redirected to the same page with an update success message and the updated details.

<hr>

**My orders**

Description:

Ensure a user can successfully view their order details and history on the Kidomart website.

Steps:

1. Navigate to the [KidoMart Dashboard](https://kidomart-78f25893d540.herokuapp.com/accounts/my_orders/) and click on the "My Orders" menu on the the sidebar.

- Alternatively, the 'View Orders' link in the 'Your orders' section of the Dashboard also leads to the the 'My Orders' page upon clicking it.

2. On the 'My Orders' page, you will find the order number, full name, phone number, order total, and ordered date. Click on the order number to view the order invoice or details of that particular order.

Expected:

User has access to and are able to view their order history anytime they want.

Actual:

Users have access to their order history and details and can view it anytime.

<hr>

**Delete Account**

Description:

Ensure a user can successfully delete their account on the Kidomart website.

Steps:

1. Navigate to the [KidoMart Dashboard](https://kidomart-78f25893d540.herokuapp.com/accounts/delete_account/) and click on the "Delete Account" menu on the the sidebar.

2. On the account deletion confirmation page, carefully review the informationon the page.

3. Confirm deletion of your account by clicking the 'Delete Account' button.

Expected:

User is first logged out and redirected to the register page with an account deletion success message after the account is deleted.

Actual:

User is first logged out and redirected to the register page with an account deletion success message after the account is deleted.

<hr>

**Add to Cart and Product Variation Selection**

Description:

Ensure a user can successfully add an item and its associated variations (colour and or size) to cart on the Kidomart website.

Steps:

1. Navigate to the [KidoMart](https://kidomart-78f25893d540.herokuapp.com/) and click on the any of the product's name or image.

- This redirects you to the [KidoMart product detail page](https://kidomart-78f25893d540.herokuapp.com/category/clothing/coll-unisex-jacket/) of that particular product.

2. In the item card, click on the 'Choose color' button to select a color and the 'Choose Size' button to select a size (if the item has variation(s)).

3. Then click on the add to cart button.

Expected:

Selected product is added to the cart with the specified color and size.

Actual:

Expected:

Selected product is added to the cart with the specified color and size.

<hr>

**Cart Item Quantity Increment and Decrement**

Description:

Ensure a user can successfully increment cart item and decrement cart item on the Kidomart website.

Steps:

1. Navigate to the [KidoMart Cart Page](https://kidomart-78f25893d540.herokuapp.com/cart/)

2. Click on the '-' button to decrease item quantity or click on the '+' button to increase item quantity.

Expected:

Upon clicking the '-' button, the quantity of the item reduces by one and upon clicking the '+' button, the quantity of the item increments by one indicating that the test passed.

Actual:

Upon clicking the '-' button, the quantity of the item reduces by one and upon clicking the '+' button, the quantity of the item increments by one.

<hr>

**Cart Item Removal**

Description:

Ensure a user can successfully remove cart item on the Kidomart website.

Steps:

1. Navigate to the [KidoMart Cart Page](https://kidomart-78f25893d540.herokuapp.com/cart/)

2. Click on the 'Remove' button under Actions.

- Alternatively, user can click on the '-' button till quantity reaches zero.

Expected:

Cart Item is successfully removed showing that the test passed.

Actual:

Cart Item is successfully removed.

<hr>

**Checkout**

Description:

Ensure a user can successfully checkout on the Kidomart website.

Steps:

1. Navigate to the [KidoMart Checkout Page](https://kidomart-78f25893d540.herokuapp.com/cart/checkout/)

2. Fill out the field in the form;

- First Name
- Last Name
- Phone Number
- Profile picture
- Address Line 1
- Address Line 2
- City
- State
- Country
- Leave a Note (optional)
- Card details (any of the stripe test card numbers(eg; 4242424242424242 4/24/242/42424))

3. Click on the 'Complete Order' button.

Expected:

User is redirected to the checkout success page which contains an invoice of their purchase with a success message that informs them on the success of their order and payment showing that the test passed.

The user also recieves a purchase confirmation email with his or her purchase details.

Actual:

User is redirected to the checkout success page which contains an invoice of their purchase with a success message that informs them on the success of their order and payment. The user also recieves a purchase confirmation email with his or her purchase details.

<hr>

**Rating and Review**

Description:

Ensure a user can successfully rate and review purchased product.

Steps:

1. Navigate to the [KidoMart Product Detail Page](https://kidomart-78f25893d540.herokuapp.com/category/clothing/coll-unisex-jacket/) after a purchase. (users can only review products they have purchased)

2. Scroll down to the review section.

3. Click on the number of stars per your rating.

4. Fill out the review form that comes with the 'Review Title' and 'Review Text' fields.

5. Click on the 'Submit Review' button.

Expected:

Review and the rating are submitted successfully. Reviews and the calculated rating average can be viewed by anyone on the product detail page. While the calculated rating average is seen also on the product on the home page. The test passed.

Actual:

Review and the rating are submitted successfully. Reviews and the calculated rating average can be viewed by anyone on the product detail page. While the calculated rating average is seen also on the products on the home page.

<hr>

**Search Bar**

Description:

Ensure a user can search for an item in the search bar of the Kidomart website.

Steps:

1. Navigate to [KidoMart](https://kidomart-78f25893d540.herokuapp.com/)

2. Type a valid search query into the search bar in the middle of the navbar.

3. Press the "Enter" key or click the search icon to initiate the search.

4. Check if the search results are displayed on the page.

5. Verify that the displayed results match the search query.

6. If no results are found, confirm that a message is displayed indicating the no search result found.

Expected:

If a search item is found, it is displayed on the page with its associated search count. When no item is found for a particular search, there is a clear message that says "Sorry! we do not have this item yet". Therefore, the test passed for this functionality.

Actual:

If a search item is found, it is displayed on the page with its associated search count. When no item is found for a particular search, there is a clear message that says "Sorry! we do not have this item yet"

<hr>

**Category Sorting**

Description:

Ensure a user can sort products by category on the Kidomart website.

Steps:

1. Navigate to [KidoMart](https://kidomart-78f25893d540.herokuapp.com/)

2. Click on the 'Categories' dropdown button.

3. Select a category by clicking on it.

4. Check if the products are sorted by that category with the category heading on top of it.

Expected:

Products are sorted by the selected category with the category heading on top of it and the item count is also displayed. This passes the test.

Actual:

Products are sorted by the selected category with the category heading on top of it and the item count is also displayed.

<hr>

**Newsletter Subscription**

Description:

Ensure a user can subscribe to newsletters on the Kidomart website.

Steps:

1. Navigate to [KidoMart](https://kidomart-78f25893d540.herokuapp.com/)

2. Locate the newsletter form at the bottom of the page in the footer part.

3. Enter a valid email address.

4. Click on the 'Subscribe' button.

5. Check for the user's email in the 'Audience' section of the Mailchimp dashboard.

Expected:

User is successfully subscribed to the Mailchimp newsletter and a "thank you for subscribing" message is displayed. The user's email is added to the 'Audience' section of the Mailchimp dashboard indicating that the test passed.

Actual:

User is successfully subscribed to the Mailchimp newsletter and a "thank you for subscribing" message is displayed. The user's email is added to the 'Audience' section of the Mailchimp dashboard.

<hr>

**Footer**

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the instagram icon opened the kidomart instagram handle in a new tab, the facebook icon opened the kidomart facebook handle in a new tab and the twitter icon also opened the kidomart twitter handle in a new tab. These behaved as expected.

## Negative Testing

Tests were performed to ensure that:

1. Forms cannot be submitted when required fields are empty.

2. Error handling has been fully implemented to take care of all possible errors during the payment process. Tests have been carried out to ensure that in cases where there are hitchtes or interruptions during the payment process, the user is assured of accurate updates on their payment status and they are informed about what precisely transpired during the payment process.

## Unit Testing

Unit tests were carried out to test core functionality in some forms, template views, models and redirects to make sure these core parts of the app is thoroughly tested to its bits.

Results:

![unit tests](media/docs/test/unittest-coverage.jpg)

## Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs
- Color contrasts meet a minimum ratio as specified in [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
- All non textual content had alternative text or titles so descriptions are read out to screen readers
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- WCAG 2.1 Coding best practices being followed

## Validator Testing

All pages were run through the [w3 HTML Validator](https://validator.w3.org/). Initially there were some warnings and errors due to stray script tags, misuse of anchor tags within buttons and some improperly closed elements. All of these issues were corrected and all pages passed validation.

Due to the django templating language code used in the HTML files, these could not be copied and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will display only the HTML rendered code.

![HTML Validator](media/docs/test/w3-html-validation.jpg)

The css stylesheet was seperately run through the [w3 CSS Validator](https://jigsaw.w3.org/css-validator/). Initially there were some warnings and errors due to use of obsolete elements like 'strike' on the home page and the product detail page. There was also an issue with the closing div container next to the nav element in the navbar. Both issues were corrected and the style sheet passed validation.

There were however two warnings, which came from the Google Font import and the Stripe custom styling which is not within my control and also not deemed harmful. The validator just issued a disclaimer on the Google Font link on the top of my css file that it does not validate thie external file.

![CSS Validator](media/docs/test/jigsaw-validation.jpg)

JavaScript code was run through the [JSHINT](https://jshint.com) javascript validator. It flagged up issues with esversion:6. This was fixed by adding '// jshint esversion: 6' to the top of the js file.
The only warning remained was the JQuery '$' signs and Stripe variable which shows up as not defined. This cannot be dealt with since the Javascript file is tested seperately and cannot in this regard find the the dynamic values in the workspace.

![JS validator- custom js](media/docs/test/jshint-custom-js.jpg)

![JS validator- stripe js](media/docs/test/jshint-stripe-js.jpg)

All python files were run through the [Pep8](https://pep8ci.herokuapp.com/) validator to ensure all code was pep8 compliant. Some errors were shown due to blank spacing and lines too long. All of these errors were resolved and code passed validator tests.

![PEP8 cart models](media/docs/test/pe8-cart-models.jpg)
![PEP8 cart admin](media/docs/test/pep8-cart-admin.jpg)
![PEP8 cart url](media/docs/test/pep8-cart-url.jpg)
![PEP8 category admin](media/docs/test/pep8-category-admin.jpg)
![PEP8 category context processor](media/docs/test/pep8-category-context-processor.jpg)
![PEP8 category model](media/docs/test/pep8-category-model.jpg)
![PEP8 custom storage](media/docs/test/pep8-custom-storage.jpg)
![PEP8 main urls](media/docs/test/pep8-main-urls.jpg)
![PEP8 order admin](media/docs/test/pep8-order-admin.jpg)
![PEP8 order forms](media/docs/test/pep8-order-forms.jpg)
![PEP8 order models](media/docs/test/pep8-order-models.jpg)
![PEP8 product admin](media/docs/test/pep8-product-admin.jpg)
![PEP8 product form](media/docs/test/pep8-product-form.jpg)
![PEP8 products urls](media/docs/test/pep8-products-urls.jpg)
![PEP8 products view](media/docs/test/pep8-products-view.jpg)
![PEP8 store urls](media/docs/test/pep8-store-urls.jpg)

In few cases, like tha of the settings file, ther are external code that may have 'Line too long' warnings. These are left in their sate if they are readable and have no hitches. In other cases, very little white spaces are left for the readability and clarity of code alongside descriptive comments. Those file how ever has unittest implemented to ensure their utmost functionality.

![PEP8 exceptions sample(Line too log)](media/docs/test/pep8-too-long.jpg)

## Lighthouse Report

Lighthouse report showed areas for improvement on Performance. This was related to the user profile images that users upload on the dashboard. There may be some restrictions of the type of images that can be posted but he website allows room for more flexibility. More restrictions on image types may frustrate users and bring down the patronage of the site. For this reason, users are given a wide range of performance-meaningful image options which are not below standard to upload. Another issue raised was on the spelling out of the width and height of the product images. Product images vary in different dimensions and can only be regulated to some minimal extent to look pleasant on the site.

![Lighthouse](media/docs/test/lighthouse-report.jpg)

## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and above as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open a browser and navigate to [KidoMart](https://kidomart-78f25893d540.herokuapp.com/)
- Open the developer tools (right click and inspect or hit the F12 key)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
- Click and drag the responsive window to maximum width

Expected:

The KidoMart website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap. Responsive test passed even beyond screens smaller than 320px.

Actual:

Website behaved as expected.

Website was also opened on the following devices and no responsive issues were found:

-iPhone SE  
-Huawei mipad 10  
-Iphone 10  
-Iphone 12 Xs max  
-Iphone 12  
-Iphone 13  
-Iphone 6S plus  
-Xiomi Redme 11 pro  
-Samsung A 12  
-Samsung Galaxy 20  
-Samsung Galaxy Tab S7  
-Samsung m21  
-Infinix Hot 12  
-Asus Sonicmaster  
-Hp EliteBook 8440p  
-Hp laptop 14s  
-Dell Latitude 5430  
-Mcbook Retina

## Bugs (fixed)

Initially, when the user had an empty cart, there was an error because the object did not exist. This have been fixed with the python exception handling.
Email sending also had an issue with the SMTP Authentication. An app password alongside email backend configuration was set up to take care of the bug. Thereafter, all verification, activation and confirmation emails are smoothly sent.
The website in total functions as expected and there are no bugs.
