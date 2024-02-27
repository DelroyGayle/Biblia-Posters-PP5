# Biblia Posters
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/19dca679-1308-464b-9ddd-ec8575c1c3d5)

[View live website](https://biblia-posters-dg-869e3a15ddae.herokuapp.com/)

## Table of Contents

1. [Introduction](#introduction)
2. [User Stories](#user-stories)
3. [UX-User Experience](#ux-user-experience)
   1. [Wireframes](#wireframes)
   2. [Agile Design](#agile-design)
   3. [Database Design](#database-design)
   4. [Data Models](#data-models)
   5. [Framework](#framework)
   6. [Colours](#colours)
   7. [Typography](#typography)
4. [Features](#features)
   1. ONE
   2. [Background Image](#background-image)
   3. [NavBar](#navbar)
   4. [Home Page](#home-page)
   5. CRUD TODO
   9. [Validation and Messages](#validation-and-messages)
   10. [Registration](#registration)
   11. [Login/Logout](#loginlogout)
   12. [Facebook Business Page](#facebook-business-page)     
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Libraries and Frameworks](#libraries-and-frameworks)
6. [Future Features](#future-features)
7. [Testing](#testing)
    1. [Please Go To TESTING.md](https://github.com/DelroyGayle/Biblia-Posters-PP5/blob/main/TESTING.md)
8. [Bugs](#bugs)
     1. [Solved Bugs](#solved-bugs)
     2. [Known Bugs](#known-bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Introduction

For my Code Institute Portfolio Project 5, 
I would like to implement an E-Commerce online store in order for shoppers to purchase Biblical and Christian posters.
This project is built from the perspective of a small business owner who wants a website to attract customers to the owner's collection of posters which depict different events shown in the Bible.
The owner will also operate as the Admin Site User so that the user can perform CRUD functions relating to posters, special days dates and shoppers' reviews. 
The website will operate as a Business to Consumer (B2C) E-Commerce site, allowing the selling of posters from the business, namely **Biblia Posters**, to individual consumers.
To meet this B2C requirement:
- the site will display a range of posters for customers to purchase
- the site will have the necessary functionality to allow users to purchase the posters online
- the site will allow users to subscribe to an email newsletter
- the site will allow a user to set up their own profile to facilitate future purchases
- the site will allow registered users to add posters to their own wish list for future purchases
- the site will allow registered users to share reviews about their purchases and interactions with Biblia Poster
- depending on particular times of the year which depict special Biblical significance, the site will offer users 25% discounts on purchases

For marketing strategy,
* I have set up a [Facebook Business Page](https://www.facebook.com/profile.php?id=61556537234433) in order to promote **Biblia Posters** to a wider audience.
* I have set up a Newsletter Subscription option in order to promote special offers and events to customers.

<details>
<summary>Biblia Posters Facebook Business Page</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c5c2ac5d-25e9-4f40-8c80-e6a72908292b)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ae963088-0eb7-4ed5-8ec0-ae777270aefb)
	
 	
</details>

----

## User Stories
<details>
<summary>The User Stories that were implemented for this Project</summary
									
* As a **Shopper** I can **view a list of posters** so that **I can select posters to purchase**
* As a **Shopper** I can **view a specific category of posters** so that **I can select specific posters without the need to search throughout all the posters**
* As a **Shopper** I can **view a poster's individual details** so that **I can identify the price, description, rating, image and reviews regarding the poster**
* As a **Shopper** I can **view the total of my purchases** so that **I can check whether I am spending within my budget**
* As a **Shopper** I can **sort the list of available posters** so that **I can quickly see the best rated and best priced posters**
* As a **Shopper** I can **sort a specific category of poster** so that **I can quickly see the best rated and best priced poster in a particular named category**
* As a **Shopper** I can **search for a poster by name or description** so that **I can find a specific poster that I would like to purchase**
* As a **Shopper** I can **add items to the virtual shopping basket** so that **I can thereby purchase items online**
* As a **Shopper** I can **view items in the virtual shopping bag** so that **I can identify all the items selected and the total cost of my purchase**
* As a **Shopper** I can **adjust the quantity of individual items in the virtual shopping bag** so that **I can make any changes to my purchase before checkout**
* As a **Shopper** I can **easily enter the payment information** so that **I can check out speedily without any difficulty**
* As a **Shopper** I can **make purchases using a industry-standard secure method** so that **I can have confidence that my purchases are safe**
* As a **Shopper** I can **receive email confirmation of my order after checkout** so that **I can have a record of all my purchases for verification and audit purposes**
* As a **Shopper** I can **subscribe to an email newsletter** so that **I can receive updates of special offers and new deals**
* As a **Shopper** I can **access a link to the Facebook business page** so that **I can inquire further information regarding this online shop**
* As a **Site User** I can **register for an account** so that **I can have a personal account for profile, reviews and wishlist purposes**
* As a **Site User** I can **receive email confirmation after registering** so that **I can verify that my account registration was successful**
* As a **Site User** I can **login or logout** so that **I can access my personal account information**
* As a **Site User** I can **have a personalised user profile** so that **I can save my address/delivery details and see my personal order history**
* As a **Site User** I can **add a review regarding a poster that I have personally purchased** so that **I can inform potential customers of my views regarding the poster as well as any related customer service**
* As a **Site User** I can **edit reviews that I have posted** so that **I can change, remove or add further details regarding the poster that I had purchased**
* As a **Site User** I can **delete reviews that I have posted** so that **I can remove the review that I had previously made**
* As a **Site User** I can **add posters to a wish list** so that **I can view any previously selected posters that I would like to purchase on a later occasion**
* As a **Site User** I can **delete items from my wish list** so that **I can remove the poster that no longer needs to be on my wish list**
* As an **Admin Site User** I can **add a poster** so that **I can add new posters to my store**
* As an **Admin Site User** I can **edit a poster** so that **I can change the price, description, image and other poster criteria**
* As an **Admin Site User** I can **delete a poster** so that **I can remove posters that are no longer for sale**

</details>
------

## UX-User Experience

### Wireframes

<details>
<summary>Home Page</summary>
<br/><br/>  

![Screenshot 2024-01-29 120059](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fdc9b8d4-88be-4302-a559-d3deb80171ab)

</details>

<details>
<summary>Posters Page - Showing the range of posters</summary>
<br/><br/>  

![Screenshot 2024-01-29 115538](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/27fe99f0-cadf-440f-b67d-77c015c44662)


</details>


------

### Agile Design
**Agile** was used as the management approach of this project. I used Github's tools namely *Milestones, Issues and Projects* resulting in the project into twenty-seven weighted user stores dividing them up into the following categories as described by the [MoSCoW prioritisation technique](https://en.wikipedia.org/wiki/MoSCoW_method)].
* ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/da0e9b7b-1a08-4519-bc96-3b6f4e7dfdbc)

* ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7501b331-f0c6-4a76-8e7f-9fa7ab4e7bf9)

* ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ceed0497-29f6-4c32-bd04-2cf39a51f34e)


Continuing with Agile methodology, I then categorised the user stories into *Epics*; that is, a collection of user stories linked with various *tasks* to implement a particular feature.

The Kanban Project layout showing the *Twenty-seven User Stories* can be viewed [here](https://github.com/users/DelroyGayle/projects/6)

<details>
<summary>Here is the Agile Kanban Board of the Twenty-Seven User Stories that were implemented</summary>

![Screenshot 2024-01-28 182649](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/85b48241-d116-4baf-91dc-d6fb1bf4f2de)

![Screenshot 2024-01-28 182711](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d01790f5-1c31-42a8-b350-0c682e6c9cde)

![Screenshot 2024-01-28 182728](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/1da699a5-aff9-4d2f-8143-3bc0e6dc3d97)

![Screenshot 2024-01-28 182755](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b04b9349-cfd6-452e-9763-461c2d8f0064)

![Screenshot 2024-01-28 182804](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/be982fff-fac9-4b0d-b953-9bf30b1d7129)


</details>

Epics, User Stories and their related Tasks are further explained in [TESTING.md](https://github.com/DelroyGayle/Biblia-Posters-PP5/blob/main/TESTING.md)

### Data Models

Data modelling
As mentioned at the beginning, Python code is used with the Django framework to generate the tables in the provisioned database. This project uses a Postgres database, hosted on ElephantSQL.




This website uses the Django framework to generated the models used for the database. The SQL database is thereby hosted on  [ElephantSQL PostgreSQL](https://www.elephantsql.com/). 

This project and its models closely follow Code Institute's Boutique Ado Walkthrough, so there are many similarities.
For example, instead of a model depecting clothing and household goods, the walkthrough's example model is now used to depict posters.

**Custom models**

The *custom* models that I designed are 
1. UserPurchasedPosters
2. Reviews
3. Wishlist
4. Special-days
   
<details>
<summary>Database Schema Diagram</summary>
<br/><br/>  

TODO


</details>

----

### Data Models

The following data models were designed to represent the database usage for this project

#### User Model

The User Model contains information about the user. It is based upon Django's in-built authentication system
- username
- email
- password

#### Model


#### Model


   
   
#### Model/1

####  Model/2

####  Model/3

### Framework

### Colours

* Foreground Colours: Bootstrap 4 colours of *text-danger*, black and white.
* Background Colours: For the homepage I used *#e0fff5*.
* For all the other pages, the background colour is *#adffe4*.
  
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/925a09d7-f8c1-45d3-a671-0f3ce897c3e2)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/cd410b7e-35c6-4f8b-9ef0-f305af9346cf)








### Typography

The fonts I have chosen to use are 
1. [Montserrat](https://fonts.google.com/specimen/Montserrat) - I like the clarity of this particular font.
2. [Pacifico](https://fonts.google.com/specimen/Pacifico) - I like the boldness of this particular font.

### Imagery

The source for my images are the following Stock image sites:


1. [Unspash](https://unsplash.com)<br>
   The *Hero Image* by [Aaron Burden](https://unsplash.com/@aaronburden?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) is a photo of an *Opened Bible on a path during the daytime*.<br>
This informs the site user that this website has a biblical theme with a view of drawing the user to follow the path to find out more about what this website has to offer.

2. [Pexels](https://www.pexels.com)<br>
  The next photo on the *Home Page* is of a man showing a poster with the inscription<br> *Who says a small poster can't start a big collection?* by [Anete Lusina](https://www.pexels.com/@anete-lusina/).<br>
This informs the site that this website's purpose is in regards to posters.

3. [Free Bible Images](https://www.freebibleimages.org/)<br>
   I used this website as the source of the images of the fifty-two posters and the three images <br>depicting *Passover, Pentecost and the Feast of Booths* on the *Home Page*.


## Features

### Homepage

#### Navigation

**Desktop navigation bar and hero image**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/652879f8-d413-40f7-ad23-43eb6a5ce94a)

The homepage opens up with the mission statement ***Proclaiming the message of the Bible one poster at a time***
<br><br>
The navigation bar shows the *BIBLIA* **POSTERS** Logo which acts as a *Home Button*. By clicking this logo, the user is returned to the Home Page.<br>The rest of the bar are links to:
* All available Posters for sale which are further divided into
* Posters sorted by Pricing
* Posters sorted by Rating
* Posters sorted by Category
* Show All available Posters
* * All available Old Testament Posters and their Categories
* * All available New Testament Posters and their Categories

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/1733db73-0941-41ce-8ae4-c97f2e5143a9)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d314399a-602f-4a9f-ad63-df424f34cd5d)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/dfb198b5-3d7f-4cc9-ad62-272b67d1a695)

On the right hand side of the navigation bar is a dropdown menu for:
*Unregistered* users, with the options
* To register
* To Login

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/47b0d5e9-a5c9-4bd7-9922-84ae7e9d4d16)

For *Registered users* with the options
* To see the user's personal profile
* See the user's wishlist
* See a list of all the reviews that the user has authored
* To Logout

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/1b63e0fe-a930-48ae-8c29-bb06e25f52a9)

In addition, the **Site Admin** user has the option to *add, edit and delete posters* via the Poster Management option i.e. CRUD functionality

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/aaee7834-29a1-4225-b0be-a9cff4cca5fd)


What follows next on the Navigation Bar is the link to the *live* virtual Shopping Bag showing its current total value

<br>In the middle of the Navigation Bar is the Search Bar whereby the user can perform (*case insensitive*) searches for Posters by title or description.

**Banner and Shop Now**

Beneath the Navigation Bar is a Banner showing Today's Date
The Banner is also used to indicate when a **Special Days** Promotion (see below) is active giving the user 25% Discount on purchases of all posters.

Please note: *21st February 2024* is **not the actual date** for Passover, Pentecost nor the Feast of Booths. These depictions of the banner are shown here for demo purposes only; indicating that the banner will change colour from black to green whereby the particular *event* is displayed alongside the offer of 25% Discount. Because of the submission date of this project, February dates were used for the sake of documentation. See ###TODO for further details.

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/caa6eaa3-5775-45d6-b6a7-c1dbef9d48d0)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/79989e3c-c76f-4d11-b74d-a9e2682f0943)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b82b5ae7-b3d7-43f6-b8bc-9e0de6090e4e)

Lastly, on the Hero Image is the **Shop Now** whereby the user is directed to the **All Posters** page to all available posters for sale.

**Mobile navigation bar and hero image**

For the mobile view, the same information is displayed as described above however the menu becomes a hamburger menu.

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7f5d242a-c315-4ffb-b8c6-577b45a937e8)


![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c2941752-8f5e-4336-9fa5-16364ddb03c2)

<br><small>(Again, 21st February, 2024 is **not** the date of the Feast of Booths - demo purposes only)</small>

#### About Us

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c05f3896-3e15-44aa-b97a-c13ee85748e0)

A description is given of the type of posters that this online store has to offer. It also points out the advantages of registering on to the site.

#### Special Days

The [USP](https://en.wikipedia.org/wiki/Unique_selling_proposition) of this online store is to offer 25% Discount currently three times a year. Namely, on the occasion of Passover, Pentecost and the Feast of Booths. The *Special Days* section of the homepage gives a summary of these three occasions which are of significant Biblical importance.

According to [Chabad.org](https://www.chabad.org/holidays/JewishNewYear/template_cdo/aid/671894/jewish/When-Is-Sukkot-in-2024-2025-2026-2027-and-2028.htm) the dates of these days for 2024 to 2027 are as follows:

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/80753a4f-278d-4c96-bece-b6ef9ce8e66a)

<details>

<summary>Admin view of the Special Days database</summary>	
 
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/984d3715-f5f7-40ee-a7bd-50b2d05f4b59)

| Special Days ID | Name        | 
| ------------- | ------------- | 
| 0 | Passover | 
| 1 | Pentecost | 
| 2 | Feast of Booths | 

</details>


I have chosen to ignore that the events *begin/end at sundown/nightfall* and chosen *midnight* instead.<br>
In addition, I have given for the sake of *late shoppers* a tolerance of 30 minutes each way.<br>That is, for Passover, 2024;  :-
* For a user who visits the website and begins shopping *sometime just before Passover*, the promotion will start in actuality, at *11:30pm 21st April, 2024*
* For a user who visits the website and begins shopping *sometime just before the end of Passover*, the promotion will end in actuality, at **12:30am 1st May, 2024*

The Django Queryset used to query the *special-days* database has been set up, that for each range:
*  subtract **30 minutes** from midnight of the *FIRSTDAY*
*  add **24 hours 30 minutes** to midnight of the *LASTDAY*
*  Then check if the current date and time is between any of the ranges
*  If True, change banner to green and display 25% Discount offer - the *Special Days ID* indicates which title to display
*  If False, display black banner - no discount offered

Because of the submission date of this project, February dates were shown above for the sake of documentation.
However, anyone visiting *the live site during the true dates as shown above*, will see the banners and discounts in action!

#### Newsletter

<details>
	<summary>Desktop and Mobile view of Newsletter option</summary>

 ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/968adabb-8852-47d4-b3c6-a758d1ca371d)

 ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6b7c3336-3e3c-4e61-8128-5010b404d138)


</details>

As part of the marketing strategy, what follows on the homepage is the option to subscribe to **Biblia Posters' Newsletter** using [Mailchimp](https://mailchimp.com/)

#### Footer

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/dba0cd78-8062-45aa-b336-0f386219ab6b)


The footer 
* explains some advantages to customers
* Customer Service contact details
* has a link to the Privacy Policy page
* Regards Social Media, 
* * There is a Link for the Facebook Business Page](https://www.facebook.com/profile.php?id=61556537234433)
  * There is a Link for Twitter
  * There is a Link for the related WordPress blog, namely, [AgeToCome](https://agetocome.wordpress.com/)

Then a note explaining that all the poster images used *are in actuality, **Free!*** <br>Moreover, there are available from [Free Bible Images](https://www.freebibleimages.org/)




features a tagline, social contact CTAs and a 'copyright' mark. In mobile view, these three components are stacked.
### HEADING

#### Create Posters

#### Edit Posters

  
<details>

<summary>Sample of a poster image: The_Resurrected_Jesus_Shows_His_Disciples_His_Pierced_Hands_And_Feet.jpg</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6af9e35d-45e1-403a-a26e-9ac9ca2d3688)

</details>


<details>
   <summary>Navigation Bar</summary>

   IMAGE


</details>

### Toast Messages 

Feedback is delivered at all times to the user via the usage of Bootstrap Toast Messages. *Success* and *Alert/Info* indicators are displayed for *six seconds* before disappearing whilst *Error Message* indicators are displayed for *ten seconds* before disappearing.<br>These messages are always  Login status is always shown in the right hand corner of the screen just below the navigation bar.

<details>
	<summary>Sample of Messages shown</summary>

 Signed In

 Signed Out

 ### Registration and Authentication

 The [django-allauth](https://docs.allauth.org/en/latest/) is used to cater for registration, login, logout and lost passwords.<br>
 The user has to select a unique username, email and password which must be confirmed via a link generated by *allauth*. Once confirmed, the user can thereby login to the website in order to 
 1. set up a profile
 2. Add/Remove posters from a wishlist
 3. Write reviews regarding posters that the user has purchased - hence, **verified** purchasers only can add reviews.

Registration/TODO


 
</details>


### View Posters


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T06 | View All Available **Old Testament** Posters | Select from Menu, Old Testament then select **ALL O.T. Posters**  | All available OT posters are to be shown | PASS |


<details>

<summary>Menu & Display</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fb28fafb-b018-42a3-8ee6-26bf023e50d7)

<summary>All the Old Testament Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/2f6bc6e8-d2dd-434e-96f7-d8bfebd738c6)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e20803a6-0c31-4679-b240-0573579802ac)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/eeb105d4-1521-4b8a-a577-ae254ae8c7e0)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T07 | View All Available **New Testament** Posters | Select from Menu, New Testament then select **ALL N.T. Posters**  | All available NT posters are to be shown | PASS |

<details>

<summary>Menu & Display</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/36b91986-bf54-434e-b8a9-11e7f2bf1926)


<summary>All the New Testament Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a5f6c916-a501-488b-9522-cd8fef3cdb39)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/262df841-30cd-43c1-8379-fd958a51ea74)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7d0b2762-b03b-44f6-bfbe-5d03fa80e438)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f31eba18-bfe0-4eb7-ae98-a49e4c251a54)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7c2f09e3-bca3-4d63-a884-2adfce760a62)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T08 | View All **Genesis** Posters | Select from Menu, Old Testament then select **Genesis**  | All available Genesis posters are to be shown | PASS |

<details>

<summary>Display of Genesis Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5d86495b-8305-4ad7-9db1-d54acb15bccf)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T09 | View All **Exodus** Posters | Select from Menu, Old Testament then select **Exodus**  | All available Exodus posters are to be shown | PASS |

<details>

<summary>Display of Exodus Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b03189ae-150c-4b7e-b982-67369f499236)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T10 | View All **Numbers** Posters | Select from Menu, Old Testament then select **Numbers**  | All available Numbers posters are to be shown | PASS |

<details>

<summary>Display of Numbers Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5f43584a-b9cf-4212-8457-667f979b6fd4)


</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T11 | View All **Joshua** Posters | Select from Menu, Old Testament then select **Joshua**  | All available Joshua posters are to be shown | PASS |

<details>

<summary>Display of Joshua Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d125a5dd-2da9-48c8-8d85-0bca33ef07fc)


</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T12 | View All **Jesus** Posters | Select from Menu, New Testament then select **Jesus**  | All available Jesus posters are to be shown | PASS |

<details>

<summary>Display of Jesus Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a5f6c916-a501-488b-9522-cd8fef3cdb39)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/262df841-30cd-43c1-8379-fd958a51ea74)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7d0b2762-b03b-44f6-bfbe-5d03fa80e438)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f31eba18-bfe0-4eb7-ae98-a49e4c251a54)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T13 | View All **The Apostles** Posters | Select from Menu, Old Testament then select **Apostles**  | All available Apostles posters are to be shown | PASS |

