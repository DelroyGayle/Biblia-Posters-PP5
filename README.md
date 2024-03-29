# Biblia Posters
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/19dca679-1308-464b-9ddd-ec8575c1c3d5)

[View live website](https://biblia-posters-dg-869e3a15ddae.herokuapp.com/)

## Table of Contents

1. [Introduction](#introduction)
2. [Facebook Business Page](#facebook-business-page)
3. [User Stories](#user-stories)
4. [UX-User Experience](#ux-user-experience)
   1. [Wireframes](#wireframes)
   2. [Agile Design](#agile-design)
   3. [Data Models](#data-models)
   4. [Colours](#colours)
   5. [Typography](#typography)
   6. [Imagery](#imagery) 
5. [Features](#features)
   1. [Home Page](#home-page)
   	1. [Navigation](#navigation)
   	2. [About Us](#about-us)
   	3. [Special Days](#special-days)
   	4. [Newsletter](#newsletter)
   	5. [Footer](#footer)
   2. [Toast Messages](#toast-messages)
   3. [Menus](#menus)
   4. [Sorting](#sorting)
   5. [Searching](#searching)
   6. [Registration](#registration)
6. [User Walkthroughs](#user-walkthroughs)
7. [Logout](#logout)
8. [Reviews](#reviews)
9. [Wishlist](#wishlist)
10. [My Profile](#my-profile)
11. [Poster Management](#poster-management)
12. [Other Features](#other-features)
13. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Libraries and Frameworks](#libraries-and-frameworks)
    3. [requirements.txt](requirements-txt)
14. [Future Features](#future-features)
15. [Testing](#testing)
    1. [Please Go To TESTING.md](https://github.com/DelroyGayle/Biblia-Posters-PP5/blob/main/TESTING.md)
    2. [Bugs](#bugs)
16. [Deployment](#deployment)
17. [How to Fork the Repository](how-to-fork-the-repository)
18. [How to Clone the Repository](how-to-clone-the-repository)
19. [Credits](#credits)
20. [Acknowledgements](#acknowledgements)

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

## Facebook Business Page

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




This website uses the Django framework to generate the models used for the database. The SQL database is thereby hosted on  [ElephantSQL PostgreSQL](https://www.elephantsql.com/). 

This project and its models closely follow Code Institute's Boutique Ado Walkthrough, so there are many similarities.
For example, instead of a model depicting clothing and household goods, the walkthrough's example model is now used to depict posters.

<details>
<summary>Biblia Posters' Models Schema Diagram</summary>
<br/><br/>  


![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e527ae13-9444-45e4-8be1-b6b526f0db87)

Posters with Categories

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/9b21fa28-59b8-4834-8083-50b84174b4ce)


Allauth and Django.contrib models are as is. Category, Order, OrderLineItem, Checkout, and UserProfile are as described in the Boutique Ado Walkthrough.

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d82f7eb1-c857-40de-9b04-89fbe59328a9)

</details>


**Custom models**

The *custom* models that I designed are 
1. UserPurchasedPosters
2. Reviews
3. Wishlist
4. SpecialDays

```1. UserPurchasedPosters```

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/cf9d64b8-2cc9-4953-af30-449c408b3412)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c532dfb5-cb22-410e-a142-d8ab7a8c7004)

<hr>

``` 2. Reviews and 3. Wishlist ```

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/38db4c32-ea2d-469a-834e-328c37b7a9fe)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/10cd6aa0-b1d4-4c0b-8af5-a74ffa0cef50)

<hr>

```4. SpecialDays```

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/87fa3ffc-85c3-4cb8-9c67-b6f40983b841)

<hr>

* Regarding *UserPurchasedPosters*: To ensure that only *verified* purchasers are allowed to author reviews, each time a *registered* user purchases a poster, the user and poster IDs are written to the UserPurchasedPosters database. If such a record already exists then no further action. If not, a new UserPurchasedPosters record is created with the IDs.
* Regarding *Reviews*: From this point onwards, when a user views a poster page that the user has purchased, the user is given the option to _add, edit and delete a review_ regarding the post - hence CRUD functionality.
* Regarding *Wishlist*: A registered user has the option _to add a poster to their wishlist_ or _remove the poster from their wishlist_.
* Regarding *SpecialDays*: This holds a range of dates where a particular range of days are depicted as _Special!_.
* This database holds:
* * the date the range starts - **special_days_firstday** beginning at midnight
* * The date the range ends - **special_days_lastday** beginning at midnight
  * **special_days_id** is the ID number signifying which 'Special Day' - *0 for Passover, 1 for Pentecost and 2 for the Feast of Booths.*
  * See [Special Days](#special-days) for further details.
  


----

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

Please note: *21st February 2024* is **not the actual date** for Passover, Pentecost nor the Feast of Booths. These depictions of the banner are shown here for demo purposes only; indicating that the banner will change colour from black to green whereby the particular *event* is displayed alongside the offer of 25% Discount. Because of the submission date of this project, February dates were used for the sake of documentation. See [Special Days](#special-days) for further details.

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/caa6eaa3-5775-45d6-b6a7-c1dbef9d48d0)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/79989e3c-c76f-4d11-b74d-a9e2682f0943)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b82b5ae7-b3d7-43f6-b8bc-9e0de6090e4e)

Lastly, on the Hero Image is the **Shop Now** whereby the user is directed to the **All Posters** page to all available posters for sale.

**Mobile navigation bar and hero image**

For the mobile view, the same information is displayed as described above however the menu collapses into a hamburger menu.

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7f5d242a-c315-4ffb-b8c6-577b45a937e8)


![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c2941752-8f5e-4336-9fa5-16364ddb03c2)
<br>(19th February, 2024 is **not** the date of the Feast of Booths - demo purposes only - see [Special Days](#special-days))

#### About Us

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c05f3896-3e15-44aa-b97a-c13ee85748e0)

A description is given of the type of posters that this online store has to offer. It also points out the advantages of registering on the site.

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

The Django Queryset used to query the *SpecialDays* database has been set up, that for each range:
*  subtract **30 minutes** from midnight of the *FIRSTDAY*
*  add **24 hours 30 minutes** to midnight of the *LASTDAY*
*  Then check if the current date and time is between any of the ranges
*  If True, change banner to green and display 25% Discount offer - the *Special Days ID* indicates which title to display
*  If False, display black banner - no discount offered

<details>
	<summary>Sample Data of Special Days 25% Discount Applied</summary>

* **(Because of the submission date of this project, *February dates* were used for testing purposes.)**
* As aforementioned, when the Django Queryset of *SpecialDays* returns *True*,
* The banner will turn green and the title of the *Special Days* event is displayed alongside the 25% Discount message
* Also, when the order is displayed at checkout
* A *line of information indicated by a **red asterisk*** is displayed
* Pointing out to the user, that 25% discount has been applied to the order
* The order confirmation email will also be updated with the same line of information
* Please note: **the delivery cost of £3.00 still remains the same - it is not discounted**
* Here are some examples


1)


* **Passover**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fd83d329-9082-461b-abc7-75b3d900ec3a)

* At the top of the order, the cost of the poster is shown to be normally £8.00; however the total has been discounted by 25% to £6.00
* Note the red asterisk and the line *Passover 25% Discount has been applied to the order*

    ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b1264622-fc0c-4179-9079-c1e2e82918f3)

* Same line shown in the email text - with an asterisk

```
Subject: Biblia Posters Confirmation for Order Number
 0A12733F7BF7498994FBDC515052EA75
From: biblia@example.com
To: super@example.com
Date: Wed, 21 Feb 2024 13:03:56 -0000
Message-ID: ...

Hello super!

This is a confirmation of your order at Biblia Posters. Your order information is below:

Order Number: 0A12733F7BF7498994FBDC515052EA75
Order Date: Feb. 21, 2024, 1:03 p.m.

Order Total: £6.00 *
Delivery: £3.00
Grand Total: £9.00
* Passover 25% Discount has been applied to the order

Your order will be shipped to 123 Any Street in London, GB.

We have got your phone number on file as 00123-456789.

If you have any questions, feel free to contact us at biblia@example.com.

Thank you for your order!

Sincerely,

Biblia Posters

-------------------------------------------------------------------------------

```


2)


* **Pentecost**

  ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d820595f-7e1d-4bad-a331-53097d0f7872)

* Total cost of posters, £12.00; however the total has been discounted by 25% to £9.00

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/2da90504-296e-4336-bb96-8c0436eafcb2)

* The email

```
Subject: Biblia Posters Confirmation for Order Number
 49E1868D1E784F739E5DFB9B457064AB
From: biblia@example.com
To: super@example.com
Date: Wed, 21 Feb 2024 13:37:15 -0000
Message-ID: ...

Hello Mr B. Smith!

This is a confirmation of your order at Biblia Posters. Your order information is below:

Order Number: 49E1868D1E784F739E5DFB9B457064AB
Order Date: Feb. 21, 2024, 1:37 p.m.

Order Total: £9.00 *
Delivery: £3.00
Grand Total: £12.00
* Pentecost 25% Discount has been applied to the order

Your order will be shipped to 123 Any Street in London, GB.

We have got your phone number on file as 00123-456789.

If you have any questions, feel free to contact us at biblia@example.com.

Thank you for your order!

Sincerely,

Biblia Posters

-------------------------------------------------------------------------------

```


3)


**Feast of Booths**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/448a44a7-b84b-4a74-9030-494ed261924f)

* Total cost £9.00; however the total has been discounted by 25% to £6.75

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c89bf9ab-100f-45d6-9ebf-9795c3dedd1a)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/327f51e3-c69d-4c7b-b1e7-f7b57654ad84)

* The email

```
Subject: Biblia Posters Confirmation for Order Number
 395DD115DF12432FAA98402B536D121F
From: biblia@example.com
To: super@example.com
Date: Wed, 21 Feb 2024 13:42:26 -0000
Message-ID: ...

Hello Mr C. Smith!

This is a confirmation of your order at Biblia Posters. Your order information is below:

Order Number: 395DD115DF12432FAA98402B536D121F
Order Date: Feb. 21, 2024, 1:42 p.m.

Order Total: £6.75 *
Delivery: £3.00
Grand Total: £9.75
* Feast Of Booths 25% Discount has been applied to the order

Your order will be shipped to 123 Any Street in London, GB.

We have got your phone number on file as 00123-456789.

If you have any questions, feel free to contact us at biblia@example.com.

Thank you for your order!

Sincerely,

Biblia Posters

-------------------------------------------------------------------------------

```

</details>


* Let me reiterate, that because of the submission date of this project, *February dates* were used for testing purposes and for the sake of documentation.
* However, **anyone visiting *the live site during the true dates of these events as shown above*, will see the banners and discounts in action!**

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
* * There is a Link for the [Facebook Business Page](https://www.facebook.com/profile.php?id=61556537234433)
  * There is a Link for Twitter
  * There is a Link for the related WordPress blog, namely, [AgeToCome](https://agetocome.wordpress.com/)

Then a note explaining that all the poster images used *are in actuality, **Free!*** <br>Moreover, there are available from [Free Bible Images](https://www.freebibleimages.org/)

### Toast Messages 

Feedback is delivered at all times to the user via the usage of Bootstrap Toast Messages. *Success* and *Alert/Info* indicators are displayed for *six seconds* before disappearing whilst *Error Message* indicators are displayed for *ten seconds* before disappearing.<br>These messages are always  Login status is always shown in the right hand corner of the screen just below the navigation bar.

<details>
	<summary>Sample of Messages shown</summary>

 Signed In

 Signed Out

</details>

### Menus 

<details>

<summary>Available Menu Options</summary>
	
**Desktop**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/bb4703d0-5a32-4ab0-a2c7-e38ec6a60dfa)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ee394855-3c50-4063-8f2c-5ad980775a2e)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/645d144f-7761-44d6-922f-fc91df115687)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/dc754798-19a2-4616-954d-3e5885174fa3)

**Mobile**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/da618cdc-4a84-4029-a2e6-501da9de07c6)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/3621eacb-19f9-4b28-a762-9879dc0f90e8)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f5563f82-9402-4d22-b177-bafff950706e)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/bee3c71d-d1d5-42fe-825a-7719cf35d276)

</details>

Please note: the number of posters listed is showed at the top-left of the screen

#### Old Testament - Genesis

<details>

<summary>Display of Genesis Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5d86495b-8305-4ad7-9db1-d54acb15bccf)

</details>


#### Old Testament - Exodus

<details>

<summary>Display of Exodus Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b03189ae-150c-4b7e-b982-67369f499236)

</details>


#### Old Testament - Numbers

<details>

<summary>Display of Numbers Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5f43584a-b9cf-4212-8457-667f979b6fd4)


</details>


#### Old Testament - Joshua

<details>

<summary>Display of Joshua Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d125a5dd-2da9-48c8-8d85-0bca33ef07fc)


</details>

#### All The Old Testament Posters

<details>

<summary>Menu & Display of all the Old Testament Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fb28fafb-b018-42a3-8ee6-26bf023e50d7)

<summary>All the Old Testament Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/2f6bc6e8-d2dd-434e-96f7-d8bfebd738c6)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e20803a6-0c31-4679-b240-0573579802ac)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/eeb105d4-1521-4b8a-a577-ae254ae8c7e0)

</details

#### New Testament - Jesus

<details>

<summary>Display of Jesus Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a5f6c916-a501-488b-9522-cd8fef3cdb39)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/262df841-30cd-43c1-8379-fd958a51ea74)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7d0b2762-b03b-44f6-bfbe-5d03fa80e438)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f31eba18-bfe0-4eb7-ae98-a49e4c251a54)

</details>

#### New Testament - Apostles

<details>

<summary>Display of The Apostles Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b9065ab6-2860-46ce-b867-3b4b0120d6f5)

</details>

#### All The New Testament Posters

<details>

<summary>Menu & Display of all the New Testament Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/36b91986-bf54-434e-b8a9-11e7f2bf1926)


<summary>All the New Testament Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a5f6c916-a501-488b-9522-cd8fef3cdb39)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/262df841-30cd-43c1-8379-fd958a51ea74)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7d0b2762-b03b-44f6-bfbe-5d03fa80e438)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f31eba18-bfe0-4eb7-ae98-a49e4c251a54)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7c2f09e3-bca3-4d63-a884-2adfce760a62)

