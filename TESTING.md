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
This test was performed before the authentication profile was added.

<details>
  <summary>Lighthouse Report</summary>

    TODO

</details>

## Additional Testing Comments
+ Carried out tests of the program on both the local terminal and the Code Institute Heroku terminal.
+ Chrome DevTools was used throughout the development process for testing purposes.
+ Added Custom [404]TODO and [500]TODO pages just in case such errors occur.
  
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

User Tasks:
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

Once the account is registered change the url ending to **/admin/account/emailaddress/**

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

User Tasks:
1. When the user selects the *Shop Now* option, the user can see all available posters
2. User has the option to view particular *categories* of posters using drop-down menus
3. That all the above work correctly with responsiveness on different sized media

In this online shop there are *52 posters* available.

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
| T02 | View Available Posters | Click the Shop Now button from the Homepage | All available (52) posters are to be shown | PASS |


<details>

<summary></summary>

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
   

### Epic: Search for Posters

<details>
  <summary>User Story</summary>
   
![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/2d721ad9-5bd9-4fef-966d-85c6f0ec36d2)

</details>

**User Tasks:**
1. A successful search consists of whether the search term appears in the Poster Name or the Poster Description
2. Enter the search parameters via the URL to perform a search e.g. */posters/?query=**saul*** to bring up all the posters with the search term *saul* in them
3. Use the Searchbar to enter the search term
4. Both methods should show identical results
5. Suitable messages when a null string is entered or null search results


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T0x | Search For Posters By Name | Either by using the URL or Searchbar test various search terms| Any posters with matching names displayed | PASS |

<details>
<summary>/posters/?query=saul</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b3aaa659-f1c7-458a-be69-fbd421088da0)
  
</details>

<details>
<summary>/posters/?query=ethio</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5c31210c-322d-40a0-a24d-3f6502d01575)
  
</details>


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T0x | Search For Posters By Description | Either by using the URL or Searchbar test various search terms| Any posters with matching descriptions displayed | PASS |

<details>
<summary>/posters/?query=BED matches the descriptions of these 2 posters</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/fcca6530-f744-4103-832a-c2c1fcaef91a)

View the description then *used CTRL-F and 'bed' to highlight that the searches were successful*

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/5e59d029-1f07-484e-896f-83f2591af1dc)
 
</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T0x | Null Search Toast/Message Displayed | Enter nothing in the Searchbar | A suitable message ought to be displayed | PASS |

<details>
<summary>Null Entry in Searchbar</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/e8160d1b-ba71-44c3-aa54-f54fcffbca2f)

</details>

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T0x | Nonexistent Search Toast/Message Displayed | Enter a search term in the Searchbar that does not exist in any of the posters | A suitable message ought to be displayed | PASS |

<details>
<summary>/posters/?query=HELLO</summary>

![image](https://github.com/DelroyGayle/Biblia-Posters-PP5/assets/91061592/b93c8664-ba08-439a-a9b7-b392a15dc771)
  
</details>


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

User Tasks:
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

User Tasks:
1. Update the Admin domain of the default site to **biblia.example.com**
2. Demonstrate that the user can Register using a username and password
3. Demonstrate that the user can Login to the site
4. Demonstrate that the user can Logout from the site


----

## Conclusion

