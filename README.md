# POMSelenium1
This a practice project for automating UI testing with Selenium and python

Website under test: https://www.saucedemo.com/v1/

---

## Tech stack 🔧:
  - Selenium ✅
  - Python ✅
  - Pytest (fixtures, setup, teardown) ✅
  - Page object model ✅
  - Report generation, pytest-html
  - Continuos Integration (Github Actions) ✅

## Continuos Integration (CI):
CI is configured using GitHub Actions.  
On every `push` to the `main` branch:

- Dependencies are installed
- Tests are executed using `pytest`
- You can view results in the **Actions** tab on GitHub

---

## ✅ Test Cases

| ID   | Name             | Description                                   |
|------|------------------|-----------------------------------------------|
| TC1  | Login Successful | User logs in with valid credentials           |
| TC2  | Login Failed     | Login attempt with invalid username/password  |
| TC3  | Login Blank      | Login attempt without entering credentials    |
| TC4  | Cart Sort        | Cart is correctly sorted by price (low to high) |