</details>

### Sorting

Please note: the number of posters listed is showed at the top-left of the screen

#### Sort By Price


![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/8e40bde7-608d-43e7-82c1-8f500df8b8b1)

<details>

<summary>Price in ascending order</summary>

Cheapest at the top

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/34cf62ea-5c37-4215-83a1-4df720f4a1f1)

Most expensive at the bottom

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/9dedb441-2e98-4664-9c6c-a3a7cc9c9a65)

</details>


![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/3b8410dc-7de8-46dc-a270-b7c50bfdcc2d)

<details>

<summary>Price in descending order</summary>

Most expensive at the top

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7b62e745-6247-43e7-9cd3-2f081948964a)

Cheapest at the bottom

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/41bf0347-ff8d-4225-85e8-b478a6515b1b)

</details>

#### Sort By Rating

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ff3b83b8-8320-4527-ab85-063c40ba69c6)

<details>

<summary>Rating in descending order</summary>

Highest ratings at the top

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/109db7e9-3c41-4267-95bb-36518f824e9d)

Lowest ratings at the bottom

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/243b55c9-347e-4769-a05c-780041731fc4)

</details>


![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/bb10ad19-74e9-4022-9ec3-50c23de23218)

<details>

<summary>Rating in ascending order</summary>

Lowest ratings at the top

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e95ee491-62f7-4ef5-8775-4f8ba2411ac6)

