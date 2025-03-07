# Pytest Test Automation for PoetryDB API

## Pre-Condition
- Install Allure
- Python 3.12
- Base URL should be added in [.env](.env), if left empty it'll pick https://poetrydb.org/ automatically

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

## Disclaimer
The `allure-report` folder has been pushed to this repository for the convenience of users who wish to quickly view the Allure report. However, in a real-time project, this folder should be excluded from version control. 

To do so, ensure that it is added to the  [.gitignore](.gitignore) to prevent the report from being tracked and committed to the repository. Or just un-comment the last line

## Results
| Scenario Name                                                                            | Test Status | Duration  |
|:-----------------------------------------------------------------------------------------|-------------|-----------|
| Verify if get all author response returns 200 with valid schema                         | Passed      | 1s 099ms  |
| Verify if get all title response returns 200 with valid schema                          | Passed      | 716ms     |
| Verify if the user is able to data based on partial name of author                      | Passed      | 968ms     |
| Verify if the user is able to data based on partial name of title                       | Passed      | 968ms     |
| Verify if the user gets 404 when searching for non-existent author                      | Failed      | 321ms     |
| Verify if the user gets 405 when searching for non-existent title                       | Failed      | 328ms     |
| Verify if the user is not able to data based on partial name of title with exact match  | Failed      | 1s 166ms  |
| Verify if the user is not able to data based on partial name of author with exact match | Failed      | 321ms     |

## Expected Output
- Status Code
- JSON schema
- Retrieved Data is correct (from search filters)