<details>

<summary>Display of The Apostles Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b9065ab6-2860-46ce-b867-3b4b0120d6f5)

</details>

### View Posters Details


<details>

<summary>View Poster Details - Desktop</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/627c0551-ee23-476c-b8c7-4db0f611747b)

</details>

<details>

<summary>View Poster Details - Mobile</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d466b50b-0db2-44b4-bce5-1d69dccba24d)

</details>

### Search for Posters

<details>
<summary>/posters/?query=saul</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/0646712d-33e8-491a-9ecc-ef74159f91a9)
  
</details>

<details>
<summary>/posters/?query=ethio</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/3bda67f6-038b-4116-8f18-4ed186f1b205)
  
</details>
*/posters/?query=BED* matched 5 posters 

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/4da87e73-00f3-477f-9994-895a5e3e8285)

<details>

<summary>What follows are 2 posters where the match was in the descriptions</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fcca6530-f744-4103-832a-c2c1fcaef91a)

View the description then *used CTRL-F and 'bed' to highlight that the searches were successful*

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5e59d029-1f07-484e-896f-83f2591af1dc)
 
</details>

<details>
<summary>Null Entry in Searchbar</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e8160d1b-ba71-44c3-aa54-f54fcffbca2f)
  
</details>

<details>
<summary>/posters/?query=HELLO</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b93c8664-ba08-439a-a9b7-b392a15dc771)
  