Highest ratings at the bottom

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/097d785c-489c-4a40-8c27-ec1e661f5b12)

</details>

#### Sort By Name

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fdcab32a-27a0-4287-8d12-b8fb3ad0b276)

<details>

<summary>Name in Alphabetical Order i.e. Abraham, ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/51d1847d-71ed-4b95-8fab-0f9e954ab72d)

</details>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ecc78c53-de13-4ff9-b761-2c53ead26c7f)

<details>

<summary>Name in Descending Alphabetical Order i.e. Zacchaeus then Timbrels ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/54d39419-0ffa-4b9e-994f-69305e5103d1)

</details>

#### Sort By Category

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ac51d05d-e79b-4a35-945e-e3a8c8653577)

<details>

<summary>Category in Alphabetical Order i.e. Apostles, ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6bb76e41-4c54-40dc-90ae-dd31448562d0)

</details>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/952f6bbc-95cd-428d-b230-f47883b1fec9)

<details>

<summary>Category in Descending Alphabetical Order i.e. Numbers then Joshua ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ccbbfa40-f228-424b-bb74-f33f45a1e31a)

</details>

#### Sort By...

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/911f4bfa-feeb-4398-9356-a88ea1d278e2)

<details>
	<summary>This option shows all 52 Posters</summary>

 ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/2f6bc6e8-d2dd-434e-96f7-d8bfebd738c6)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e20803a6-0c31-4679-b240-0573579802ac)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/eeb105d4-1521-4b8a-a577-ae254ae8c7e0)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a5f6c916-a501-488b-9522-cd8fef3cdb39)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/262df841-30cd-43c1-8379-fd958a51ea74)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7d0b2762-b03b-44f6-bfbe-5d03fa80e438)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f31eba18-bfe0-4eb7-ae98-a49e4c251a54)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7c2f09e3-bca3-4d63-a884-2adfce760a62)

