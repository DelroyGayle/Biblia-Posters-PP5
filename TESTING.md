# Testing

1. [HTML Validation](#html-validation)
2. [CSS Validation](#css-validation)
3. [JavaScript Validation](#javascript-validation)
4. [Python Validation](#python-validation)
5. [Lighthouse](#lighthouse)
6. [Manual Testing](#manual-testing)
   
## HTML Validation
This was performed using [W3C HTML Validator](https://validator.w3.org/nu/)

* There were conflicts with the validator and Django Template Language, for example

* TODO

* Spaces following % produced "Non-space characters found without seeing a doctype first."

* Besides these conflicts I changed all my \<article\>'s and \<section\>'s to \<div\>'s

* *Warning: The type attribute is unnecessary for JavaScript resources.*

## CSS Validation

This was performed using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

 - No issues flagged during CSS validation

## JavaScript Validation

This was performed using [JSHint](https://jshint.com/)

## Python Validation

This was performed using Code Institute's [PEP8 Linter](https://pep8ci.herokuapp.com/)

- No issues flagged during Python validation

## Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility and SEO of the website.

<details>
  <summary>Lighthouse Report</summary>

   Home Page

   ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/4dff288c-a0e5-4164-ab34-8bf57e32655e)

   Posters Page ... **/posters/**

   ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/67459201-10e3-4275-bc77-c587434762bc)


</details>

## Additional Testing Comments
+ Carried out tests of the program on both the local terminal and the Code Institute Heroku terminal.
+ Chrome DevTools was used throughout the development process for testing purposes.
+ Added Custom *404 and 500* pages in case any errors occur.
  
## Manual Testing 

### Epic: *Register and Login*

This is broken down into the following
<details>
  <summary>User Stories</summary>

   ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/09e75a1c-7f1c-4d9c-bad2-25f12dd0886a)
 
  ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/982af554-be3f-4d82-9699-e0fc75fba0b7)

</details>

Criteria:
1. Both Username and Email is necessary to login
2. Verification by Email is mandatory
3. Minimum username length is 4 characters

**User Tasks:**
1. Update the Admin domain of the default site to **biblia.example.com**
2. Demonstrate that the user can Register using a username, password and email address
3. Verify that both the Django and Allauth acknowledge the user's email address
4. Demonstrate that the user can Login to the site
5. Demonstrate that the user can Logout from the site


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T01 | Register, Login, Logout | Using Allauth incorporate Register/Login/Logout functionality | That the above User Tasks are accomplished | PASS |

<details>

<summary>Verify Registration</summary>

Select the Register option
In this example I registered the username **Tommy**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7edc1c29-02b7-46c5-932f-380ba63288cb)

Once the account is registered change the Endpoint to **/admin/account/emailaddress/**

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/324ee5ea-9144-40ff-abfc-426de3fa1102)

Click to verify the email in the Admin Dashboard

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/89f40c3c-b4fb-4cec-8511-ff9ea6c35743)

Confirm That the Email Address is Verified

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a4e72bbe-d3e8-4ee0-8131-dd71b46710a5)

</details>

<details>

<summary>Go back to the App Name/ URL and Logout</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/4e061c55-04bc-4ea5-a64f-8c2288a55dfc)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7b4b1f8c-8cee-4f1e-9c0d-ed3001947436)

</details>

### Epic: Viewing Posters which includes Menus, Categorisation and Sorting

This is broken down into the following

<details>
  <summary>User Stories</summary>

   ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/63d0bf5f-f0b7-46df-b3aa-5544058c2684)

   ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/9e9ea1e4-a20d-4400-98d7-122dbfbc291b)

</details>

**User Tasks:**
1. When the user selects the *Shop Now* option, the user can see all available posters
2. User has the option to view particular *categories* of posters using drop-down menus
3. Posters can be sorted by Price, Rating, Poster Name, and Category
4. That all the above work correctly with responsiveness on different sized media

In this online store there are *52 posters* available.

<details>

<summary>Sample of a poster image: The_Resurrected_Jesus_Shows_His_Disciples_His_Pierced_Hands_And_Feet.jpg</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6af9e35d-45e1-403a-a26e-9ac9ca2d3688)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T02 | View Available Posters | Click the Shop Now button from the Homepage | All available (52) posters are to be shown | PASS |

<details>

<summary>Top of the page</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/0b94d27e-3d37-45c1-bd14-adc03e76b3da)

</details>

<details>

<summary>Bottom of the page</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/81d80de2-7054-4604-80b8-0afe0f23b57a)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T03 | Responsiveness when Viewing Posters | Using the Inspect Tool, demonstrate the view of posters | All available (52) posters are to be shown regardless of the media size | PASS |

<details>

<summary>Large Screen</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/94007ffb-4603-4af9-a198-e7fe3d43f96c)

</details>

<details>

<summary>Tablet</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7d3d6e3b-4e59-48bc-9df7-76f646148dcc)

</details>

<details>

<summary>Mobile</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/516cf97f-679a-451c-b0ba-50ea4b013495)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/849b30ff-79fb-49b2-ac5d-5a077e429e7d)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T04 | When a Poster is selected, its details are displayed | From the View of Posters, click the image | The poster image is shown with description and rating | PASS |

<details>

<summary>View Poster Details - Desktop</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/627c0551-ee23-476c-b8c7-4db0f611747b)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T05 | View Available Posters | Click the Shop Now button from the Homepage | All available (52) posters are to be shown | PASS |

<details>

<summary>View Poster Details - Mobile</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d466b50b-0db2-44b4-bce5-1d69dccba24d)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T06 | View All Available **Old Testament** Posters | Select from Menu, Old Testament then select **ALL O.T. Posters**  | All available OT posters are to be shown - Categories */posters/?category=genesis,exodus,numbers,joshua* | PASS |


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
| T07 | View All Available **New Testament** Posters | Select from Menu, New Testament then select **ALL N.T. Posters**  | All available NT posters are to be shown - Categories */posters/?category=jesus,apostles* | PASS |

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
| T08 | View All **Genesis** Posters | Select from Menu, Old Testament then select **Genesis**  | All available Genesis posters are to be shown - Endpoint */posters/?category=genesis* | PASS |

<details>

<summary>Display of Genesis Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5d86495b-8305-4ad7-9db1-d54acb15bccf)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T09 | View All **Exodus** Posters | Select from Menu, Old Testament then select **Exodus**  | All available Exodus posters are to be shown - Endpoint */posters/?category=exodus* | PASS |

<details>

<summary>Display of Exodus Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b03189ae-150c-4b7e-b982-67369f499236)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T10 | View All **Numbers** Posters | Select from Menu, Old Testament then select **Numbers**  | All available Numbers posters are to be shown - Endpoint */posters/?category=numbers*| PASS |

<details>

<summary>Display of Numbers Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5f43584a-b9cf-4212-8457-667f979b6fd4)


</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T11 | View All **Joshua** Posters | Select from Menu, Old Testament then select **Joshua**  | All available Joshua posters are to be shown - Endpoint */posters/?category=joshua* | PASS |

<details>

<summary>Display of Joshua Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/d125a5dd-2da9-48c8-8d85-0bca33ef07fc)


</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T12 | View All **Jesus** Posters | Select from Menu, New Testament then select **Jesus**  | All available Jesus posters are to be shown - Endpoint */posters/?category=jesus* | PASS |

<details>

<summary>Display of Jesus Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/a5f6c916-a501-488b-9522-cd8fef3cdb39)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/262df841-30cd-43c1-8379-fd958a51ea74)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/7d0b2762-b03b-44f6-bfbe-5d03fa80e438)

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/f31eba18-bfe0-4eb7-ae98-a49e4c251a54)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T13 | View All **The Apostles** Posters | Select from Menu, New Testament then select **Apostles**  | All available Apostles posters are to be shown - Endpoint */posters/?category=apostles* | PASS |