</details>

### Menus

#### Desktop
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/bb4703d0-5a32-4ab0-a2c7-e38ec6a60dfa)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ee394855-3c50-4063-8f2c-5ad980775a2e)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/645d144f-7761-44d6-922f-fc91df115687)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/dc754798-19a2-4616-954d-3e5885174fa3)

#### Mobile

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/da618cdc-4a84-4029-a2e6-501da9de07c6)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/3621eacb-19f9-4b28-a762-9879dc0f90e8)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f5563f82-9402-4d22-b177-bafff950706e)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/bee3c71d-d1d5-42fe-825a-7719cf35d276)




### Categorisation

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/75d40fa7-1616-49cf-9113-66f37f20caea)

#### Demonstration of Each Method

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T14 | Sort Posters **By Price**, *Ascending Order* | Select from Menu, All Posters then select **By Price**  | Posters shown, cheapest at the top, lowest at the bottom - URL */posters/?sort=price&direction=asc* | PASS |

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T15 | Sort Posters **By Price**, *Ascending Order* - Method 2 | From the Sort Selector, select **Price (low to high)**  | Posters shown, cheapest at the top, lowest at the bottom - URL */posters/?sort=price&direction=asc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/8e40bde7-608d-43e7-82c1-8f500df8b8b1)

<details>