</details>

### Searching

What follows is a sample of the *case-insensitive* searches and their results.

Please note: the number of matched posters is showed at the top-left of the screen

<details>
<summary>/posters/?query=saul</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/0646712d-33e8-491a-9ecc-ef74159f91a9)
  
</details>

<details>
<summary>/posters/?query=ethio</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/3bda67f6-038b-4116-8f18-4ed186f1b205)
  
</details>
/posters/?query=BED matched 5 posters 

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/4da87e73-00f3-477f-9994-895a5e3e8285)

<details>

<summary>What follows are two posters where the match for 'BED' was in the descriptions</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fcca6530-f744-4103-832a-c2c1fcaef91a)
(I viewed the description then *used CTRL-F and 'bed' to highlight that the search was indeed successful*)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5e59d029-1f07-484e-896f-83f2591af1dc)
 
</details>

<details>
<summary>/posters/?query=HELLO</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b93c8664-ba08-439a-a9b7-b392a15dc771)
  
</details>

<details>
<summary>Null Entry in Searchbar</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e8160d1b-ba71-44c3-aa54-f54fcffbca2f)
  
</details>

------


 ### Registration

 * The [django-allauth](https://docs.allauth.org/en/latest/) is used to cater for authenticated registration, login, logout and lost passwords.<br>
 * The user has to select a unique username, email and password which must be confirmed via a link generated by *allauth*. <br>Once confirmed, the user can thereby login to the website in order :-
 * * To set up a profile.
 * * To add or Remove posters from a wishlist.
   * To write reviews regarding posters that the user has purchased - hence, **verified** purchasers only can add reviews.


------

## User Walkthroughs

What follow are sample walkthroughs showing the functionality of the **Biblia Posters** website

After a user clicks the **Shop Now** button the *All Posters** page is displayed showing all available 52 posters

<details>
	<summary>All Posters Page</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/17e90a6b-4773-4473-a5db-5dc582ede526)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f2f681d8-edcd-411b-879c-ccc82a15757f)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/369f3601-9eca-4354-ac9b-61c4c168cb67)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/46176bc3-5b99-4451-84b4-ff3ff431d766)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/46608cf4-7c82-4790-ae67-155e4be2b488)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d375e572-344b-437e-b645-4d21a4b48327)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/11d90f00-dff1-408d-8e88-0920553a2385)


</details>

### A Typical Shopper - Unregistered

To select a Poster the user clicks an the image for example after clicking


![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/1dda5b39-fe4c-4331-b5ba-f7b02ac2dbc8)

The *Poster Details* page of the selected poster is then displayed

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/573e8fd4-04ac-4795-85fc-958ca365203e)

The User has the option to adjust the quantity e.g. changed from one to two

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/128045ad-e6e0-4c85-80b6-3f31ad03137a)

Click *ADD TO BAG*

A message is instantly showed to illustrate an updated Shopping Bag
In this case 2 X £5 = total of £10 *excluding* delivery

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/2c34adca-1e3c-4759-9f88-4ca4513df31b)

However including the delivery cost of £3 gives a total of £13

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/1a62557e-216d-4318-a6c5-19c7a0b384f4)

