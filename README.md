<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1604163817/ms4%20images/unicorn_ozbxlz.png" width="200" height="200" alt="Thank you for visiting my Readme"></p>

[![nicknacks on Heroku](https://img.shields.io/badge/Heroku-nicknacks-pink)](https://ms4nicknacks.herokuapp.com/)
[![Deployed preview](https://res.cloudinary.com/dugnokxox/image/upload/v1609882886/ms4%20images/nicknacks_eqitvq.png)](https://ms4nicknacks.herokuapp.com/)




## Intro


<p align="center">This task is essential for the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course. 
This project is an eCommerce shop front to host decorative pins, keychains and cute stationery. The name chosen for the website is nicknacks, which means in free translation "this and that". The name choice will allow administrator to expand on the produce offered.</p>

<p align="center">The site is worked within Django structure, sent live on Heroku, utilizes AWS S3 to have media and static records. Locally, it utilizes the inherent Django Db.sqlite3 information base, though when conveyed live it uses Heroku's Postgres information base. Authentication functionality is provided by Django's Allauth: administrator superuser can add and alter things in the Products and Categories applications, while visiting clients can enlist and login, accessing vestige depictions and their request history in the Checkout and Profile applications. A section has also been made available to the enlisted client, to add their own drawings, which can in due course be used as designs of their own. This is analysed furthermore in this readme, under the relevant heading.</p>




<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/user_experience_cpzk3c.png" width="auto" height="70" alt="UX"></p>

## Goals

<p align="center">The main goal of the nicknacks is to sell beautiful hand made accessories. Secondly, through that website people can order something they have designed and desire to have made into piece of accessory or piece of stationery</p>

## Target Audience

- Users aged 8 to 80
- Users interested in cute accessories and stationery
- Users with interest in accessory and stationery design and production for their own use

## Business Goals

- To create a platform that enables the prospect client to find and purchase the product they like
- To enable prospect user to submit their design and have it either just stored or even produced
- In order to increase the retention, encourage users to register
- Offer a presentable design of the website, with the use of neumorphic design, to increase aesthetic appeal
- Offer easy interaction on the page

## Customer goals

- Finding product that fits their taste
- Buy product through an easy payment flow
- Upload their own designs and store them in their registered account
- Place order for their designs, to have them produced
- See their previous purchases

## User Stories

### Viewing and Navigation		
- As a shopper I want to be able to View the list of products to purchase some
- As a shopper I want to be able to VIew individual product details to identify the price, description, rating, image and available sizes
- As a shopper I want to be able to Quickly identify deals, clearance items and special offers to take advantage of special savings on products I'd like to purchase
- As a shopper I want to be able to Easily view the total of my purchases at any time to avoid spending too much

### Registration and User Accounts  
- As a registered shopper I want to be able to Easily register for an account so I can have a personal account and be able to view my profile
- As a registered shopper I want to be able to Easily login or logout so I can access my personal account information
- As a registered shopper I want to be able to Easily recover my password in case I forget it so I can recover access to my account
- As a registered shopper I want to be able to Receive an email confirmation after registering so I can verify that my account registration was successful
- As a registered shopper I want to be able to Have a personalised user profile so I can view my personal order history and order confirmations and save my payment information
- As a registered shopper I want to be able to Add my own personalised design so I can view all my designs and choose which one I would like to order
- As a registered shopper I want to be able to Place an order for my personalised design so I can have my design made into pin, keyring or a piece of stationery
- As a registered shopper I want to be able to Easily contact the store owner with any queries I might have so I can ask any questions I may have

### Sorting and searching  
- As a shopper I want to be able to Sort the list of available products so I can easily identify the best rated, best priced and categorically sorted products
- As a shopper I want to be able to Sort a specific category of products so I can find best priced or best rated product in a specific category or sort the product in that category by name
- As a shopper I want to be able to Sort multiple categories of products simultaneously so I can find the best priced or best rated products across board categories, such as pins or keyrings
- As a shopper I want to be able to Search for a product by name or description so I can find a specific product I'd like to purchase
- As a shopper I want to be able to Easily see what I have searched for and the number of results so I can quickly decide whether the product I want is available
Purchasing and Checkout  
- As a registered shopper I want to be able to Easily select quantity of a product when purchasing it so I can ensure I am selecting correct product and a correct quantity
- As a registered shopper I want to be able to View items in my bag to be purchased so I can identify the total cost of my purchase and all items I will receive
- As a registered shopper I want to be able to Adjust the quantity of individual items in my bag so I can easily make changes to my purchase before checkout
- As a registered shopper I want to be able to Easily enter my payment information  so I can check out quickly and with no hassle
- As a registered shopper I want to be able to Feel that my personal and payment information is safe and secure so I can confidently provide the needed informatoin to make a purchase
- As a registered shopper I want to be able to View an order confirmation after checkout so I can verify that I have not made any mistakes
- As a registered shopper I want to be able to Receive an email confirmation after checking out so I can keep the records of my purchases

### Admin and Store Management  
- As a store owner Add a product as this would enable me to add new items to my store
- As a store owner Edit/Update product to apply any changes, be it in price, description, image or other product criteria
- As a store owner Delete a product Remove product if they are no longer for sale

## Design

The use of neumorphic design througout the page influenced a decision of one main color being used. The color used throughout the page is pale and light, almost white, as this ensures best effectivens of the design style.


<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609881480/ms4%20images/Screenshot_2021-01-05_at_21.17.21_nua89x.png" alt="Database Structure"></p>

Color used for the fonts is off black, which gives the page a soft finish. Black font can be a bit invasive and eye hurting.

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/database_structure_k2dbcm.png" width="auto" height="70" alt="Database Structure"></p>
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

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/technologies_mr6sj9.png" width="auto" height="70" alt="Technologies"></p>

[![Gitpod](https://img.shields.io/badge/IDE-Gitpod-blue)](https://www.gitpod.io/) Used as my primary IDE for coding<br>
[![Github](https://img.shields.io/badge/Remote%20code-Github-white)](https://github.com/) Remote storing of my code online<br>
[![Photoshop](https://img.shields.io/badge/Photoediting-Photoshop-lightblue)](https://www.adobe.com/ie/products/photoshop.html) to edit the images, main logo and readme chapter-headings<br>
[![Goodnotes](https://img.shields.io/badge/Wireframes-Goodnotes-Orange)](https://www.goodnotes.com/) to create Wireframes<br>
[![Pixlr.com](https://img.shields.io/badge/Image%20editing-Pixlr-blue)](https://pixlr.com/x/) used to edit the product images<br>
[![Cloudinary](https://img.shields.io/badge/Cloud%20image%20storing-Cloudinary-0F4E97)](https://cloudinary.com/) used to store my images<br>

[![HTML](https://img.shields.io/badge/Mark%20up%20text-HTML-yellow)](https://www.w3schools.com/html/html_intro.asp) base for markup text<br>
[![CSS](https://img.shields.io/badge/Styling-CSS-blueviolet)](https://www.w3schools.com/css/) base for cascading styles<br>
[![JavaScript](https://img.shields.io/badge/JS%20Functionality-JS-darkgreen)](https://jquery.com/) used as the JS functionality<br>
[![Bootstrap](https://img.shields.io/badge/Design%20Framework-Bootstrap-%23F5A4A7)](https://getbootstrap.com/) used as the overall design framework<br>
[![Django](https://img.shields.io/badge/Microframework-Django-%238B0000)](https://www.djangoproject.com/) used as a microframework<br>
[![Shields](https://img.shields.io/badge/Readme%20Badges-Shields-lightgrey)](https://shields.io/) to create a badge<br>
[![Heroku](https://img.shields.io/badge/App%20Hosting-Heroku-%237B68EE)](https://www.heroku.com/home) used for app hosting<br>
[![Python](https://img.shields.io/badge/Back%20end%20programming-Python-%09%23008000)](https://www.python.org/)to handle backend functions<br>

[![SQlite3](https://img.shields.io/badge/Wireframes-SQlite3-Orange)](https://www.sqlite.org) The database used in development environment<br>
[![Postgres](https://img.shields.io/badge/Image%20editing-Postgres-blue)](https://www.postgresql.org/) Database used in productions<br>
[![AWS Services](https://img.shields.io/badge/AWS%20-Services-orange)](https://aws.amazon.com/) s3 is used to store the static and media files of the site<br>

--------------

[![W3C HTML Validator](https://img.shields.io/badge/HTML%20Validator-W3C%20HTML%20Validator-red)](https://validator.w3.org/) to validate HTML<br>
[![W3C CSS Validator](https://img.shields.io/badge/CSS%20Validator-W3C%20CSS%20Validator-darkred)](https://jigsaw.w3.org/css-validator/) to validate CSS code<br>
[![Pep8 Online](https://img.shields.io/badge/Python%20Validator-PEP8%20online-white)](http://pep8online.com/) to validate Python code<br>
[![JShint](https://img.shields.io/badge/JS%2FjQuery%20Validator-JSHint-%23008e94)](https://jshint.com/) to validate JavaScript/jQuery<br>


<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/testing_ioxxts.png" width="auto" height="70" alt="Testing"></p>

|  Feature |  Action | Effect |
|---|---|---|
| Logo (upper left corner)  |  Hover over (little had is not appearing!) |  The address on hover is showing as home page |
| Search bar  |  Entered "Space", |<ul><li> one product is listed under this name - correct</li><li>The summary shows message "1 Products found for 'space'" (See if this can be amended to dependable if it's one or many, with or without s"</li>|
|   |   |   |


<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/deployment_o0onfb.png" width="auto" height="70" alt="Deployment"></p>
<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1609938201/ms4%20images/credits_n1yyeq.png" width="auto" height="70" alt="Credits"></p>

<p align="center"><img src="https://res.cloudinary.com/dugnokxox/image/upload/v1606579543/20786350-B46F-40B3-86F3-4D97002D9FB6_xizcyw.png" width="auto" height="170" alt="Copyright"></p>
 