<summary>Price in ascending order</summary>

Cheapest at the top

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/34cf62ea-5c37-4215-83a1-4df720f4a1f1)

Most expensive at the bottom

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/9dedb441-2e98-4664-9c6c-a3a7cc9c9a65)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T16 | Sort Posters **By Price**, *Descending Order* | From the Sort Selector, select **Price (high to low)**  | Posters shown, most expensive at top, cheapest at the bottom - URL */posters/?sort=price&direction=desc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/3b8410dc-7de8-46dc-a270-b7c50bfdcc2d)

<details>

<summary>Price in descending order</summary>

Most expensive at the top

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7b62e745-6247-43e7-9cd3-2f081948964a)

Cheapest at the bottom

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/41bf0347-ff8d-4225-85e8-b478a6515b1b)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T17 | Sort Posters **By Rating**, *Descending Order* | Select from Menu, All Posters then select **By Rating** | Posters shown, highest rate at the top, lowest rating at the bottom - URL */?sort=rating&direction=desc* | PASS |

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T18 | Sort Posters **By Rating**, *Descending Order* - Method 2 | From the Sort Selector, select **Rating (high to low)** | Posters shown, highest rate at the top, lowest rating at the bottom - URL */?sort=rating&direction=desc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ff3b83b8-8320-4527-ab85-063c40ba69c6)