When the user clicks the Shopping Bag total in blue the user is taken to the *Shopping Bag* page

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ec59c42f-4095-4547-93d5-0206ba306e2d)

Which shows 
* the poster(s) (and description(s)) being purchased
* The price of the individual poster
* The Quantity selected
* The Subtotal
* Bag Total and Delivery
* Grand Total

(The user also has the option of to leave the Shopping Bag and contining shopping by clicking *KEEP SHOPPING*)

Click *SECURE CHECKOUT*

* On the left the user is shown a form to add the delivery address
* On the right an Order Summary is given
* The user is given a reminder to *create an account* in future to save the address details or
* if the user is a registered user, to login in order to use the *saved profile address details*
  
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7dcd212d-faa9-4a96-9c18-cb1f5433079f)

* The Stripe test card number is *4242 4242 4242 4242*<br>
* Any CVC and  any suitable date in the future can be used for the expiration date
* Followed by any **five-digit** postal code

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d9b7cfb1-008a-4b3f-b095-141ce610e440)

Once the transaction is being acted on, a blue rotating spinner will be displayed on a blue overlay

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/da381165-eb93-40fa-a1c8-9b405b1163ce)


After a successful transaction, a Success message will be showed in the top right corner

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6f9980e4-d039-4e83-89dd-a56a30fa2317)

With the Shopping Bag reset to zero

Whilst on the left of the page is a **THANK YOU** showing the details received and a message indicating that a confirmation email of the order would be sent to the user's email

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6967161d-c0f9-4c95-ae63-86ccbca56ffe)


### A Typical Shopper who chooses to Register

* Select the Register option

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/4dbb2acf-cef8-4641-8aef-6635e76e2c68)

* The Signup page would be displayed

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c4390b8e-8560-4c72-9cf1-935655b60d61)

* The user then needs to enter a unique email, a unique username and a unique password

* Once the *allauth* system verifies that the entered details are correct, a message will be displayed to indicate that a confirmation email has been sent to the user

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/55a7ec77-d22a-4010-929f-e9eed609e98b)

<details>
	<summary>Sample of a registration confirmation email</summary>

Subject: [example.com] Please Confirm Your E-mail Address
From: biblia@example.com
To: jsm30171@zslsz.com
Date: Mon, 26 Feb 2024 11:15:03 -0000
Message-ID: ...

Hello from example.com!

You're receiving this e-mail because user james has given yours as an e-mail address to connect their account.

To confirm this is correct, go to .../accounts/confirm-email/MQ:1reYwp:qI9yPIO-fWF4Fblsa9yTsN4X04zcx9phpLnEPCaLQ0w/

Thank you from example.com!

example.com

-------------------------------------------------------------------------------

</details>

* Within the email would be given an *allauth* generated link.
* When the user clicks the link they would be directed to the confirmation page which displays

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c961e371-e5eb-408e-a013-1dc51fb45e9a)

* The user clicks *Confirm*
* The *Sign In* Page would then be displayed with a Success message in the top-righthand corner

  ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/635378c1-e149-4199-bb18-d30c262b445a)

  ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/57ffa7fe-5534-4eb2-9b6d-5f03a4a5b138)

* The user can now sign-in - a message indicating a successful sign-in will be displayed

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c949dbac-e19e-439b-a1f4-8baa24b0d09e)

* Now when a user makes a purchase they have the checkbox option to save the delivery address to their profile

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f28bd6a2-ce83-48e2-a18e-aa98585c6ced)



<details>
	<summary>Sample of an order confirmation email</summary>

```
Subject: Biblia Posters Confirmation for Order Number
 0988506B9202410C9A1DB1D803E7450E
From: biblia@example.com
To: jsm30171@zslsz.com
Date: Mon, 26 Feb 2024 11:37:51 -0000
Message-ID: ...

Hello James Smith!

This is a confirmation of your order at Biblia Posters. Your order information is below:

Order Number: 0988506B9202410C9A1DB1D803E7450E
Order Date: Feb. 26, 2024, 11:37 a.m.

Order Total: £9.00 
Delivery: £3.00
Grand Total: £12.00


Your order will be shipped to 123 Any Street in London, GB.

We have got your phone number on file as 00123-456789.

If you have any questions, feel free to contact us at biblia@example.com.

Thank you for your order!

Sincerely,

Biblia Posters

-------------------------------------------------------------------------------

```

</details>



* As a registered user, a record of each purchase order is recorded for the user's perusal
* The most recent shown at the top; that is, the user's order history is shown in *descending date* order
* A tooltip is displayed when the user hoovers the mouse over the truncated order number which then displays the full order number


![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c1755582-6f95-4981-8beb-cda6e5d3fd55)


* If the user clicks the *order number url* the *past* purchase order would be displayed
* With an accompanying message indicating that this is a *past* confirmed order and that an email had been sent e.g.

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e9ca760f-d995-414f-89aa-33ebe3b66bf2)


## Logout

The registered user has the menu option to logout

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/9733d1be-1712-4645-94e3-4e3209658055)

* A sign out page is shown with the question: *Are you sure you want to sign out?*
* Also shown are the *Sign Out* and *Cancel* buttons

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b623de1d-1529-4290-a672-4e44f3ffb7d5)

