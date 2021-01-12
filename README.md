<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1604163817/ms4%20images/unicorn_ozbxlz.png" width="200" height="200" alt="Thank you for visiting my Readme"></p>

[![nicknacks on Heroku](https://img.shields.io/badge/Heroku-nicknacks-pink)](https://ms4nicknacks.herokuapp.com/)
[![Deployed preview](https://res.cloudinary.com/dugnokxox/image/upload/v1609882886/ms4%20images/nicknacks_eqitvq.png)](https://ms4nicknacks.herokuapp.com/)




# Intro


<p align="center">This task is the final project for the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course. 
This project is an eCommerce shop front to host decorative pins, keychains and cute stationery. The name chosen for the website is nicknacks, which means in free translation "this and that". The name choice will allow administrator to expand on the produce offered.</p>

<p align="center">The site is worked within Django structure, sent live on Heroku, utilizes AWS S3 to have media and static records. Locally, it utilizes the inherent Django Db.sqlite3 information base, though when conveyed live it uses Heroku's Postgres information base. Authentication functionality is provided by Django's Allauth: administrator superuser can add and alter things in the Products and Categories applications, while visiting clients can enlist and login, accessing vestige depictions and their request history in the Checkout and Profile applications. A section has also been made available to the enlisted client, to add their own drawings, which can in due course be used as designs of their own. This is analysed furthermore in this readme, under the relevant heading.</p>

* [UX](#goals)
  * [Goals](#goals)
  * [Target Audience](#target-audience)
  * [Business Goals](#business-goals)
  * [Customer Goals](#customer-goals)
  * [User Stories](#user-stories)
    * [Viewing and Navigation](#viewing-and-navigation)
    * [Registration and Users Accounts](#registration-and-users-accounts)
    * [Sorting and Searching](#sorting-and-searching)
    * [Admin and Store Management](#admin-and-store-management)
  * [Design](#design)
    * [Font](#font)
    * [Color Scheme](#color-scheme)
    * [Wireframes](#wireframes)
    * [Registration and User Accounts](#registration-and-users-accounts)
* [Database Structure](#)
* [Features](#)
* [Technology](#)
* [Testing](#)
* [Deployment](#)
* [Credits](#)



<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/user_experience_cpzk3c.png" width="auto" height="70" alt="UX"></p>

# Goals

<p align="center">The main goal of the nicknacks is to sell beautiful hand made accessories. Secondly, through that website people can order something they have designed and desire to have made into piece of accessory or piece of stationery</p>

# Target Audience

- Users aged 8 to 80
- Users interested in cute accessories and stationery
- Users with interest in accessory and stationery design and production for their own use

# Business Goals

- To create a platform that enables the prospect client to find and purchase the product they like
- To enable prospect user to submit their design and have it either just stored or even produced
- In order to increase the retention, encourage users to register
- Offer a presentable design of the website, with the use of neumorphic design, to increase aesthetic appeal
- Offer easy interaction on the page

# Customer goals

- Finding product that fits their taste
- Buy product through an easy payment flow
- Upload their own designs and store them in their registered account
- Place order for their designs, to have them produced
- See their previous purchases

# User Stories

### Viewing and Navigation		
- As a shopper I want to be able to view the list of products to purchase some
- As a shopper I want to be able to view individual product details to identify the price and description
- As a shopper I want to be able to quickly identify  special offers to take advantage of special savings on products I'd like to buy
- As a shopper I want to be able to easily view the total of my purchases at any time to see the history of my purchases and how much I spent.

### Registration and User Accounts  
- As a registered shopper I want to be able to easily register for an account so I can have a personal account, be able to see what I purchased or designs I uploaded
- As a registered shopper I want to be able to easily login or logout so I can access my personal account information
- As a registered shopper I want to be able to easily recover my password in case I forget it so I can recover access to my account
- As a registered shopper I want to be able to receive an email confirmation after registering so I can verify that my account registration was successful
- As a registered shopper I want to be able to have a personalised user profile so I can view my personal order history and order confirmations and save my payment information
- As a registered shopper I want to be able to add my own personalised design so I can view all my designs and choose which one I would like to order
- As a registered shopper I want to be able to place an order for my personalised design so I can have my design made into pin, keyring or a piece of stationery
- As a registered shopper I want to be able to easily contact the store owner with any queries I might have so I can ask any questions I may have

### Sorting and searching  
- As a shopper I want to be able to sort the list of available products so I can easily identify the best rated, best priced and categorically sorted products
- As a shopper I want to be able to sort a specific category of products so I can find best priced or best rated product in a specific category or sort the product in that category by name
- As a shopper I want to be able to sort multiple categories of products simultaneously so I can find the best priced or best rated products across board categories, such as pins or keyrings
- As a shopper I want to be able to search for a product by name or description so I can find a specific product I'd like to purchase
- As a shopper I want to be able to easily see what I have searched for and the number of results so I can quickly decide whether the product I want is available
Purchasing and Checkout  
- As a registered shopper I want to be able to easily select quantity of a product when purchasing it so I can ensure I am selecting correct product and a correct quantity
- As a registered shopper I want to be able to view items in my bag to be purchased so I can identify the total cost of my purchase and all items I will receive
- As a registered shopper I want to be able to adjust the quantity of individual items in my bag so I can easily make changes to my purchase before checkout
- As a registered shopper I want to be able to easily enter my payment information  so I can check out quickly and with no hassle
- As a registered shopper I want to be able to feel that my personal and payment information is safe and secure so I can confidently provide the needed informatoin to make a purchase
- As a registered shopper I want to be able to view an order confirmation after checkout so I can verify that I have not made any mistakes
- As a registered shopper I want to be able to receive an email confirmation after checking out so I can keep the records of my purchases

### Admin and Store Management  
- As a store owner I want to be able to add a product as this would enable me to add new items to my store
- As a store owner I want to be able to Edit/Update product to apply any changes, be it in price, description, image or other product criteria
- As a store owner I want to be able to delete a product remove product if they are no longer for sale

# Design

### Font

Throughout the project there is only one font used, which is Montserrat at various weighs. The aim is to make this website as minimalist and clean as possible, to make the neumorphic effect stand out more.

### Color Scheme

The use of neumorphic design througout the page influenced a decision of one main color being used. The color used throughout the page is pale and light, almost white, as this ensures best effectivens of the design style.

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609881480/ms4%20images/Screenshot_2021-01-05_at_21.17.21_nua89x.png" alt="Database Structure"></p>

### Wireframes


<details><summary>All Products - Mobile and PC</summary>
 
![](https://res.cloudinary.com/dugnokxox/image/upload/v1610107297/eCommerce_Web_Design-12_lxaltd.jpg)
</details>

<details><summary>Product Detail - Mobile and PC</summary>
 
![](https://res.cloudinary.com/dugnokxox/image/upload/v1610107297/eCommerce_Web_Design-13_x9sx3z.jpg)
</details>

<details><summary>Register Account - Mobile and PC</summary>
 
![](https://res.cloudinary.com/dugnokxox/image/upload/v1610107296/eCommerce_Web_Design-15_vyz1iw.jpg)
</details>

<details><summary>Sign In - Mobile and PC</summary>
 
![](https://res.cloudinary.com/dugnokxox/image/upload/v1610107297/eCommerce_Web_Design-14_2_onyqe4.jpg)
</details>

<br><br>

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/database_structure_k2dbcm.png" width="auto" height="70" alt="Database Structure"></p>
<br><br>
<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/features_bm7mnk.png" width="auto" height="70" alt="Features"></p>

- Products to purchase through an ecommerce system
- A dedicated Design section for the registered user to upload their own designs
- A dedicated Order section for the registered user to order their own designs
- Administration panel so superuser can add, edit and delete products
- Profile page where registered shopper can see their order history
- Contact button through which both registered and not registered user may send a message to the superuser.

All pages share navigation bar with logo to the left, which once clicked on, takes you home from any page.

In the middle there are four call to action buttons:
-  Everything - Option that returns a dropdown list with Items sorted in accordance to price, rating, category and just last option, everything
- Pins - Option returning the main hero of this website, which are all Pins. Upon clicking on this option the user will be able to choose from Animals, Things, People, Plants and finally, just head to all Pins. 
- Randoms - By clicking on this the user will be faced with three choices, Keychains, Stickers and Stationery
- Special Offers - this dropdown list contains two positions which are visible to the non logged users, which are New and Sale items, as well as the position which is only available if user is logged in. This is Your Designs, weher user may be able to check out the Design they uploaded, as well as order them
To the right corner in the PC view there are two CTA buttons: My Account and a Basket.
- My Account:
For the registered and while logged in user that is not a superuser, they will be able to add Custom Drawing/Design, Check out their Profile, which contains history of purchases. By clicking on this option, the logged in user will be able to log out from their session
For the regisered and logged in as a superuser, the user will be able to do all of the above plus Manage the main products of the ecommerce. This will include adding, editing and deleting the products."
- Basket 
This option is available to both logged in and not logged in users. The difference is, only logged in user will be able to successfully check out with the items, as this option is for the time being only made available to the logged in user.
<br><br>
<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/technologies_mr6sj9.png" width="auto" height="70" alt="Technologies"></p>

[![Gitpod](https://img.shields.io/badge/IDE-Gitpod-blue)](https://www.gitpod.io/)
[![Github](https://img.shields.io/badge/Remote%20code-Github-white)](https://github.com/)
[![Photoshop](https://img.shields.io/badge/Photoediting-Photoshop-lightblue)](https://www.adobe.com/ie/products/photoshop.html)
[![Goodnotes](https://img.shields.io/badge/Wireframes-Goodnotes-Orange)](https://www.goodnotes.com/)
[![Pixlr.com](https://img.shields.io/badge/Image%20editing-Pixlr-blue)](https://pixlr.com/x/)
[![Cloudinary](https://img.shields.io/badge/Cloud%20image%20storing-Cloudinary-0F4E97)](https://cloudinary.com/)
[![HTML](https://img.shields.io/badge/Mark%20up%20text-HTML-yellow)](https://www.w3schools.com/html/html_intro.asp)
[![CSS](https://img.shields.io/badge/Styling-CSS-blueviolet)](https://www.w3schools.com/css/)
[![JavaScript](https://img.shields.io/badge/JS%20Functionality-JS-darkgreen)](https://jquery.com/)
[![Bootstrap](https://img.shields.io/badge/Design%20Framework-Bootstrap-%23F5A4A7)](https://getbootstrap.com/)
[![Django](https://img.shields.io/badge/Microframework-Django-%238B0000)](https://www.djangoproject.com/)
[![Shields](https://img.shields.io/badge/Readme%20Badges-Shields-lightgrey)](https://shields.io/)
[![Heroku](https://img.shields.io/badge/App%20Hosting-Heroku-%237B68EE)](https://www.heroku.com/home)
[![Python](https://img.shields.io/badge/Back%20end%20programming-Python-%09%23008000)](https://www.python.org/)
[![SQlite3](https://img.shields.io/badge/SQLite-Production%20Database-yellowgreen)](https://www.sqlite.org)
[![AWS Services](https://img.shields.io/badge/AWS%20-Services-orange)](https://aws.amazon.com/)
[![W3C HTML Validator](https://img.shields.io/badge/HTML%20Validator-W3C%20HTML%20Validator-red)](https://validator.w3.org/)
[![W3C CSS Validator](https://img.shields.io/badge/CSS%20Validator-W3C%20CSS%20Validator-darkred)](https://jigsaw.w3.org/css-validator/)
[![Pep8 Online](https://img.shields.io/badge/Python%20Validator-PEP8%20online-white)](http://pep8online.com/)
[![JShint](https://img.shields.io/badge/JS%2FjQuery%20Validator-JSHint-%23008e94)](https://jshint.com/)
<br>
<br>
<br>
<br>
<br>
<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/testing_ioxxts.png" width="auto" height="70" alt="Testing"></p>

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1610112449/ms4%20images/PFCMNF1_0.5x_ns8gtj.png" alt="All screens"></p>

### Product Features

|  Feature |  Action | Effect |
|---|---|---|
| Logo (upper left corner)  |  Hover over |  The address on hover is showing as home page |
| Search bar  |  Entered "Space", |<ul><li> one product is listed under this name - correct</li><li>The summary shows message "1 Products found for 'space'" (See if this can be amended to dependable if it's one or many, with or without s"</li>|
|  All button, bringing back to all products |  Click on All button |  Linked correctly  |
| Everything  |  Click on By Price |  Items appear sorted ascending, from low price to high |
|   |  Click on By Rating |  Items appear sorted descending, from high rating to low |
|   |  Click on By Category |  Categories of Items become sorted alphabetically |
|   |  Click on Everything |  All items are displayed, sorted by SKU |
| Pins  |  Click on Animals |  Pins from that Category are displayed, the badge on top of the page also states what Category we are at. |
|   |  Click on Things |  Pins from that Category are displayed, the badge on top of the page also states what Category we are at. |
|   |  Click on People |  Pins from that Category are displayed, the badge on top of the page also states what Category we are at. |
|   |  Click on Plants |  Pins from that Category are displayed, the badge on top of the page also states what Category we are at. |
|   |  Click on All Pins |  All Pins are displaying now |
| Randoms  |  Click on Keychains |  Keychains are displayed, the badge on top of the page states same. |
|   |  Click on Stickers |  Stickers are displayed, along with badge |
|   |  Click on Stationery |  Stationery and badge are here |
| Special Offers  |  Click on New Arrivals |  New Arrivals and badge are here |
|   |  Click on Sale |  Pins from that Category are displayed, the badge on top of the page also states what Category we are at. |
| My Account  |  Click on Register |  <ul><li>Sign up form appears</li><li>Form sends</li><li>Confirmation email appears in the email box</li><li>Clicked on the confirmation email - Confirm email address page appears</li><li>Logged in with newly created account - the success message appears and I am now logged in</li><li>Upon clicking Confirm, a success message appears and a signing page is returned</li><li></li></ul> |
|   |  Click on Login |  The address on hover is showing as home page |
| Basket  |  Bag empty |  Click on Keep Shopping button, brings me back to all Products page |
|   |  Bag with content | <ul><li>Increase and Decrease quantity buttons work</li><li>Price updates when Update option is clicked</li><li>Price in Grand total Updates over the 10% Delivery</li><li>Free Delivery treshold is calculated correctly and called back to user |
| Footer  |    |   |
| | Home page | |
| Shop Now button  |  Clicked on |  Brings me to a page with all products |
| | All Products page | |
| Sort Products Dropdown  |  Sort testing each Condition |  <ul><li>Price (low to high) - sorts according to price, from cheapest to dearest</li><li> Price (high to low) - sorts according to price, from dearest to cheapest</li><li>Rating (low to high) - sorts rating from lowest</li><li>Rating (high to low) - sorts rating from highest.</li><li>Name (A-Z) - sorts Products alphabetically</li><li>Name (Z-A) - sorts products reverse-alphabetically</li><li>Category (A-Z) - sorts Categories of products alphabetically</li><li>Category (Z-A) - sorts Products by Categories sorted reverse-alphabetically</li></ul> |
| Superuser - editing the product details  |  Click on the Edit option underneath one of the products |  <ul><li>A Product Management Edit a Product form is rendered and a warning message is triggered in upper right corner</li><li>Changed Category and Name,saved</li><li>Name and Category successfully changed, confirmed with a success toast rendered in upper right corner </li></ul> |
|   |  Click on the Delete option |  Product is immediately deleted and a success toast confirming deletion is rendered in the upper right corner of the page |
| Adding product to the basket  |  Click on the Product and click Add to Basket |  <ul><li>Basket total updates to the correct amount, success toast confirms the product was added to the bag </li></ul> |
| Navigating from Product Detail back to All Products  |  Click on the Keep Shopping button |  A page with all product is rendered |
| Checking out  |  Click on the Shopping Bag, click on Secure Checkout |  <ul><li>Non registered user - a sign in page renders with option to register, if user is not yet registered</li><li>Registered User - A Checkout page is rendered with most information saved as per users account. User can also see the Order Summary to the right of the form</li><li>Entered card details and name, after which clicked on the Complete Transaction button</li><li>A thank you page is rendered, with a summary of order as well as the success toast renders in upper right corner</li><li>Confirmation email arrives to the email box</li></ul> |

### For testing the Stripe checkout use the following:

 - __Card number__: 4242 4242 4242 4242
 - __CVC__: any 3 digits
 - __Card expiry date__: any future date
 - __ZIP/Postcode__: any 5 digits
 
 
<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1610112217/ms4%20images/Mobile_mock_up_puqyce.png" alt="Mobile  mockup"></p>


### Users Features

|  Feature |  Action | Effect |
|---|---|---|
| Registration  |   |   |
| Login  |   |   |
| Logout  |   |   |
| Change Password  |   |   |
| View profile  |  Click on My Account and My Profile |  |
| Update profile  |  Click on My Account and My Profile |   |
| Logo (upper left corner)  |   |   |

### User Stories Testing

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1610130216/ms4%20images/186_0.5x_rlizkx.png" alt="User Stories Testing"></p>

|  Feature |  Action | Effect |
|---|---|---|
| Registration  |   |   |
| Login  |   |   |
| Logout  |   |   |
| Change Password  |   |   |
| View profile  |  Click on My Account and My Profile |  |
| Update profile  |  Click on My Account and My Profile |   |
| Logo (upper left corner)  |   |   |

### Error pages testing

#### 404

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1610295737/ed53286c91f7bc0591961a39a1d61366be452ab0_cikwpt.gif" alt="Error 404 Screenrecording"></p>

#### 500

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1610295914/fe381bc034796c3bc0f0d9a62449f24595ad9a6f_ipukmj.gif" alt="Error 500 Screenrecording"></p>


<br><br>
<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/deployment_o0onfb.png" width="auto" height="70" alt="Deployment"></p>

### Requirements

 - an IDE such as GitPod or Visual Studio Code - I used GitPod
 - [PIP](https://pip.pypa.io/en/stable/installing/) to install packages in Python
 - [python 3](https://www.python.org/downloads/) programming language used on the back-end
 - [git](https://git-scm.com/) version control system for code source
 - [stripe](https://stripe.com/) create an account for online payments
 - [AWS](https://aws.amazon.com/) cloud storage service for online backup of website assets. (Create an S3 bucket)


### Local deployment
1. Save a copy of the github repository at https://github.com/bezebee/MS4.git by clicking the 'download.zip'
button at the top of the page and extracting the zip file, or you clone the repository with this command:
   ```
   $ git clone https://github.com/bezebee/MS4.git
   ```
1. Copy the repository into your IDE.
1. Install all required modules with the command:
   ```
   pip3 install -r requirements.txt
   ```

1. Store your environment variables and save them in the 'Environment Variables'-Settings in your IDE:

    ```bash
    'DEVELOPMENT', 'True'
    'SECRET_KEY', '<your value>'
    'STRIPE_PUBLIC_KEY', '<your value>'
    'STRIPE_SECRET_KEY', '<your value>'
    'STRIPE_WH_SECRET', '<your value>'
    ```
1. Replace <your value> with the values from your own accounts
    - The SECRET KEY: you can get from a free Django Secret Key Generator
    - STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY: from Developer's API on the Stripe dashboard
    - STRIPE_WH_SECRET: from Stripe's developer API after creating a webhook
     
1. Set up the local database by running these two commands:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
   
1. Create a superuser for the database, in order to access Django's admin-panel
    ```bash
    python3 manage.py createsuperuser
    ```

1. Start your server by running the following management command in your terminal:
    ```bash
    python3 manage.py runserver
    ```


### Deployment on Heroku

1. Go to https://heroku.com/ and create a new app with a unique name
1. Provision the Postgres database: Go to the Resources tab and install the addon "Heroku Postgres". Heroku automatically adds
the 'DATABASE_URL' to the Config Vars.
1. Go to the Settings tab, click Reveal Config Vars and copy the DATABASE_URL value into your local memory.
1. In your App on Heroku, go to the Settings tab, and click on 'Reveal Config Vars', set these variables:
    
    ```bash
    'AWS_ACCESS_KEY_ID', '<your value>'
    'AWS_SECRET_ACCESS_KEY', '<your value>'
    'DATABASE_URL', '<your value>'
    'SECRET_KEY', '<your value>'
    'STRIPE_PUBLIC_KEY', '<your value>'
    'STRIPE_SECRET_KEY', '<your value>'
    'STRIPE_WH_SECRET', '<your value>'
    'USE_AWS', 'True'
    ```

1. Migrate the database:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
1. Create a superuser for the database, to access Django's admin panel:
    ```
    python3 manage.py createsuperuser
    ```
1. If any packages have been updated, make a new requirements.txt file: 
    ```
    pip freeze > requirements.txt
    ```
1. Create a new file named Procfile with no file extension, add web: python app.py to the file and save
1. push files that were changed to Github:
    ```bash
   git add .
   git commit -m "..."
   git push
   ``` 
1. Go back to the Heroku, open your app and go to the Deploy tab. Choose a Deployment method, I deployed mine through GitHub.
1. By choosing Github as a deployment method, I had to enter your Github link and choose Automatic Deployments. This will enable every commit to push directly to Heroku.

<br><br><br>
<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/credits_n1yyeq.png" width="auto" height="70" alt="Credits"></p>

The inspiration for the website was mainly taken from the Coding Institute lectures presented by Chris Zielinski. 
Below are other resources I used while building the project:

1. [CSS3 Neumorphic Social Media Icons | Coding Nepal](https://www.youtube.com/watch?v=85tDF_h1Ci4&ab_channel=CodingNepal)
2. [Neumorphic design example - Codepen](https://codepen.io/Web_Cifar/pen/gObzrMR)
3. [Neumorphism and CSS](https://css-tricks.com/neumorphism-and-css/)
4. [Debug False not rendering static files locally - Solution from StackOverflow](https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail)


### The images of pins are used for Educational Purposes only. Products are available to purchase from these pages:

[Holly Pixels](https://hollypixelsstudio.com/collections/enamel-pins/Enamel-Pins) | [Mustard](https://www.justmustard.com/product/genius-clips/)
:-------------------------:|:-------------------------:
![](https://res.cloudinary.com/dugnokxox/image/upload/v1607500119/ms4%20images/tardigrade_ohz0rw.png)  |  ![](https://res.cloudinary.com/dugnokxox/image/upload/v1604944776/ms4%20images/download_14_uili5w.jpg)

### The gif animations are used for Educational Purposes only. 

[James Curran](https://dribbble.com/slimjimstudios) | [Marcus Magnusson](https://dribbble.com/MarkusM)
:-------------------------:|:-------------------------:
![](https://res.cloudinary.com/dugnokxox/image/upload/v1610291337/image_processing20200811-20221-10kgdnz_wuyupq.gif)  |  ![](https://res.cloudinary.com/dugnokxox/image/upload/v1610288563/kick_push_dribbble_ge9ciq.gif)


