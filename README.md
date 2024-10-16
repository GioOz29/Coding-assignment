# JSONPlaceholder API Client

This Python application interacts with JSONPlaceholder API, fetching and displaying from `/posts` and `/users` endpoints.The application is builted with Object-Oriented Programming (OOP) principles and includes static type checking with `Mypy`, as well as test automation using `pytest`.

## Contents

- Prerequisites
- Installation
- Running the application
- Running the test
- Checking for Type Errors (Mypy)
- Vewing the test coverage report
- GitHub Actions workflow

## Prerequisites

Before running the application, make sure you have installed:
* Python 3.10 or higher
* pip (python package manager)
* Git

## Installations

Follow these steps to set up the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/GioOz29/Coding-assignment.git
    cd Coding-assignment
    ```

2. Create a Python environment:
    ```bash
    python -m venv .venv
    ```

3. Activate the environment:
    * On macOS or Linux:
    ```bash
    source .venv/bin/activate
    ```

    * On Windows:
    ```bash
    .venv\Scripts\activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the application

To start the application interactions and interact with JSONPlaceholder API to fetch data, run:
```bash
python AppAPI.py
```

## Running the test

The application uses **pytest** and **requests-mock** to run the tests. To execute all the test from terminal, run:
```bash
pytest
```

To display the code coverage in the terminal, run:
```bash
pytest --cov=AppAPI --cov-report=term-missing
```

## Checking for _Type Errors_ with Mypy

To check if the code follows type savety rules and highlighting any type errors, run Mypy on the project with the following command:
```bash
mypy AppAPI.py
```

If your environment doesn't have Mypy already installed, run:
```bash
pip install mypy
```

## Vewing the test coverage report

The report will show the test coverage for each file and line of code. To generate a detailed coverage report and view it in the browser:
1. Run tests and generate an HTML report:
    ```bash
    pytest --cov=AppAPI --cov-report=xml
    ```

2. The coverage report will be saved in coverage.xml in the root directory of your project.

3. To view the XML coverage report, you can:
    * Open the coverage.xml file in a text editor or IDE that supports XML.
    * Use tools such as SonarQube, Coveralls, or Codecov for further processing or uploading the report to a CI/CD dashboard.

## GitHub Actions workflow

GitHub Actions is set up to automate the testing process and generate a coverage report. The workflow runs tests on every push to the master or main branch, as well as when manually triggered. Follow these steps to run the workflow:
1. Trigger Manually: You can manually run the workflow by:
    * Navigating to the "Actions" tab on your GitHub repository.
    * Selecting the "Run Pytest and Generate Coverage Report" workflow.
    * Clicking the "Run workflow" button.

2. On Push to master or main: The workflow will automatically be triggered on every push to the master or main branch.

### Viewing Artifacts and Coverage

Once the workflow completes, the test results and coverage report are generated.
You can view these reports by going to the "Actions" tab, selecting the specific workflow run, and downloading the artifacts.