* Clicking *Cancel* will take the user to the *Home Page*
* Clicking *Sign Out* - a *Signed Out* message is shown

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/22b444b2-3c00-43b0-b0ff-23ade8c1709e)


## Reviews 

<details>
	<summary>Review functionality</summary>
	
### Add a Review
* As a registered user, the user has the option to _add, edit and delete reviews_ regarding any posters that they have purchased
* When the user views the *details* page of a poster, the option is shown as **Review - Add**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/77cf78d9-16c6-4dfe-aecb-3eed604d5dda)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a116c72f-e6f6-43a2-8ea0-cac0b21a5025)


* To Add a Review, a form is shown for the user to enter consisting of
* * User displayed name
  * Title of the review
  * Content
  * Rating - integers in the range 0 to 5
  * Validation is performed on the Price field
* Please note: if the *User displayed name* is blank, the reviewer's name will be displayed as **Anonymous**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b5c07fec-33f1-4399-99f6-91705c282fe8)

* A message is shown when a Review is added
* The *User displayed name* and the Review Title are shown in *title-case*
* If a nonzero rating was given, the said number of stars are shown

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6f49f975-b930-4c3c-b5b6-9c8bfafe7a1c)

* From this point onwards, when any shopper who views the *details page* of a poster <br>and scrolls down pass the *ADD TO BAG* button
* the shopper will then be able to see the review(s) left by shoppers
* Please note: the review date always reflects the date the review was created

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d7f7a7ea-2c15-43c3-aaa3-9324d4d9817b)

Once a user has written a review, any time the user revisits the poster, <br>there is now the option to **Review - Edit | Delete**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6428d70f-f0eb-4849-895a-1214dd8d0320)

### Edit a Review

* Reviews are shown on the *Poster Details* page in *descending date order*
* That is, the most recent reviews are shown at the top, older ones towards the bottom
* However if the *viewer* of the page happens to be the user who has authored a review of said poster, <br>**the user's review is shown first!**
* Followed by any other reviews in descending date order.
* When the author of a review clicks the *Edit* option, a message would be displayed to inform the user, the title of the review that the user is currently editing 
* The form with the current Review details is shown
* Validation is performed on the Price field

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5a0f9998-ad9a-46eb-ac08-4097b3fe4c17)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/52da2cde-57a5-4106-a601-9d12e494e9d6)

* Any changes can now be made to the review
* Clicking *Cancel* will take the user back to the *Poster Details* page

* Here are two scenarios:
  
**1) Blank out the reviewer's name**
   
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/77a42e35-55f3-483a-b3ad-496feb2f5fcb)

* Click *Update Review*
* Message showing a successful update

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/9c37590b-a3fb-4380-a26c-5b0c56346129)

* The Review is updated with the new details
* The *Poster Details* page is refreshed showing whatever changes were made <br>with **the user's review shown first**
* Please note: the review date always reflects the date the review was updated
* In this example, the user is now shown as an *Anonymous* reviewer
  
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f876bef6-6ffd-40cb-9ac8-8251a15dbc9e)

**2) Name changed to Jimmy and a Zero rating given**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/73a53fe8-1b8a-4fa9-a511-918eff64f43b)

### Delete a Review

* When the author of a review clicks the *Delete* option 
* A summary page is shown displaying the title of the review and up to forty words of the review content
* With the warning: *Are you sure you want to delete?*
* Also shown are the *Yes* and *Cancel* buttons

  ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f24e86ce-6215-4639-8281-d0b8cad1aaaa)

* Clicking *Cancel* will take the user back to the *Poster Details* page
* Clicking *Yes* - a *Deleted* message is shown

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5d280a9b-9757-4485-a4d7-be275d24e755)

* The *Poster Details* page is refreshed with the user's review now removed

### My Reviews

* Menu option

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5511cde5-e844-4350-afd4-eef61fdefdb2)

* The number of reviews written by the user is shown at the top of the page. The heading is pluralised accordingly
* The date that the review was created or last updated is shown - The reviews are listed in *descending date order*
* That is, the most recent reviews are shown at the top, older ones towards the bottom
* On this page, the user has the option
* * to **EDIT REVIEW** or
* * to **DELETE REVIEW**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/068df20c-6418-449f-a8ec-9039cf478893)



### Edit Review

* The same functionality and messaging as described regarding the *Edit a Review* option on the *Poster Details* page is identical here
* The only difference is that if the user clicks *Cancel*, the user is directed back to the *My Reviews* page 


### Delete Review

* The same functionality and messaging as described regarding the *Delete a Review* option on the *Poster Details* page is identical here
* Regardless of whether the user clicks *Cancel* or *Delete*, the user is directed back to the *My Reviews* page 

**Empty User's Review Page**

* This page is shown when the user has *not* authored any reviews
* This page is also shown when the user has *deleted* all their reviews

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b09f02e7-f6dc-4c69-89a7-b6734e661726)

</details>



## Wishlist

<details>
	<summary>Wishlist functionality</summary>

### Add to Wishlist

* The registered user has the option to **Add to Wishlist** on the *details* page of a poster

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/90b8003e-4f79-4d62-a846-e79608a29344)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f620a711-b8ac-4b7f-80ba-ab69114b7c42)