<details>

<summary>Rating in descending order</summary>

Highest ratings at the top

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/109db7e9-3c41-4267-95bb-36518f824e9d)

Lowest ratings at the bottom

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/243b55c9-347e-4769-a05c-780041731fc4)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T19 | Sort Posters **By Rating**, *Ascending Order* | From the Sort Selector, select **Rating (low to high)** | Posters shown, lowest rating at the top, highest rating at the bottom - URL *?sort=rating&direction=asc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/bb10ad19-74e9-4022-9ec3-50c23de23218)

<details>

<summary>Rating in ascending order</summary>

Lowest ratings at the top

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e95ee491-62f7-4ef5-8775-4f8ba2411ac6)

Highest ratings at the bottom

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/097d785c-489c-4a40-8c27-ec1e661f5b12)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T20 | Sort Posters **By Category**, *A-Z* | Select from Menu, All Posters then select **By Category**  | Posters shown in Alphabetical Order of Category - URL */posters/?sort=category&direction=asc* | PASS |

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T21 | Sort Posters **By Category**, *A-Z* - Method 2 | From the Sort Selector, select **Category (A-Z)**  | Posters shown in Alphabetical Order of Category - URL */posters/?sort=category&direction=asc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ac51d05d-e79b-4a35-945e-e3a8c8653577)

