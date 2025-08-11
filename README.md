# POMSelenium1
This a practice project for automating UI testing with Selenium and python

Website under test: https://www.saucedemo.com/v1/

---

## Tech stack 🔧:
  - Selenium ✅
  - Python ✅
  - Pytest (fixtures, setup, teardown) ✅
  - Page object model ✅
  - Report generation, pytest-html ✅
  - Continuos Integration (Github Actions) ✅

## Continuos Integration (CI):
CI is configured using GitHub Actions.  
On every `push` to the `main` branch:

- Dependencies are installed
- Tests are executed using `pytest`
- You can view results in the **Actions** tab on GitHub

## HTML report:
After the workflow run on a push, HTML report will be generated. Can find it in:
- Select workflow run
- Below in the "artifacts" section report can be downloaded
- Open the file, usually using google chrome to see the report.


---

## ✅ Test Cases

| ID   | Name                       | Description                                                        |
|------|----------------------------|--------------------------------------------------------------------|
| TC1  | Login Successful           | User logs in with valid credentials                                |
| TC2  | Login Failed               | Login attempt with invalid username or password                    |
| TC3  | Login Blank                | Login attempt without entering any credentials                     |
| TC4  | Logout                    | User logs in and successfully logs out                             |
| TC5  | Cart Sorting               | Products are sorted by price (low to high)                         |
| TC6  | Add Products               | Adds the first 3 products to the shopping cart                     |
| TC7  | Remove Product from Inventory | Removes products from the product listing page before adding to cart |
| TC8  | Remove Product from Cart   | Removes products from within the shopping cart page after adding  |
| TC9  | Checkout                  | Completes checkout and verifies that total price matches sum of products |