* Once clicked, the user is alerted that the addition has been done

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/dab751c1-e924-4ce8-83ef-fd273ef2a0d5)

### Remove from Wishlist

* The option then toggles to a **Remove from Wishlist** option

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/991713f9-f068-44f0-8339-a0dcb3379b67)

* Once clicked, the user is alerted that the removal has been done

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/bd9c81ea-a9e0-4d7e-8163-4d0ab72842f7)

* The option toggles back to the **Add to Wishlist** option


### My Wishlist

* Menu option

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5511cde5-e844-4350-afd4-eef61fdefdb2)

* The number of posters on a user's wishlist is shown at the top of the page. The heading is pluralised accordingly
* The date that the poster was added is shown - The posters on the wishlist are listed in *descending date order*
* That is, the most recent additions shown at the top, older ones towards the bottom
* On this page, the user has:
* * the option to add a poster which is on their wishlist to the Shopping Bag
  * that is (each time clicked), *a quantity of one poster* to the bag
* * the option to remove the poster from their wishlist

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/8b38a444-f0c3-4cee-963a-e582f402eac9)

* Message when a poster is removed from the wishlist

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/881ecdc5-ac3f-4050-9477-0fd0f2d10d96)

* Message when a poster is added to the Shopping Bag 

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/57071e3c-3078-4701-8cdd-b690d3ed0309)


**Empty User's Wishlist Page**

* This page is shown when the user has *not* added any posters to their wishlist
* This page is also shown when the user has *removed* all posters from their wishlist

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/cf2f1c96-dd3a-49cf-a393-efaf5d3504a9)


</details>

## My Profile

* The page shows the *Delivery Details* of the registered user
* This information is saved and then used subsequently to autofill the user's delivery address details at checkout.

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a033419c-9193-4bd1-8842-38e22c3079d7)

* When the user clicks *UPDATE INFORMATION*, a *Updated* message is displayed

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/4c039d74-8eb2-4c78-9b8f-ab28995bb96d)

### Order History

On the right hand side of the *My Profile* page, a history of all the registered user's purchase orders are displayed in *descending date* order

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f1927b97-bb3e-453a-b314-648964ace304)

* A tooltip is displayed when the user hoovers the mouse over the truncated order number which then displays the full order number

* For example,
  
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c1755582-6f95-4981-8beb-cda6e5d3fd55)

* If the user clicks the *order number url* the *past* purchase order would be displayed
* With an accompanying message indicating that this is a *past* confirmed order and that an email had been sent e.g.

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e9ca760f-d995-414f-89aa-33ebe3b66bf2)

## Poster Management

<details>
	<summary>Poster Management functionality</summary>

* Menu option

The **Admin Site User** has an additional menu option called *Poster Management*

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/8f57df9b-1059-42d2-ba80-aef1130063ee)

* As an **Admin Site User**, the user has the option to _add, edit and delete posters_
* Therefore, when an **Admin Site User** views the *details* page of any poster, the *Poster - Edit | Delete* option is shown

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b279cf89-9ad0-4a26-8a7c-a1b837e21d42)

### Add a Poster

* After clicking *Poster Management*, a form is shown for the user to enter consisting of the Poster's
* * Category
  * Sku
  * Name
  * Description
  * Price - up to six digits
  * Rating - any decimal number in the range 0 to 5 (Cannot be greater than 5)
  * The default Rating of 5 is shown
  * Validation is performed on both the Price and Rating fields
  
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/3642dfec-2b25-4689-b6b2-a89ed339b151)

* Regardless of whether the user clicks *Cancel* or *Add Poster*, the user is directed to the *All Posters* page 
* A message is shown when a Poster is added

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ee8b3aa2-2d26-49ce-baa9-8f354780f987)

* This example shows an added poster with no image

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/908fe052-4dbf-4bc0-989b-f37538f3e300)

* The *Select Image* is included in order for the user to select an image from their computer
* So, this example shows a poster with an image

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/8a86e9f3-7e33-43ed-97d0-2929d6c2e4c8)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a0080893-fb88-4538-bb94-94518c385fb3)

* From this point onwards, new posters can be view, sorted, purchased, just like any other posters

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/96259fd1-b3f4-456b-b053-a1a161bac58c)

### Edit a Poster

The **Admin Site User** has the option to **Poster - Edit | Delete** from a *Poster Details* page

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/9c3567df-08e0-4a57-9b33-b85a7daa7882)


* When the user clicks the *Edit* option, a message would be displayed to inform the user, the title of the poster that the user is currently editing 
* The form with the current Poster details is shown
* If the poster has an image, a clickbox is displayed giving the user the option to *Remove* the image from the poster
* The user also has the *Select Image* option
* The same validation is performed on both the Price and Rating fields

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/58b8e763-f9f0-4975-a384-1b37c0346b3d)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d4596fd9-a430-45d5-beb8-4d50a2557b14)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/64764de2-39f7-4aca-8aa2-db974c5d38f4)


* Any changes can now be made to the poster
* Clicking *Cancel* will take the user back to the *Poster Details* page of the Poster in question
* Clicking *Update Poster*
* Message showing a successful update

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fa67ae5b-54c2-4f7d-8845-7c1401556550)


* The Poster is updated with the new details
* The *Poster Details* page is refreshed showing whatever changes were made to the poster

