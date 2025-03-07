import random

import pytest
from utils.api_helpers import APIClient
import allure

from utils.json_schema_validator import validate_json


@pytest.fixture(scope="module")
def client():
    return APIClient()


@allure.title("Verify if get all title response returns 200 with valid schema")
@pytest.mark.title
def test_get_title_list(client):
    response = client.get("/title")
    assert response.status_code == 200
    validate_json(data=response.json(), schema_file_name="title.json")


@allure.title("Verify if the user is able to data based on partial name of title")
@pytest.mark.title
def test_get_title_with_partial_name(client):
    response = client.get("/title").json()
    full_title = random.choice(response["titles"])
    partial_title = full_title[:-3]
    response = client.get(f"/title/{partial_title}")
    assert response.status_code == 200
    assert response.json()[0]["title"] == full_title


@allure.title(
    "Verify if the user is not able to data based on partial name of title with exact match"
)
@pytest.mark.title
def test_get_title_with_partial_name_exact_match(client):
    response = client.get("/title").json()
    partial_title = random.choice(response["titles"])[:-3]
    response = client.get(f"/title/{partial_title}:abs")
    assert response.status_code == 404


@allure.title("Verify if the user is gets 404 when searching for non-existent title")
@pytest.mark.title
def test_non_existent_title(client):
    response = client.get(f"/title/abcdefghijklmnopqrstuvwxyz")
    assert response.status_code == 404


@allure.title("Verify if the user is gets 405 when searching for non-existent title")
@pytest.mark.title
def test_non_existent_title(client):
    response = client.get(f"/title/abcdefghijklmnopqrstuvwxyz")
    assert response.status_code == 404
