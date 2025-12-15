# Pytest-Playwright End-to-End Tests – Demo Web Shop

This repository contains **end-to-end (E2E) tests** written using **pytest-playwright** for the Demo Web Shop application, with a focus on shopping cart functionality.

🔗 **Application under test:** [https://demowebshop.tricentis.com/cart](https://demowebshop.tricentis.com)

---

## 📌 Project Overview

The purpose of this project is to validate key user flows in the Demo Web Shop using 
**Python-based browser automation**. The tests simulate real user interactions to 
ensure that critical cart features behave correctly across different browsers.

This project uses **pytest** as the test runner and **Playwright for Python** 
for browser automation.

---

## 🧪 Test Scope

The automated tests cover (but are not limited to):

* Navigating to the Demo Web Shop
* Adding products to the shopping cart
* Opening and validating the cart page
* Updating product quantities
* Removing products from the cart
* Verifying cart totals, messages, and UI elements
* Basic assertions for page content and behavior

---

## 🛠️ Tech Stack

* **Python** – Programming language
* **pytest** – Test framework
* **Playwright (Python)** – Browser automation library
* **pytest-playwright** – Pytest plugin for Playwright integration

---

## ⚙️ Prerequisites

Ensure the following are installed on your system:

* **Python 3.9+**
* **pip** (Python package manager)

## 🚀 Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\\Scripts\\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
playwright install
```

---

## ▶️ Running Tests

Run all tests in headless mode:

```bash
pytest
```

Run tests in headed (UI) mode:

```bash
pytest --headed
```

Run tests in a specific browser:

```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

Run a specific test file:

```bash
pytest tests/test_cart.py
```

---

## 📊 Test Reports

Pytest output is shown in the terminal by default.

To generate an HTML report (optional), install `pytest-html` and run:

```bash
pytest --html=report.html
```

---

## 🌐 Supported Browsers

Using pytest-playwright, tests can run on:

* Chromium
* Firefox
* WebKit

Browser selection is controlled via pytest command-line options.

---

## 🧹 Best Practices Followed

* Clear and descriptive test names
* Reusable pytest fixtures
* Independent and repeatable test cases
* Reliable Playwright locators
* No hard-coded waits (uses auto-waiting and assertions)

---

## ⚠️ Notes

* The Demo Web Shop is a **public demo application**, so product data or cart behavior may reset.
* Tests should not depend on persistent cart state between runs.

---

## 📄 License

This project is intended for **learning, practice, and demonstration purposes only**.

---

## 🙌 Author

Created as a **pytest-playwright E2E testing practice project**.
