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


| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T01 | Register, Login, Logout | Using Allauth incorporate Register/Login/Logout functionality. | That the above User Tasks are accomplished. | PASS |


### Epic: *TODO*

This is broken down into the following

<details>
  <summary>User Stories</summary>

![image]TODO

</details>

**User Tasks:**

| Test No. | Feature        | Steps        | Expected Outcome  | Actual Outcome |
| ------------- | ------------- | -------------    | ------------- | ------------- |
| T02 | FEATURE  | STEPS | EXPECTED | PASS |

<details>
<summary>Screenshot</summary>

  ![image]TODO
  
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

## Conclusion