<details>

<summary>Category in Alphabetical Order i.e. Apostles, ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6bb76e41-4c54-40dc-90ae-dd31448562d0)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T22 | Sort Posters **By Category**, *Z-A* | From the Sort Selector, select **Category (Z-A)**  | Posters shown in Descending Alphabetical Order of Category - URL */posters/?sort=category&direction=desc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/952f6bbc-95cd-428d-b230-f47883b1fec9)

<details>

<summary>Category in Descending Alphabetical Order i.e. Numbers then Joshua ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ccbbfa40-f228-424b-bb74-f33f45a1e31a)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T23 | Sort Posters with **All Posters**| Select from Menu, All Posters then select **All Posters**  | All **52** Posters shown - Default view - URL */posters/* | PASS |

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T24 | Sort Posters with **All Posters** - Method 2 | From the Sort Selector, select **Sort by...**  | All **52** Posters shown - Default view - URL */posters/* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/911f4bfa-feeb-4398-9356-a88ea1d278e2)

<details>

<summary>All 52 Posters - Default View</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/627c0551-ee23-476c-b8c7-4db0f611747b)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T25 | Sort Posters **By Name**, *A-Z* | From the Sort Selector, select **Name (A-Z)**  | Posters shown in Alphabetical Order of Poster Name - URL */posters/?sort=name&direction=asc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fdcab32a-27a0-4287-8d12-b8fb3ad0b276)