<details>

<summary>Display of The Apostles Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b9065ab6-2860-46ce-b867-3b4b0120d6f5)

</details>

#### Demonstrate that Posters can be sorted by Price, Rating, Poster Name, and Category

There are two ways of sorting 
1) By Drop-Down Menu:

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/643ed253-43a9-4016-ba88-ae6f3953527e)

2) Or By The Sort Selector

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/091078ad-b5b5-419c-9bb1-36d36729d3c9)

#### Demonstration of Each Method

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T14 | Sort Posters **By Price**, *Ascending Order* | Select from Menu, All Posters then select **By Price**  | Posters shown, cheapest at the top, lowest at the bottom - Endpoint */posters/?sort=price&direction=asc* | PASS |

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T15 | Sort Posters **By Price**, *Ascending Order* - Method 2 | From the Sort Selector, select **Price (low to high)**  | Posters shown, cheapest at the top, lowest at the bottom - Endpoint */posters/?sort=price&direction=asc* | PASS |

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
| T16 | Sort Posters **By Price**, *Descending Order* | From the Sort Selector, select **Price (high to low)**  | Posters shown, most expensive at top, cheapest at the bottom - Endpoint */posters/?sort=price&direction=desc* | PASS |

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
| T17 | Sort Posters **By Rating**, *Descending Order* | Select from Menu, All Posters then select **By Rating** | Posters shown, highest rate at the top, lowest rating at the bottom - Endpoint */?sort=rating&direction=desc* | PASS |

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T18 | Sort Posters **By Rating**, *Descending Order* - Method 2 | From the Sort Selector, select **Rating (high to low)** | Posters shown, highest rate at the top, lowest rating at the bottom - Endpoint */?sort=rating&direction=desc* | PASS |

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
| T19 | Sort Posters **By Rating**, *Ascending Order* | From the Sort Selector, select **Rating (low to high)** | Posters shown, lowest rating at the top, highest rating at the bottom - Endpoint *?sort=rating&direction=asc* | PASS |

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
| T20 | Sort Posters **By Category**, *A-Z* | Select from Menu, All Posters then select **By Category**  | Posters shown in Alphabetical Order of Category - Endpoint */posters/?sort=category&direction=asc* | PASS |

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T21 | Sort Posters **By Category**, *A-Z* - Method 2 | From the Sort Selector, select **Category (A-Z)**  | Posters shown in Alphabetical Order of Category - Endpoint */posters/?sort=category&direction=asc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ac51d05d-e79b-4a35-945e-e3a8c8653577)

