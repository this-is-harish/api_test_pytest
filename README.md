# Pytest Test Automation for PoetryDB API

## Pre-Condition
- Install Allure
- Python 3.12

## Requirements
Before running the tests, make sure you have the necessary dependencies installed. You can do this by running:
```bash
pip3 install -r requirements.txt
```
This will install all the required packages specified in the requirements.txt.

## Running the Tests
To run all test cases:
```bash
pytest tests/title_tests.py --alluredir=allure_results
```
To execute all the test cases, use the following command:
```bash
pytest tests/title_tests.py -m <tag> --alluredir=allure_results
```
This will run all tests and store the results in the `allure_results` directory.
This will filter and run only the test cases marked with `@pytest.mark.<tag>` and store the results in the `allure_results` directory.

## Generating HTML Report
After running the tests, you can generate an HTML report using the following command:
```bash
allure generate allure_results --output=allure_report
```

## Notes
Pushed `allure-report` folder for convenience for user to checkout the allure report. When using this repo in real time project, this folder should be added in  