### Delete a Poster

* When the **Admin Site User** clicks the *Delete* option 
* A summary page is shown displaying the title of the poster and up to forty words of the poster's description
* With the warning: *Are you sure you want to delete?*
* Also shown are the *Yes* and *Cancel* buttons

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/77a01495-c3f8-4e7f-a8d5-3878b98187a3)

* Clicking *Cancel* will take the user to the *All Posters* page
* Clicking *Yes* - a *Deleted* message is shown

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/c8ff7d1a-0595-43b8-8ac2-e8c368a1f76f)

* The user is taken to the *All Posters* page

</details>



## Other Features

There is a BackToTop button which is displayed on the following pages
* The Home Page
* The All Posters page
* The Poster Details page
* The Shopping Bag page
* The *My Reviews* page
* The *My Wishlist* page


  ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/95beffe9-ed70-436c-acdc-48504281d8d3)


------


## Technologies Used

### Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  
### Libraries and Frameworks

* [Django](https://www.djangoproject.com/) was used as the web framework.
* [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/)was used for Responsiveness website design
* [ElephantSQL PostgreSQL](https://www.elephantsql.com/) was used for hosting the SQL Database
* [GitHub](https://github.com/) for hosting the site
* [Gitpod](https://www.gitpod.io/) for editing the files
* [Heroku](https://heroku.com) for the deployment of the site
* [Jquery](https://jquery.com/) for scripting purposes
* [Miro](https://miro.com/) was used to create the wireframes
* [Django Extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html) was used to draw the Django models
* [Am I Responsive](http://ami.responsivedesign.is/) was used for creating the multi-device mock-up shown at the top of this README.md file
* [Favicon](https://favicon.io/) was used to generate the Favicon
* [Mailchimp](https://mailchimp.com/) was used for the Newsletter
* [Privacy Policy Generator](https://www.privacypolicygenerator.info/) was used to produce the Privacy Policy
* [Code Institute's GitHub full template](https://github.com/Code-Institute-Org/python-essentials-template) in order to run Django and Python on Heroku/Render

### requirements.txt

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

### Bugs

------

## Deployment

The project is deployed on Heroku.<br> 
Heroku is used to deploy the final project.

1. You need to create an account at [Heroku](https://signup.heroku.com/).
2. Once you have logged in, click the button 'New' and select 'Create new app'.
3. Name your app, then select what region is closest to you and click 'Create App'.
4. Then on the resources tab, navigate to the 'Add-ons' section and search for 'Heroku Postgres'.

Regarding your Django App, in order to use Postgres you will need to install dj_database_url and psycopg2. 

1. In your IDE type the command:  
    `pip3 install dj_database_url`
2. Then once that is installed type the command:  
    `pip3 install psycopg2-binary`
3. Then, to make sure Heroku install all your apps requirements when you deploy it, run the command:  
    `pip3 freeze > requirements.txt`
4. Next, navigate to your setting.py file in your main project folder. At the top of the file add the line:  
    ```
    import dj_database_url
    ```
5. Then scroll down the file till you find your database settings. Comment out the default configuration and underneath insert the code:  
    ```
    DATABASES = {
        'default': dj_database_url.parse(*Enter Database URL here*)
    }
    ```
    The database URL can be found in the settings tab of your app in heroku, under Config Vars. 
6. Once that is saved, you will now need to run migrations in order to connect to a new database. This is done by running the command:  
    `python3 manage.py migrate`
   If you have any *fixtures i.e. json files* perform  `./manage.py loaddata <NAME>` in order to import your data into the postgres database
7. Create a superuser for the new database. The command is:  
    `python3 manage.py createsuperuser`
8. Check that all *secret keys* have been removed from settings.py.
9. Ensure that the DATABASE_URL handling in settings.py has been updated as follows:  when using the app on heroku or sqlite if not. Scroll back to the database section and refactor the code to look like this:  
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
    ```
10. Install  gunicorn:  
    `pip3 install gunicorn`
    Freeze the requirements.txt file with:  
    `pip3 freeze > requirements.txt`
11. Create in your root directory, a file called Procfile. This file tells Heroku to create a web dyno. 
Insert the code:  
    `web: gunicorn **'your_projects_name_here'**.wsgi:application
12. Then, back in heroku, navigate to settings and in the config vars input the key DISABLE_COLLECTSTATIC with the value 1, and click 'Add'.
This is to stop Heroku from collecting any static files when you deploy.
13. You will also need to add the Heroku app to your allowed hosts in your settings.py.    
    ```
    ALLOWED_HOSTS = [<your heroku app name>.herokuapp.com', 'localhost']
    ```
14. Now add, commit and push these changes, followed by a push to heroku with the command:  
    `git push heroku main'
    Your app will now be deployed
15. Please note: using a host such as AWS or Cloudinary, you now need to add the necessary host file details to your Heroku config vars in order for the Heroku app to process the *static files* needed for your project.

## How to Fork the Repository
1. Log in (or sign up) to Github.
2. Go to the repository that you wish to fork on GitHub.
3. Click the "Fork" button in the top right corner.

## How to Clone the Repository
1. Log in (or sign up) to Github.
2. Go to the repository that you wish to clone on GitHub
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