<details>

<summary>Category in Alphabetical Order i.e. Apostles, ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/6bb76e41-4c54-40dc-90ae-dd31448562d0)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T22 | Sort Posters **By Category**, *Z-A* | From the Sort Selector, select **Category (Z-A)**  | Posters shown in Descending Alphabetical Order of Category - Endpoint */posters/?sort=category&direction=desc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/952f6bbc-95cd-428d-b230-f47883b1fec9)

<details>

<summary>Category in Descending Alphabetical Order i.e. Numbers then Joshua ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ccbbfa40-f228-424b-bb74-f33f45a1e31a)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T23 | Sort Posters with **All Posters**| Select from Menu, All Posters then select **All Posters**  | All **52** Posters shown - Default view - Endpoint */posters/* | PASS |

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T24 | Sort Posters with **All Posters** - Method 2 | From the Sort Selector, select **Sort by...**  | All **52** Posters shown - Default view - Endpoint */posters/* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/911f4bfa-feeb-4398-9356-a88ea1d278e2)

<details>

<summary>All 52 Posters - Default View</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/627c0551-ee23-476c-b8c7-4db0f611747b)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T25 | Sort Posters **By Name**, *A-Z* | From the Sort Selector, select **Name (A-Z)**  | Posters shown in Alphabetical Order of Poster Name - Endpoint */posters/?sort=name&direction=asc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fdcab32a-27a0-4287-8d12-b8fb3ad0b276)

<details>

<summary>Name in Alphabetical Order i.e. Abraham, ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/51d1847d-71ed-4b95-8fab-0f9e954ab72d)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T26 | Sort Posters **By Name**, *Z-A* | From the Sort Selector, select **Name (Z-A)**  | Posters shown in Descending Alphabetical Order of Poster Name - Endpoint */posters/?sort=Name&direction=desc* | PASS |

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ecc78c53-de13-4ff9-b761-2c53ead26c7f)

<details>

<summary>Name in Descending Alphabetical Order i.e. Zacchaeus then Timbrels ...</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/54d39419-0ffa-4b9e-994f-69305e5103d1)

</details>

### Epic: Search for Posters

<details>
  <summary>User Story</summary>
   
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/2d721ad9-5bd9-4fef-966d-85c6f0ec36d2)

</details>

**User Tasks:**
1. A successful search consists of whether the search term appears in the Poster Name or the Poster Description
2. Enter the search parameters via endpoints to perform a search e.g. */posters/?query=**saul*** to bring up all the posters with the search term *saul* in them
3. Use the Searchbar to enter the search term
4. Both methods should show identical results
5. Suitable messages when a null string is entered or null search results

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T27 | Search For Posters By Name | Either by using the Endpoint or Searchbar test various search terms| Any posters with matching names displayed | PASS |

<details>
<summary>/posters/?query=saul</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/0646712d-33e8-491a-9ecc-ef74159f91a9)
  
</details>

<details>
<summary>/posters/?query=ethio</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/3bda67f6-038b-4116-8f18-4ed186f1b205)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T28 | Search For Posters By Description | Either by using the Endpoint or Searchbar test various search terms| Any posters with matching descriptions displayed | PASS |

*/posters/?query=BED* matched 5 posters 

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/4da87e73-00f3-477f-9994-895a5e3e8285)

<details>

<summary>What follows are 2 posters where the match was in the descriptions</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fcca6530-f744-4103-832a-c2c1fcaef91a)

View the description then *used CTRL-F and 'bed' to highlight that the searches were successful*

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5e59d029-1f07-484e-896f-83f2591af1dc)
 
</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T29 | Null Search Toast/Message Displayed | Enter nothing in the Searchbar | A suitable message ought to be displayed | PASS |