<details>

<summary>Name in Alphabetical Order i.e. Abraham, ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/51d1847d-71ed-4b95-8fab-0f9e954ab72d)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T26 | Sort Posters **By Name**, *Z-A* | From the Sort Selector, select **Name (Z-A)**  | Posters shown in Descending Alphabetical Order of Poster Name - URL */posters/?sort=Name&direction=desc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ecc78c53-de13-4ff9-b761-2c53ead26c7f)

<details>

<summary>Name in Descending Alphabetical Order i.e. Zacchaeus then Timbrels ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/54d39419-0ffa-4b9e-994f-69305e5103d1)

</details>



### Home Page

### Create ...


#### Create ...


### Search ...

Note: the Search option is *case-insensitive* <br>
Once the user has searched for the relevant poster, the user then has to click *View* to see the poster


### View Posters

### Edit Posters

### Delete Posters


### Validation and Messages



------

### Registration

* In order for a user to be able to create, read, edit and delete TODO, the user will need to register on the site.
* Registration is based upon Django's built-in authentication system.
* When the user registers the user will get a success message to confirm.

### Login/Logout

* In order for a user to be able to create, read, edit and delete TODO, the user will need to <br/>log into the App using their username and password.
* Login/Logout is based upon Django's built-in authentication system.
* When the user logs in, the Home Page will appear to the user.
* When the user logs out, the user will get a success message to confirm.
* 
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/4e061c55-04bc-4ea5-a64f-8c2288a55dfc)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7b4b1f8c-8cee-4f1e-9c0d-ed3001947436)

## Technologies Used

### Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  
### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)   
    * Django was used as the web framework.
