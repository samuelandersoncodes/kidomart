# KidoMart

Kidomart is an e-commerce website that sells a variety of children's products. We give you a wide range of categories consisting of dolls, toys, clothing, electronics, beauty and accessories to choose from. And as part of our inaugurational promotion, we deliver it to your doorstep free of charge.

The live link can be found here: [Live Site - KidoMart](https://kidomart-78f25893d540.herokuapp.com/)

![Mock Up](media/docs/readme-images/mockup-kidomart.jpg)

## Table of Contents

- [KidoMart](#kidomart)
  - [Table of Contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
  - [The-Strategy-Plane](#the-strategy-plane)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics) -[Sprints](#sprints)
      - [User Stories](#user-stories)
  - [The-Scope-Plane](#the-scope-plane)
  - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The-Skeleton-Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plane](#the-surface-plane)
    - [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Technolgies](#technolgies)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

The website is aimed at providing a platform for parents, wards and children themselves to easily shop online. Registered users are able to easily purchase items ranging from toys to educational essentials online.

Our free inaugral and promotional nation-wide delivery ensures that ordered products with the 'paid' status are rightfully delivered to the associated billing addresses on time.

We look forward to becoming the best seller for children's products.

### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 10 sprints in total, spaced out evenly over eight weeks.

The kanban issues were assigned to epics and were labelled as 'must have' and 'could have'. They were assigned to sprints based on their level of priority. It was done this way to ensure that core requirements are first taken care of.

The Kanban board was created using github projects and can be located [here](https://github.com/users/samuelandersoncodes/projects/2) Each issue within it consists of a user story, acceptance criteria and tasks that defines the required functionality and its associated tasks to be executed. In total, there were 22 issues.

### KidoMart Project Board

![Kanban project image](media/docs/readme-images/kanban-project.jpg)

### KidoMart Issues

![Kanban issues image](media/docs/readme-images/kidomart-issues.jpg)

#### Epics

The project had 6 main Epics:

**EPIC 1 - Deployment Epic**

The app was first deployed to heroku so that the site is live for users. All dependencies were put in place and thouroughly tested to ensure that the live app is properly set up and has no problems. This epic was implemented first in order to avoid last minute deployment descrepancies.

**EPIC 2 - Base Setup**

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the next epic to be delivered after deployment as all other features depend on it. Here, the home page view, page navigation, product detail views and admin store management were executed.

**EPIC 3 - Registration and User Account**

In the registration and user account epic, user and super user accounts management, user registration, user authentication, password recovery, password recovery email confirmation and user profile management were executed. This epic was very important because shoppers can only make a purchase if they are authenticated. It was therefore considered as the next epic after the base setup.

**EPIC 4 - Product Sorting and Searching Epic**

The Product sorting and searching epic is for all stories related to the product sorting functionality, product categories and the product search functionality. This is very crucial for the grouping of products for easy identification and user search.

**EPIC 5 - Purchasing and Checkout**

The purchasing and checkout epic is for all stories that relate to product purchasing customization, shopping cart management, cart quantity management, checkout summary, order confirmation management, order confirmation email as well as rating and reviews.

**EPIC 6 - Documentation**

This epic is for all documentation related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

### Sprints

**EPIC 1 - Deployment Epic**

**Sprint 1**

##### User Stories

As a developer I want the application to be deployed on Heroku successfully so that is live and accessible through the Heroku domain.

As a developer, I want the necessary environment variables to be configured on Heroku so that I am sure that all dependencies like AWS s3 bucket, postgresql, stripe and django are properly wired up for the full and overall functionality of the deployed app.

As a developer, I want the application to make use of the ElephantSQL database in the production environment so that all my database schema, tables and its associated data are well structured for data storage and display.

As a developer, I want to configure the application to use AWS S3 so that all static files are safely stored and served.

##### Acceptance Criteria

- The application is successfully deployed on Heroku. The deployed application must be accessible through a Heroku domain.

- All necessary environment variables are configured on Heroku.

- The application seamlessly interacts with the ElephantSQL database on Heroku.

- Static and media files are stored and served from the configured AWS S3 bucket.

- The DEBUG setting is finally set to False.

##### Tasks

- Create a kidomart Github repository.

- Create a Heroku app for kidomart and link it to the kidomart repository on Github.

- Install Django and create the kidomart project.

- Wire up the settings for database, wsgi procfile, middleware, static and media file setups.

- Make the initial commit when the app is set and live.

- Set all necessary environment variables both in the gitpod workspace and in the Heroku settings.

- Ensure that no secret key is commited to the kidomart repository.

- Set up all dependecies for Django, AWS s3 bucket, elephant postgresql, whitenoise, stripe and email host.

- Ensure the project's dependencies and configurations are compatible with Heroku and all other used dependencies.

- Make regular commits after every bit of significant increment.

**EPIC 2 - Base Setup**

**Sprint 2**

### Product Viewing and Navigation

#### Product Display

##### User Stories

As a developer, I need to create a logo so that users can easily identify the site by it as a brand

As a developer, I need to create the navbar so that users can navigate the website from all sizes of devices

As a shopper, I want to see a list of all available products so that I can browse through and make informed purchase decisions.

As a developer, I need to create a footer with my social media business handles, contact details and newsletter subscription so that I can market my brand and communicate with my users.

##### Acceptance Criteria

- There is a navbar that has the kidomart logo which links to the home page.

- The product list should display product names, images, price and rating.

- There is a drop down menu that displays available categories.

- The page should include a search bar to enable users to search for specific products by name, description or category.

##### Tasks

- Design a kidomart logo and navbar, fixing the logo aesthetically into the navbar.

- Design and implement a responsive product list interface using HTML and CSS.

- Retrieve product data from the database and display it dynamically with Python and Django on the product list page.

#### Product Detail Page

##### User Story

As a shopper, I want to view detailed product information, including descriptions, images, ratings, reviews and pricing, so that I can make informed purchase decisions.

##### Acceptance Criteria

- The product details page should display the product name, description, images, price, ratings, reviews and any available variations of colour and or size.

- The product details page should include a section for customer reviews and ratings.

- Given the product details page, the user should be able to see high-resolution images of the product.

- The product details page should display the product's stock information. Shopper should be informed if a particular product is out of stock.

##### Tasks

- Design and implement a product details page template with a user-friendly layout using HTML and CSS.

- Retrieve and display detailed product information dynamically on the product details page, including product description, images, average rating, reviews and pricing.

- Implement a system to display product variations, if applicable. For instance, size, color and quantity to choose from.

- Develop a feature to enable customers to leave reviews and ratings for purchased products and display them on the product details page.

- Ensure that the product details page is responsive and compatible with various devices and screen sizes.

#### Home Page Pagination

##### User Story

As a site user I want to be able to easily navigate through multiple pages of product listings so that I can find and view the products I am interested in.

##### Acceptance Criteria

- When viewing products or category of products with twelve and eight products respectively, I should see a pagination component at the bottom of the page.

- The pagination component should display page numbers and navigation controls, such as "PREV" and "NEXT."

- Clicking on a page number should load and display the corresponding set of products on the page.

- The current page should be visually highlighted for good user experience.

- The "PREV" button should be disabled if the user is on the first page and the "NEXT." button should be disabled if the user is on the last page.

Implement logic in the backend to paginate product listings based on home page products, the selected category or search query.

##### Tasks

- Utilize Django's Paginator mechanism to handle the pagination logic efficiently.

- Create a reusable frontend component for pagination. Ensure the component can dynamically render the page numbers and adjust the display based on the current page and total number of pages.

- Apply appropriate styles to the pagination component for a cohesive and visually appealing design.

- Ensure the pagination is responsive and works well on various screen sizes and devices.

- Ensure that clicking on a page number triggers the appropriate calls to retrieve and display the corresponding products.

- Conduct a thorough test to ensure the pagination component works well without errors.

**Sprint 3**

### Admin Store Management

#### Store Product Stocking

##### User Story

As a store owner, I want to be able to easily add new items to my store so that I can efficiently keep the product inventory up-to-date.

##### Acceptance Criteria

- The product addition process should include fields for product details, such as name, description, price, images, category, availability status, stock count, color and size variations.

- As an administrator, I want to have the option to categorize the newly added products and assign relevant tags for improved organization and searchability.

- The system should allow the admin to assign categories, color and size variations to the new products for streamlined inventory management.

##### Tasks

- Design and implement an intuitive product addition interface for the admin, including input fields for product details and image upload functionality.

- Create a category and tagging system that enables the admin to organize and label products based on specific categories for efficient inventory management.

- Implement input validation and error handling to ensure that the admin can only add complete and accurate product information to the store's inventory.

- Test the product addition and management features thoroughly to ensure their functionality, security, and user-friendliness for the admin interface.

#### Updating Products

##### User Story

As a store owner, I want to be able to update product prices, images and description so that it reflects changes in market trends or business requirements.

##### Acceptance Criteria

- The admin should be able to access a user-friendly product editing page with editable fields for product prices, images, and descriptions.

- Updates should reflect on the respective products accordingly.

##### Tasks

- Design and implement an intuitive product editing interface for the admin, including editable fields for product prices, image uploads and description updates.

- Develop a product management system that securely stores and retrieves product information, allowing the admin to update and revise product details as needed.

- Implement input validation and error handling to ensure that the admin can only make valid and accurate changes to product details within the system.

- Test the product editing and management features rigorously to ensure its intended functionality.

#### Deleting Products

##### User Story

As a store owner, I want to be able to remove outdated or discontinued products from the store's inventory so that only up-to-date and relevant products are left in the store.

##### Acceptance Criteria

- The store owner should be able to access a product management page with an option to delete products from the store's inventory.

- The product deletion process should include confirmation prompts to prevent accidental deletion of products.

##### Tasks

- Design and implement an intuitive product management interface for the store owner, including a delete option for removing products from the inventory.

- Implement confirmation prompts and safeguards to prevent accidental deletion of products, ensuring that the store owner confirms the deletion action before it is executed.

- Test the product deletion and management features rigorously to ensure the functionality works as expected.

#### Sales Highlighting

##### User Story

As a shopper, I want to easily identify products on promotional sale offer so that I can take advantage of discounted prices.

##### Acceptance Criteria

- The website should prominently display discounted products with visible labels or tags.

- The sale prices should be clearly indicated on the respective product while the initial price is cancelled out.

##### Tasks

- Design and implement a visually distinct labelling badge for products on sale.

- Test the visibility and effectiveness of the highlighting system with a diverse group of users to ensure its clarity and user-friendliness.

**EPIC 3 - Registration and User Account**

**Sprint 4**

#### Custom User and Super User Accounts Creation and Management

##### User Story

As a developer, I want the ability to create custom users and super users so that I can manage the website's access efficiently to my liking.

##### Acceptance Criteria

- The admin can create a custom user with specified access levels and permissions.

- The admin can create a super user with full access and control over the website.

- Both custom users and super users should have unique login credentials.

- The created users should be able to log in with email as username and a password to perform their designated actions.

- Error handling should be in place for any invalid inputs or unauthorized access attempts.

- Regular users should have no permisions to staff and admin operations.

- The system should maintain a secure database of all users and their respective access levels.

- All user should be able to update their respective user details.

##### Tasks

- Design the user interface for the admin to create custom users.

- Develop the backend logic to handle custom user creation requests and store them securely in the database.

- Implement authentication and authorization mechanisms for login credentials.

- Create fields for the admin and regular users to input their necessary details.

- Define access levels and permissions for both custom users and super users.

- Test the user creation functionality for both custom users and super users, ensuring all acceptance criteria are met.

- Implement error handling to display appropriate messages for invalid inputs or unauthorized access attempts.

#### User Registration

##### User Story

As a site user, I want to easily create a personal account to access personalized features so that I can make future purchases securely and efficiently.

##### Acceptance Criteria

- The registration process should require basic information such as name, email address, phone number, address lines 1 and 2, country, state, city, password and confirm password.

- The registration process should include input validation and error handling to ensure that all required fields are filled out correctly.

##### Tasks

- Design and implement a user-friendly registration interface with clear and responsive input fields using HTML and CSS.

- Develop a secure authentication system to store user credentials and encrypt sensitive information, such as passwords.

- Implement input validation and error handling to prompt users to correct any incomplete or inaccurate information during the registration process.

- Conduct thorough testing to ensure that the registration process is smooth, secure, and user-friendly across different devices and platforms.

#### Registration Email Activation

##### User Story

As a site user, I want to receive an email confirmation upon registration to verify my account so that I can ensure registration success.

##### Acceptance Criteria:

- The system should send an automated email with a secure account activation link to the user's registered email address.

- The email should contain a user-friendly message with a prominent call-to-action link for account activation.

- The email confirmation should provide clear instructions and guidance on how to verify the account and complete the registration process.

##### Tasks

- Configure the system to trigger an automated email with a secure account activation link to the user's registered email address upon successful registration.

- Design and create an email template that includes clear instructions and a user-friendly interface for account verification and actvation.

- Implement a mechanism to track the status of email confirmations and update the user account status upon successful verification.

- Conduct rigorous testing to ensure that the email activation system functions correctly and that users can verify their accounts seamlessly.

- Provide appropriate error handling to assist users who encounter issues with the email activation process.

#### User Authentication

##### User Story

As a returning customer, I want to be able to log in quickly and securely so I can access my personalized account settings and order history.

##### Acceptance Criteria

- The login process should require a valid email address and password.

- Given the login page, the user should be able to enter their valid credentials and access their account dashboard upon successful authentication.

- The logout process should clear any active user sessions and provide a confirmation message to the user upon successful logout.

##### Tasks

- Design and implement a visually appealing and user-friendly login page with input fields for email and password using HTML and CSS.

- Develop a secure authentication system to verify user credentials and grant access to the account dashboard upon successful login.

- Implement a clear and straightforward logout button all pages to enable users to log out from any page of the website.

- Configure the system to clear any active user sessions and remove any locally stored user data upon successful logout.

- Test the login and logout processes rigorously to ensure their security, usability, and responsiveness across various devices and browsers.

#### Password Recovery

##### User Story

As a user, I want the option to reset my password easily if I forget it, so that I can regain access to my account and protect my profile and data.

##### Acceptance Criteria

- The password recovery process should involve verifying the user's identity through a secure method such as email verification.

- The system should send an email verification link through which the respective user can change their password while they concurrently verify their identity.

- The password reset process should prompt the user to create a new password and provide confirmation upon successful password update.

##### Tasks

- Design and implement a user-friendly password recovery link on the login page with HTML and CSS.

- Develop a secure password reset system that sends a reset link to the user's registered email address.

- Configure the system to validate user input and ensure that the provided information matches the account details before allowing a password reset.

- Implement necessary security measures, such as expiration links for reset requests and limitations on the number of password reset attempts within a specific time frame.

- Test the password recovery process rigorously to ensure its reliability, security, and user-friendliness across different devices and browsers.

**Sprint 5**

#### User Profile Management

##### User Story

As a site user, I want to create a personal profile so that I can easily view my order confirmation and history as well as save and manage my profile.

##### Acceptance Criteria

- The profile creation process should include fields for users to input their personal details, such as first and last names, email address, profile picture, address lines, phone number, country, state and city.

- The system should allow users to edit and modify their profile information, with appropriate validation and error handling.

- Only registered users have access to create a user profile by editing their profile on the dashboard sidebar.

##### Tasks

- Design and implement a user-friendly profile creation interface with input fields for first and last names, email address, profile picture, address lines, phone number, country, state and city.

- Develop a user profile management system that stores and retrieves user data securely and efficiently into the database.

- Create a an edit button on the dasboard that will enable users to update their profile information.

- Implement data validation and error handling to ensure that the user-provided information is accurate and meets the required criteria.

- Test the user profile feature thoroughly to ensure its functionality, security, responsiveness and user-friendliness across different devices.

**EPIC 4 - Product Sorting and Searching**

**Sprint 6**

#### Product Sorting functionality

##### User Story

As a shopper, I want the ability to sort the list of products by category so that I can easily find products in my preferred category.

##### Acceptance Criteria

- The product sorting functionality should enable users to arrange products by category.

- The product sorting functionality should be responsive and provide users with a seamless experience across different devices and screen sizes.

##### Tasks

- Design and implement a user-friendly product sorting interface that allows users to from various categories.

- Develop a sorting mechanism that rearranges the product list based on the selected category.

- Integrate a responsive design approach to ensure that the product sorting functionality is user-friendly and responsive on all screen sizes.

- Conduct comprehensive testing to validate the accuracy and efficiency of the product sorting feature, checking for any potential bugs or performance issues.

#### Product Search Functionality

##### User Story

As a shopper, I want to be able to search for products by their names or description so that I can easily find specific products of my preference.

##### Acceptance Criteria

- The search functionality should provide relevant product results and search item counts based on the user's input.

- The system should return accurate search results that matches the keywords found in the product descriptions and or name.

- In exceptions where the search found no result, The user should be informed of that no results was found for their respective search.

- The search functionality should be responsive and provide users with a seamless experience across different devices and screen sizes.

##### Tasks

- Design and implement a user-friendly search bar interface that allows users to enter search queries.

- Develop a search mechanism that retrieves and displays relevant products based on the user's input and matches the search query with product names and descriptions.

- Integrate a responsive design approach to ensure that the search functionality is accessible and user-friendly on all screen sizes.

- Conduct a comprehensive testing to validate the accuracy and efficiency of the product search feature, checking for any potential bugs or performance issues.

**EPIC 5 - Purchasing and Checkout**

**Sprint 7**

#### Product Purchasing Customization

##### User Story

As a shopper, I want to be able to select the size and colour of a product to ensure that it fits my preferences and needs.

##### Acceptance Criteria

- The product colour and size options should be clearly presented on the product detail page.

- Users should be able to select the desired colour and size of the product from the available sizes and colour options provided by the system.

##### Tasks

- Design and implement a user-friendly product customization that retrieves and displays available colour and size options and enables users to select their preferred quantity, colour and size before checking out.

- Integrate input validation and error handling to ensure that users can only select valid size and colour options and input a valid quantity within the specified range.

- Test the product customization feature thoroughly to ensure its functionality, responsiveness and compatibility across different devices and screen sizes.

**Sprint 8**

#### Shopping Cart Management

##### User Story

As a shopper, I want to view all the items in my shopping cart so that I can ensure that my order is accurate before making a purchase.

##### Acceptance Criteria

- The shopping cart page should display a comprehensive list of all the items added to the cart, including their names, prices, quantity, colour and size variations if applicable.

- The shopping cart page should include options to update quantities, remove items, or continue shopping.

- The shopping cart page should provide clear instructions and options for users to edit quantities, remove items, or proceed to checkout as needed.

##### Tasks

- Design and implement a user-friendly shopping cart interface that displays a list of all added items and their corresponding details.

- Develop a shopping cart management system that allows users to update quantities, remove items or continue shopping seamlessly.

- Implement a tax and total cost calculation feature that dynamically updates the total cost based on the selected items and quantities in the shopping cart.

- Integrate a responsive design approach to ensure that the shopping cart interface is accessible, responsive and user-friendly on all screen sizes.

- Test the shopping cart functionality rigorously to ensure its accuracy and compatibility across different devices and screen sizes.

#### Cart Quantity Management

##### User Story

As a shopper, I want the option to increase or decrease the quantity of individual items in my cart so that I can make quantity adjustments before purchase.

##### Acceptance Criteria

- The shopping cart should include intuitive controls for users to adjust item quantity with clear visual feedback.

- The system should allow users to easily remove specific items from their cart with a single click or tap.

- Users should be able to adjust the quantity of individual items by using increment and decrement buttons.

##### Tasks

- Design and implement an intuitive quantity adjustment interface within the shopping cart that allows users to modify item quantities.

- Develop a cart management system that updates the total cost dynamically based on the adjusted quantities of individual items in the shopping cart.

- Implement a streamlined process for users to remove specific items from their cart with minimal effort, ensuring a smooth and efficient shopping experience.

- Conduct comprehensive testing to validate the accuracy and responsiveness of the quantity adjustment feature, checking for any potential bugs or performance issues.

#### Checkout Summary

##### User Story

As a shopper, I want to view the tax and total purchase amount before proceeding to checkout so that I can verify the accuracy of the billing details.

##### Acceptance Criteria

- The checkout summary should in detail display a breakdown of all the items in the cart along with their individual prices, quantities and subtotal for each item in the cart and the total amount, inclusive of taxes.

- The system should update the total purchase amount dynamically when items are added or removed from the shopping cart.

##### Tasks

- Design and implement a visually clear and concise checkout summary section displaying the breakdown of the total purchase amount.

- Develop a mechanism to update the purchase total in real time when items are added, removed or updated in the shopping cart.

- Integrate a tax calculation system to accurately calculate applicable taxes based on the customer's items in the cart.

- Implement a feature that allows customers to modify the quantity or remove items directly from the checkout summary.

- Conduct comprehensive testing to ensure that the purchase total is accurately calculated and displayed throughout the checkout process.

#### Order Confirmation Management

##### User Story

As a site user, I want to view clear and detailed order confirmation after completing my purchase so that I can be sure of an accurate and processed order.

##### Acceptance Criteria

- The order confirmation page should display a summary of the purchased items, the total cost, and the tax details.

- The order confirmation page should provide clear invoice of the pruchase details.

- Shoppers should be able to view a detailed summary of their purchased items, including names, email address quantity, tax and total amount in their order history.

##### Tasks

- Design and implement a visually appealing order confirmation page that displays a comprehensive summary of the purchased items and its details.

- Implement an order confirmation page that provides a clear invoice of the pruchase details.

- Develop an order management system that generates and populates the order confirmation page with accurate and up-to-date information after a successful checkout.

- Test the order confirmation feature thoroughly to ensure its accuracy, responsiveness, and compatibility across different devices and screen sizes.

#### Order Confirmation Email

##### User Story

As a shopper, I want to receive an email confirmation immediately after making a purchase so that I can have a record of my transaction for future reference.

##### Acceptance Criteria

- Users should receive an email confirmation of their purchase in their registered email inbox right after a purchase.

- The email confirmation should include a comprehensive summary of the purchased items, quantity, tax and total amount.

##### Tasks

- Configure the system to automatically send an email confirmation to users' registered email addresses immediately after a successful checkout.

- Design an email template that includes a detailed summary of the purchased items, tax and the total cost.

- Ensure that the email is sent from kidomarts official email address for trustworthiness.

- Integrate a secure and reliable email delivery system that ensures the timely delivery of email confirmations to users' inboxes.

- Conduct thorough testing to validate the accuracy and delivery of the email confirmation feature, checking for any potential issues with email formatting, content or delivery.

- Gather user feedback and monitor email delivery metrics to identify any potential improvements or adjustments that would enhance the overall user experience.

**Sprint 9**

#### Rating and Reviews

##### User Story

As a site user of the e-commerce website, I want to be able to read and submit reviews for products, as well as provide ratings based on my experience with the products, so that I can make informed purchasing decisions.

##### Acceptance Criteria

- When I visit a product page, I can see existing reviews and ratings for that product.

- I can submit a review for a product, including a title, text and a rating (1 to 5 stars) after i purchase that product.

- Review text should support multi-line and basic formatting.

- I can edit reviews that I have submitted. Only the user who submitted the review should have the ability to edit it.

- The product page should display the average rating based on all submitted reviews.

- Admin can moderate and remove inappropriate reviews.

##### Tasks

- Set up a database model for reviews and ratings.

- Implement logic for calculating and updating the average rating for each product.

- Design and implement a responsive UI component for displaying reviews on product pages.

- Create a form for submitting reviews. Integrate the form and review display components on product pages.

- Implement user authentication to track the user submitting the review. Ensure that only authenticated users who bought that specific product can submit or edit reviews and ratings on it.

- Implement admin functionality to moderate and remove reviews.

- Conduct integration testing for frontend components.

- Test the end-to-end flow of submitting, editing, and editing reviews.

**EPIC 6 - Documentation Epic**

**Sprint 10**

#### Documentation

##### User Story

As a developer, I want to provide a comprehensive documentation on my project so that other developers and users are able to know about the project's building process, how the website works and all the details involved in its use and functionality.

##### Acceptance Criteria

- The project documentation is organized into clear sections, such as introduction, architecture, planes, agile planning, features, testing, deployment and used technologies.

- Each section is well-detailed, providing comprehensive information about its respective topic.

- Use diagrams and charts to visualize complex concepts.

##### Tasks

- Set up a documentation table of content, dividing it into logical sections for clarity.

- Write up a clear concise and comprehensive documentation on the introduction, architecture, planes, agile planning, features, testing, deployment and used technologies of the project.

- Make use of comprehensive diagrams and charts like ERD to visualize complex concepts like database the schema.

## The-Scope-Plane

- Responsive Design - Site should be fully functional on all devices above 320px.
- Dropdown menu for product categories.
- Ability to perform CRUD functionality on user profile.
- Restricted role based features.
- Home page with site information.

## The-Structure-Plane

### Features

`USER STORY - As a developer, I need to create a logo so that users can easily identify the site by it as a brand`

Implementation:

**Logo**

A logo has been added to the top left corner of the site which is seen on all site pages. This helps users to easily identify the site.

![Logo](media/docs/readme-images/logo-kidomart.jpg)

`USER STORY - As a developer, I need to create the navbar so that users can navigate the website from all sizes of devices`

Implementation:

**Navigation Menu**

The Navigation contains links for the logo, categories dropdown menu, search bar, user first name display, dashboard and logout links for logged in users and login and register links for unauthenticated users. It also has the cart button on the right corner and a free delivery promotional text at the center bottom of it.

The category dropdown button that helps users to sort the products by category.
There is also a search bar that allows users to easily look for specific products.
The cart button that displays the users cart count also and leads autheticated users to their cart items and keeps record of their carts as well.
When logged in, there is a user dashboard link that leads the user to his profile for order views, profile editing and deletion as well as password change.
Beside it is a logout link that logs out logged in users.

The following navigation items are available on all pages:

- Logo -> index.html - Visible to all
- Searchbar -> search - Visible to all
- Dropdown menu -> category.geturl - Visible to all
- Dashboard -> dashboard.html - Visible to logged in users
- Login -> login.html - Visible to logged out users
- Register -> register.html - Visible to logged out users
- Logout -> logout - Visible to logged in users

The navigation menu is displayed on all pages and is reponsive on all devices. This will allow users to view the site from any device without difficulty.

![Navbar](media/docs/readme-images/navbar-kidomart.jpg)

`USER STORY - As a developer, I need to create a footer with my social media business handles, contact details and newsletter subscription so that I can market my brand and communicate with my users`

Implementation:

**Footer**

A footer has been added to the bottom of the site which is seen on all site pages. This helps me to communicate to my site users and market my brand.

In the footer, I have provided the shops customer care number and email address for shoppers to be able to contact me on business related issues. I have also provided my social media business handles to market my brand and also for users to interact and communicate with my brand. In the middle is a newsletter form that helps me market my brand as well.

![Footer](media/docs/readme-images)

`As a shopper, I want the ability to sort the list of products by category so that I can easily find products in my preferred category.`

Implementation:

**Product categories menu**

On the top of the navabar, there is a category dropdown menu that drops with the All, Clothing, Dolls, Electronics and Education, Other, Toys and Lego, Beauty and accessories menu.

![Categories Menu](media/docs/readme-images/category-dropdown.jpg)

When the user clicks on any of the menu items, the respective category opens.

![Clothing Category](media/docs/readme-images/clothing-category.jpg)

`As a shopper, I want to be able to search for products by their names or description so that I can easily find specific products of my preference.`

Implementation:

**Search bar**

When a user types in a search input in the search bar located in the middle of the navbar, the search result is displayed on the page if the search is found.

![Search Found](media/docs/readme-images/search.jpg)

If there is no search result found, a message is displayed to let the user know about the state of the search result.

![Search Not Found](media/docs/readme-images/search-not-found.jpg)

`USER STORY - As a shopper, I want to see a list of all available products so that I can browse through and make informed purchase decisions.`

Implementation:

**Home Page**

The home page contains a logo that is informative enough to let users know that the site Kiod Mart is Mart for Kids.
The displayed products also throws more light on the type of products we sell.

Below the navbar is a nice carousel that slides images of three children with left and right arrows that could manually do the sliding as well.
In the middle of the page, are list of products.
Each product has an image, name, price and its associated rating below it.

The page takes twelve products at a go in pagination. Therefore at the bottom of each twelfth post is the 'next' button that takes users to subsequent pages. When users are on older posts, they can easily come back to fresher posts by clicking the 'prev' button.
Then come the footer which is found also on all pages.

`Logged in`
![Home page logged in](media/docs/readme-images/home-logged-in.jpg)

`Default`
![Home page default](media/docs/readme-images/home-logged-out.jpg)

`As a shopper, I want to view detailed product information, including descriptions, images, ratings, reviews and pricing, so that I can make informed purchase decisions.`

Implementation:

**Product Details Page**

When a user clicks a product's name or image from the home page, It takes them right to the product detail page.

On the product details page, there is a card in which the product image, name, rating, price, description, size and or color select buttons, add to cart button and back buttons are found.

Below the card is the review and rating section with five empty rating stars and a review form that comes with title and text fields. Below that is the existing rating and reviews if applicable. A logged in user who has purchased a product will see the submit review button that enables him or her to review and rate that particular product.

![Product details](media/docs/readme-images/product-details-loggedin.jpg)

![Product details](media/docs/readme-images/product-details.jpg)

`USER STORY - As a site user, I want to easily create a personal account to access personalized features so that I can make future purchases securely and efficiently.`

Implementation:

**Register Page**

Upon clicking the register link anywhere on the site, users are directed to the registration page to make a registration in order for them to be able to get full access to the site's features and most especially place orders.

On the top of the page is a heading and text that informs the user on the page's purpose.

Below that is the form for username, email address, phone number, password and password confirmation fields. Beneath that is the register button that enables users to register on the site.

Then comes the login alternative text and link for users who are already registered.

![Register](media/docs/readme-images/register.jpg)

After a successful registration, a success message is displayed to the user.

![Registration success](media/docs/readme-images/registration-alert.jpg)

An activation email is then sent to the user with a secure link to activate their account.

![Register](media/docs/readme-images/register-activation-email.jpg)

Upon clicking the link in the email, user is taken to the login page with an activation success message.

![Register](media/docs/readme-images/registration-successful.jpg)

In cases where there are errors in filling the registration form, the user is prompted by an error message on the specific error.

![Register error](media/docs/readme-images/registration-error.jpg)

`USER STORY - As a returning customer, I want to be able to log in quickly and securely so I can access my personalized account settings and order history.`

Implementation:

**Login Page**

Upon clicking the log in link anywhere on the site, users are directed to the log in page to log in so that they can be able to get full access to the site's features.

The login form has email address and password fields alogside a forgot password link.

Below that is the login button the logs the user in upon a click or a tap.

On the top of the page is a heading and text that informs the user on the page's purpose.

Below the login form is a register text and link that enable users to register if they do not have an account.

Upon a successful login, the user is redirected to his dashboard with a success message.

![Login](media/docs/readme-images/login.jpg)

In cases where user's credentials are invalid, an error message is displayed to alert the user.

![Login error](media/docs/readme-images/login-error.jpg)

Upon clicking the logout link on the navbar or on the dashboard sidebar, users are directly logged and redirected to the login page with a logout success message.

![Logout](media/docs/readme-images/logout.jpg)

`USER STORY - As a user, I want the option to reset my password easily if I forget it, so that I can regain access to my account and protect my profile and data.`

Implementation:

**Reset Password Page**

When the user clicks on the forgot password link within the login form, right on top of the login button, he is taken to the reset password page. On this page, he or she only needs to fill in the email address he registered with and click on submit.

On the top of this page is a heading that informs users on the page's purpose and a text that provides clear instructions for resetting password.

Below the email field is a login link that provides easy login access to the user in case he or she remembers his or her password before the reset action.

![Password reset page](media/docs/readme-images/password-reset.jpg)

After the user inputs his or her email (the one he registered with), a verification email is sent to this email address.

![Password reset email](media/docs/readme-images/password-reset-email.jpg)

The user is then redirected to the login page with a message that informs him or her on the sent email for password reset.

![Password reset message](media/docs/readme-images/password-reset-msg.jpg)

When the user is verified upon clicking the link in the email, the user is redirected to the password reset page and allowed to reset his or her password.

![Reset Password Page](media/docs/readme-images/reset-password.jpg)

After the user has successfully changed their password, he or she is redirected to the login page with a success message informing them on the success of the password reset. Then he or she can login with the new password.

![Password Reset success](media/docs/readme-images/password-reset-success.jpg)

Error handling has been implemented solidly to take care of all steps within the password reset process. Right from the beginning of the process, if the user is not registered, he or she is not allowed to start the process at all. Very strict and secured mechanisms has been implemented with the custom user model to secure user accounts.

![Password Reset success](media/docs/readme-images/Reset-error.jpg)

The password reset link is also secured with expiration for user accout security. If the link is expired, the user is alerted wth an error message to restart the verification process. User account with multiple password reset trials within a short range of time might be suspended for stricter verification.

![Password Reset link](media/docs/readme-images/expired-reset-link.jpg)

`USER STORY - As a site user, I want to create a personal profile so that I can easily view my order confirmation and history as well as save and manage my profile.`

Implementation:

**Dashboard**

Only registered users are allowed access to the dashboard. The dashboard has a sidebar on the left side. This side bar has a menu consisting of My Orders, Edit Profile, Change Password, Delete Account and a logout button below it.

On the right side is card divided into two. The first side consists of the user's order count and a link to the users order history. While the second side of the card consists of the user's profile image email address and phone number.

![Dashboard Page](media/docs/readme-images/dashboard.jpg)

On the dashboard, when the user clicks on 'My orders' menu, he or she is taken to the order history page where they can view their order history. The 'View Orders' link in the first part of the card also leads to this order history page.

![My Orders Page](media/docs/readme-images/my-orders.jpg)

On the 'My Orders' page, when the user click on order number he or she is redirected to the order details of that particular order.

![Order Details](media/docs/readme-images/order-detail.jpg)

On the dashboard, when the user clicks on the 'Edit Profile' menu, he or she is taken to the edit profile page where they can update their profile details.

![Profile Update](media/docs/readme-images/profile-update.jpg)

When the profile update is successful, a success message alerts the user on the success of the update.

![Profile Update Success](media/docs/readme-images/profile-edit-success.jpg)

On the dashboard, when the user clicks on the 'Change Password' menu, he or she is taken to the change password page where they can change their password.

![Password Change Page](media/docs/readme-images/change-password.jpg)

When the password change is successful, the user is redirected to the password change success page with buttons to login or go to the home page.

![Password Change Success Page](media/docs/readme-images/password-change-success.jpg)

On the dashboard, when the user clicks on the 'Delete Account' menu, he or she is taken to the account deletion confirmation page where they can confirm the deletion of their account.

![Account Deletion Page](media/docs/readme-images/delete-account.jpg)

After the user confirms the deletion of their account, he or she is first logged out automatically by the system and redirected to the resgister page with a log out and an account deletion succces message.

![Account Deletion success](media/docs/readme-images/acc-delete-success.jpg)

`USER STORY - As a shopper, I want to be able to select the size and colour of a product to ensure that it fits my preferences and needs.`

Implementation:

**Product variation selection**

Users are given the option to select the colour and or sizes of the product(s) they want to buy on the product detail page before they add the item(s) to their cart (that is if the product has colour or size or both).

![Product detail variation selection](media/docs/readme-images/item-variation.jpg)

`USER STORY - As a shopper, I want to view all the items in my shopping cart so that I can ensure that my order is accurate before making a purchase.`

Implementation:

**Cart**

After the user has selected item(s) from the post detail page and clicked on the add to cart button, They are redirected to the cart page where their slected item(s) are displayed with its coresponding tax, quantity, price, item and its variation details. The total amonut is also displayed on the cart page side bar. In this side bar is the checkout button that leads to the checkout page and the continue shopping button that leads to the home page.

If the user already has cart item(s), the cart button on the navbar can also take the user to the cart page where they will find the items in their cart.

`USER STORY - As a shopper, I want the option to increase or decrease the quantity of individual items in my cart so that I can make quantity adjustments before purchase.`

Implementation:

**Cart**

On the cart page, they can increase the quantity of any of the item(s) by clicking or taping the '+' button below the quantity section, decrease the quantity of any of the item(s) by clicking or taping the '-' button below the quantity section or click on the 'Remove' button to take off that particular item from their cart.

When the cart item quantity is 1, and the decrease button is clicked, the cart item will be removed from the cart meaning it is decreased to 0 which should be nothing or 0.

Before an item is removed from the cart, the user is alerted to confirm the item removal and when they consent to it, the item is successfully removed from the cart.

![Cart Page](media/docs/readme-images/cart.jpg)

`USER STORY - As a shopper, I want to view the tax and total purchase amount before proceeding to checkout so that I can verify the accuracy of the billing details.`

Implementation:

**Checkout Page**

On the right hand side of the checkout page on big screens and below the checkout form on small screens, there is a card that contains the product details of the item(s) a user is about to purchase viz; product name, image, variations (if applicable), quantity and price. Below that are the 'check cart' and 'continue shopping' buttons.

At the bottom of the checkout form is the calculated total tax and grand total of the potential purchase which informs the user on the total amount they will be paying for and its corresponding tax.

Then comes the 'complete order' button for placing the order.

Below the 'complete order' button is a warning message that asks users to stay on the page while their order is been processed.

![Checkout Page](media/docs/readme-images/checkout-page.jpg)

`USER STORY - As a site user, I want to view clear and detailed order confirmation after completing my purchase so that I can be sure of an accurate and processed order.`

Implementation:

**Checkout Success Page**

After a user has filled out the form fields and card details on the checkout page above, he or she is redirected to the checkout success page with a payment success message.

The checkout success page contains the invoice of the user's purchase details viz; order number, transaction id, order status, order date, item name, item quantity, item variation(if applicable), grand total and the users billing address.

On top of the page is a heading that tells the purpose of the page and a message below it that informs the user about an email sent to him or her. Below it is a button that takes the user back to the home page if they want.

![Checkout Success Page](media/docs/readme-images/payment-success.jpg)

Error handling has been fully implemented to take care of all possible errors during the payment process. So in cases where there are hitchtes or interruption during the payment process, the user is assured of accurate updates on their payment status and they are informed about what precisely transpired during the payment process.

![Checkout Error](media/docs/readme-images/checkout-error.PNG)

`USER STORY - As a shopper, I want to receive an email confirmation immediately after making a purchase so that I can have a record of my transaction for future reference.`

Implementation:

**Checkout Success Email**

An email is also automatically sent to the user with details to confirm and provide purchase details.

![Checkout Success Email](media/docs/readme-images/checkout-success-email.png)

**Error Pages**

`USER STORY - As a developer, I need to implement a 404 error page to alert users when they have accessed a page that does not exist`

Implementation:

**404 Page**

As a developer, I need to implement a 404 error page so that users are redirected there when they try to access a page that is not available to them.

A 404 page has been implemented and will display if a user navigates to a broken link or a page they are not suppose to have access to.

The 404 page will allow the user to easily navigate back to the Home page through the 'back' button

![404 error page](media/docs/readme-images/404.jpg)

`USER STORY - As a developer, I need to implement a 403 error page to alert users when accessing a page or view that they do not have permission to view`

Implementation:

**403 Page**

Likewise, a 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URL's and attempt to edit, delete or access pages that are restricted.

`USER STORY - As a developer, I need to implement a 500 error page to alert users when an internal server error occurs`

Implementation:

**500 Page**

A 500 error page has also been implemented to alert users when an internal server error occurs.

**Favicon**

    * A site wide favicon was implemented.
    * This provides an image in the tabs header to allow the user to easily identify the website if they have multiple tabs opened.

![Favicon](static/favicon.ico/favicon.ico)

### Features Left To Implement

- In a future release I would like to implement the address field with the use of django's AddressField. This will make it easier for users to input their addresses.
- I will also want to provide a variety of payment methods like paypal for user's payment convenience.

## The-Skeleton-Plane

### Wireframes

- Home page

![Home Page lg](media/docs/readme-images/wireframe-home-lg.jpeg)

![Home Page md](media/docs/readme-images/wireframe-home-md.jpeg)

![Home Page sm](media/docs/readme-images/wireframe-home-sm.jpeg)

- Register page

![Register Page lg](media/docs/readme-images/wireframe-register-lg.jpeg)

![Register Page md](media/docs/readme-images/wireframe-register-md.jpeg)

![Register Page sm](media/docs/readme-images/wireframe-register-sm.jpeg)

- Registration Success page

![Registration Success lg](media/docs/readme-images/wireframe-thanks-register-lg.jpeg)

![Registration Success md](media/docs/readme-images/Thanks-register-md.jpeg)

![Registration Success sm](media/docs/readme-images/wireframe-thanks-register-sm.jpeg)

- Login page

![Login Page lg](media/docs/readme-images/wireframe-login-lg.jpeg)

![Login Page md](media/docs/readme-images/wireframe-login-md.jpeg)

![Login Page sm](media/docs/readme-images/wireframe-login-sm.jpeg)

- Checkout Page

![Checkout Page lg](media/docs/readme-images/wireframe-checkout-lg.jpeg)

![Checkout Page md](media/docs/readme-images/wireframe-checkout-md.jpeg)

![Checkout Page sm](media/docs/readme-images/wireframe-checkout-sm.jpeg)

- Checkout Success Page / Invoice

![Checkout Success Page lg](media/docs/readme-images/wireframe-invoice-lg.png)

![Checkout Success Page md](media/docs/readme-images/wireframe-invoice-md.png)

![Checkout Success Page sm](media/docs/readme-images/wireframe-invoice-sm.png)

- Dashboard page

![Dashboard page lg](media/docs/readme-images/wireframe-dashboard-lg%20.png)

![Dashboard page md](media/docs/readme-images/wireframe-dashboard-md.png)

![Dashboard page sm](media/docs/readme-images/wireframe-dashboard-sm.png)

- My orders

![My Order page lg](media/docs/readme-images/wireframe-my-orders-lg.png)

![My Order page md](media/docs/readme-images/wireframe-my-order-md.png)

![My Order page sm](media/docs/readme-images/wireframe-my-order-sm.png)

- Edit Profile page

![Edit Profile page lg](media/docs/readme-images/wireframe-edit-profile-lg.png)

![Edit Profile page md](media/docs/readme-images/wireframe-edit-profile-md.png)

![Edit Profile page sm](media/docs/readme-images/wireframe-edit-profile-sm.png)

- Change Password page

![Change Password page lg](media/docs/readme-images/wireframe-change-password-lg.png)

![Change Password page md](media/docs/readme-images/wireframe-change-password-md.png)

![Change Password page sm](media/docs/readme-images/wireframe-change-password-sm.png)

- Cart page

![Cart page lg](media/docs/readme-images/wireframe-cart-lg.jpeg)

![Cart page md](media/docs/readme-images/wireframe-cart-md.jpeg)

![Cart page sm](media/docs/readme-images/wireframe-cart-sm.jpeg)

- Empty Cart page

![Empty Cart page lg](media/docs/readme-images/wireframe-empty-cart-lg.jpeg)

![Empty Cart page md](media/docs/readme-images/wireframe-empty-cart-md.jpeg)

![Empty Cart page sm](media/docs/readme-images/wireframe-cart-empty-sm.jpeg)

- Account Delete Confirmation page

![Account Delete Confirmation page lg](media/docs/readme-images/wireframe-account-delete-lg.png)

![Account Delete Confirmation page md](media/docs/readme-images/wireframe-account-delete-confirm-md.png)

![Account Delete Confirmation page sm](media/docs/readme-images/wireframe-account-delete-confirm-sm.png)

- 403 error page

![403 Error Page lg](media/docs/readme-images/wireframe-403-lg.jpeg)

![403 Error Page sm](media/docs/readme-images/wireframe-403-sm.jpeg)

- 404 error page

![404 Error Page lg](media/docs/readme-images/wireframe-404-lg.jpeg)

![404 Error Page sm](media/docs/readme-images/wireframe-404-sm.jpeg)

- 500 error page

![500 Error Page lg](media/docs/readme-images/wireframe-500-lg.jpeg)

![500 Error Page sm](media/docs/readme-images/wireframe-500-sm.jpeg)

### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The custom user account model is at the heart of the application as it is connected to the registration, profile editing and deleting, password reset and change, purchasing, automated email reception, review and rating. It is linked by primary/foreign key relationships.

The custom Account model which is the core model of the app is tied to the the Order model, the CartItem model, ReviewRating model and LogEntry as foreign keys. The UserProfile model relates to the Account model as a one-to-one relationship for custom account and user profile management. 

The Product model on the other hand which has the Category model as its foreign key is tied to the OrderProduct model, ProductVariation model, CartItem model and the RateReview model as foreign keys.

The entity relationship diagram below shows the schemas for each of the models and how they are related.

![Entity Relationship Diagram](media/docs/readme-images/ERD.JPG)