<details>
<summary>Null Entry in Searchbar</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e8160d1b-ba71-44c3-aa54-f54fcffbca2f)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T30 | Nonexistent Search Toast/Message Displayed | Enter a search term in the Searchbar that does not exist in any of the posters | A suitable message ought to be displayed | PASS |

<details>
<summary>/posters/?query=HELLO</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b93c8664-ba08-439a-a9b7-b392a15dc771)
  
</details>

### Epic: Shopping Bag Functionality

This is broken down into the following

<details>
  <summary>User Stories</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e1062050-7c1c-40c3-b85e-df3fc6ef71c5)


</details>

**User Tasks:**
1. When the user selects the Shopping Bag Icon ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/ffa955a2-b5c9-457b-9db5-1d0de845e4d4)  <br> The user is taken to the shopping bag page whereby the user can see the bag contents.
2. From the shopping bag page the user has options to continue to add further posters to the bag
3. When use clicks Add To Bag ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/faac98c5-18d9-430d-978c-4df8c3a8d272)
<br> The Shopping Bag is adjusted by the quantity of posters that the user has selected
4. The quantities of Posters that have already been added to the bag can be increased or decreased
5. Posters can be removed from the bag even to the point that the bag is empty
6. The user can always see a running total each time, posters are added to or removed from the bag
7. Validation is performed when entering poster quantities


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T31 | Option to Keep Shopping after adding to the bag | On the Details page of a poster after entering adding poster to the bag, click KEEP SHOPPING  | The user is taken to the *Shopping* page | PASS |
* After adding poster (ID 5) to the bag the endpoint is *bag/add/5/* and the bag was updated accordingly<br><br>
* When ![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/0bead797-ae67-49fe-a768-d6c1f8380dc7) was clicked
<br> the endpoint was changed to *posters/* which reflects the *Shopping* page i.e. the view of all posters

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T32 | Validation of Quantities | On the Details page of a poster enter an illegal quantity  | The user would be informed that such quantities can to be entered | PASS |

<details>

<summary>Quantity Validation - Trying to enter a negative number</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/423164ab-94ed-4494-a963-1e181237374b)

</details>

<details>

<summary>Quantity Validation - Trying to enter a number greater than 99</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e5b82ae3-4d96-4613-9480-4d7a9c871a26)

</details>

<details>

<summary>Quantity Validation - Trying to enter a decimal number</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fb4f72fd-dd0c-4b92-9d7f-907260640ef7)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T08 | View All Genesis Posters | Select from Menu, Old Testament then select **Genesis**  | All available Genesis posters are to be shown | PASS |

<details>

<summary>Display of Genesis Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5d86495b-8305-4ad7-9db1-d54acb15bccf)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T08 | View All Genesis Posters | Select from Menu, Old Testament then select **Genesis**  | All available Genesis posters are to be shown | PASS |

<details>

<summary>Display of Genesis Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5d86495b-8305-4ad7-9db1-d54acb15bccf)

</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T08 | View All Genesis Posters | Select from Menu, Old Testament then select **Genesis**  | All available Genesis posters are to be shown | PASS |

<details>

<summary>Display of Genesis Posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5d86495b-8305-4ad7-9db1-d54acb15bccf)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T02 | View Available Posters | Click the Shop Now button from the Homepage | All available (52) posters are to be shown | PASS |

<details>

<summary></summary>

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T02 | View Available Posters | Click the Shop Now button from the Homepage | All available (52) posters are to be shown | PASS |
   

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T03 | FEATURE  | STEPS | EXPECTED | PASS |

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T04 | FEATURE  | STEPS | EXPECTED | PASS |

<details>
<summary>Screenshot</summary>
  
![image]TODO

</details>

----

## Manual Testing of TODO

### Epic: *Create and View*

This is broken down into the following
<details>
  <summary>User Stories</summary>

  ![image]TODO

  ![image]TODO

</details>

**User Tasks:**
1. Implement Navbar 
2. Demonstrate TODO
3. TODO

<details>
  <summary>TODO</summary>

  ![image]TODO

</details>

TODO

That the endpoints are protected - that only logged-in users can use the site

----


### Epic: *Register, Login and Logout*

This is broken down into the following
<details>
  <summary>User Story</summary>

   ![image]TODO
   
  
</details>

Criteria:
1. Both Username and Email is necessary to login
2. Verification by Email is mandatory
3. Minimum username length is 4 characters

**User Tasks:**
1. Update the Admin domain of the default site to **biblia.example.com**
2. Demonstrate that the user can Register using a username and password
3. Demonstrate that the user can Login to the site
4. Demonstrate that the user can Logout from the site


----
TODO EPIC - INCLUDE TESTING OF 404
## Conclusion