* [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [ElephantSQL PostgreSQL](https://www.elephantsql.com/)
    * ElephantSQL was used for hosting the SQL Database
* [Cloudinary](https://cloudinary.com/)
    * Cloudinary was used for image management.

#### Other tools and frameworks

* [GitHub](https://github.com/) for hosting the site
* [Gitpod](https://www.gitpod.io/) for editing the files
* TODO
* [Heroku](https://heroku.com) for the deployment of the site
* [Jquery](https://jquery.com/) for scripting purposes
* [Miro](https://miro.com/) was used to create the wireframes
* [Django Extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html) was used to draw the Django models
* [Am I Responsive](http://ami.responsivedesign.is/) was used for creating the multi-device mock-up shown at the top of this README.md file
* [Favicon](https://favicon.io/) was used to generate the Favicon
* [Mailchimp](https://mailchimp.com/) was used for the Newsletter
* [Privacy Policy Generator](https://www.privacypolicygenerator.info/) was used to produce the Privacy Policy
* [Code Institute's GitHub full template](https://github.com/Code-Institute-Org/python-essentials-template) in order to run Django and Python on Heroku/Render
TODO REQ
#### requirements.txt

```
asgiref==3.7.2
boto3==1.34.21
botocore==1.34.21
dj-database-url==0.5.0
Django==3.2.23
django-allauth==0.41.0
django-countries==7.2.1
django-crispy-forms==1.14.0
django-storages==1.14.2
gunicorn==21.2.0
jmespath==1.0.1
oauthlib==3.2.2
Pillow==10.1.0
psycopg2==2.9.9
PyJWT==2.8.0
python3-openid==3.2.0
pytz==2023.3.post1
requests-oauthlib==1.3.1
s3transfer==0.10.0
sqlparse==0.4.4
stripe==7.10.0
urllib3==1.26.15
```
------

## Future Features

## Testing

Please refer to [TESTING.md](https://github.com/DelroyGayle/Biblia-Posters-PP5/blob/main/TESTING.md)

## Code Validation

------

## Bugs

### Solved Bugs

### Known Bugs

------

## Deployment
TODO
The project is deployed on Render.<br> 
All credit goes to Sophia Iroegbu and her tutorial [How to Deploy a Django App on Render](https://www.freecodecamp.org/news/deploying-a-django-app-to-render/) which worked flawlessly.<br><br>
These are the steps in order to deploy on Render:
1. Regarding your project - ensure you have PostgreSQL Database setup - for my project, [ElephantSQL Postgres](https://www.elephantsql.com/) was used
     + However alternatively there is an option to create a PostgreSQL database within Render
2. Create a Render account - either via Github itself or use your own email address
   - Either way, you will need to use your email address to confirm registration with Render
3. Once you have signed up, then proceed to Set Up a PostgreSQL Database if no setup already exists <br>- *skip Steps 3,5,6 if you already have a Database setup*
   - go to the Render dashboard and Click the **New +** button, hover over **PostgreSQL**, and click it
   - Next, define your database settings by giving your *database instance* a unique name
   - For **Region**, use **Frankfurt (EU Central)** if you are based in Europe
   - Select the free tier and click on **Create Database**
   - Once the status on your database shows **Available**, it means the database has been successfully created and is ready to use
   - Scroll down this page to see your database settings. You will need the **External Database URL**
4. Once the database is set up, you need to connect it to your Django project
   - Install dj-database-url by running the command
   - **pip install dj-database-url**
5. If you created your Postgres Database setup within Render, <br>then head over to your database settings on Render and copy the **External Database URL**
6. Copy this into your **env.py** i.e. **os.environ["DATABASE_URL"]="postgres:// ..."**
- Note: There is no need to do this step, if **os.environ["DATABASE_URL"]** already contains the URL of a previous, working database
7. Ensure that in your *settings.py* under your sitename the following settings are at the top of the file:
  ```
  import dj-database-url
  import os

  DATABASES = {
	"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
   ```
8. Confirm everything is installed correctly by running **pip3 install -r requirements.txt**
9. Next, migrate your tables to your new database to ensure the connection was successful
   - **python manage.py makemigrations**
   - **python manage.py migrate**
10. Create a folder in the root directory called **staticfiles**
11. Populate this folder by running **python manage.py collectstatic --noinput**
12. Push your codebase to your Git repo
13. Head over to your Render dashboard. Click **New +** and **Select Web web-service-name**
14. Connect your GitHub if you haven't already
    - This is done by: **Search** for the repo you want to deploy and click the **Connect** button
15. Give your **web web-service-name** a name and ensure you are connecting to the right branch
   - Use the same **Region** as used earlier
   - Build command should be: **pip install -r requirements.txt**
   - Start command should be: **gunicorn \<sitename\>.wsgi**
   - (Note: this would be the same entry that follows the word **web:** in a Heroku Procfile; although a Procfile is **not** needed by Render)
   - Select the free tier and click on **Create Web Service**
16. Copy the **\<web-service-name\>.com** name that was chosen - that is, *No https://, No URL* - simply **\<web-service-name\>.com**
   - Enter that into ALLOWED_HOSTS
   - The entry should be:
   - ```
     ALLOWED_HOSTS = ['\<web-service-name\>.com', ...]
     Ensure
     DEBUG = False
     ```
17. Push your codebase to your Git repo
18. Once that is done, on the left hand column, click Environment
   - This is where you enter the contents of **env.py**
   - You do this by selecting by going to the **Secret Files** option
   - Under **Filename**, enter **env.py**
   - Under **Contents** copy and paste the contents of **env.py** into the box provided
   - Then click **Save Changes**
19. Everything should now be set up for deployment i.e. the database name, the 'secret' environment variables, <br>the *render.com web service name*
20. At the top right of the Render Dashboard, click **Manual Deploy** then **Deploy latest commit**
21. The date, time and *Building In progress* spinner will be displayed
21. Ensure there are no errors. Render will display the message **Your service is live** in the log,<br>whilst above the log, the word **Live** will be shown in green
22. Click the URL link of the form **https:\/\/\<web-service-name>.onrender.com/**

### How to Fork the Repository
1. Log in (or sign up) to Github.
2. Go to the TODO repository on GitHub.
3. Click the "Fork" button in the top right corner.

### How to Clone the Repository
1. Log in (or sign up) to Github.
2. Go to the TODO repository on GitHub.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
  
## Credits
+ Hero Image Photo of an *Opened Bible on a path during daytime* is by [Aaron Burden](https://unsplash.com/@aaronburden?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) at [Unsplash](https://unsplash.com/photos/opened-book-on-brown-field-during-daytime-4uX_r8OhJ_o?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
+ Photo of a man showing poster with the inscription *Who says a small poster can't start a big collection?* is by [Anete Lusina](https://www.pexels.com/@anete-lusina/) at [Pexels](https://www.pexels.com/photo/crop-man-showing-poster-with-inscription-on-white-background-6353838/)
+ All the images used for the Posters and the images of Passover, Pentecost and Feast of Booths were sourced from [Free Bible Images](https://www.freebibleimages.org/)
+ Dates used for Passover, Pentecost and Feast of Booths were sourced from [Chabad.org](https://www.chabad.org/holidays/JewishNewYear/template_cdo/aid/671894/jewish/When-Is-Sukkot-in-2024-2025-2026-2027-and-2028.htm)
        
## Acknowledgements
+ Code Institute's Boutique Ado Walkthrough Project upon which this project is modelled upon.
+ Code Institute's Tutor Support for their great patience towards me with my myriad of issues. Thank You!


