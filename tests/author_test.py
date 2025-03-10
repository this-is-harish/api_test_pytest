import random

import allure
import pytest

from utils.api_helpers import APIClient
from utils.json_schema_validator import validate_json


@pytest.fixture(scope="module")
def client():
    return APIClient()


@allure.title("Verify if the user is able to data based on partial name of author")
@pytest.mark.author
def test_get_author_with_partial_name(client):
    response = client.get("/author").json()
    full_author_name = random.choice(response["authors"])
    partial_author_name = full_author_name[:-3]
    response = client.get(f"/author/{partial_author_name}")
    assert response.status_code == 200
    assert response.json()[0]["author"] == full_author_name


@allure.title(
    "Verify if the user is not able to data based on partial name of title with exact match"
)
@pytest.mark.author
def test_get_author_with_partial_name_exact_match(client):
    response = client.get("/author").json()
    partial_author_name = random.choice(response["authors"])[:-3]
    response = client.get(f"/author/{partial_author_name}:abs")
    assert response.status_code == 404


@allure.title("Verify if the user is gets 404 when searching for non-existent author")
@pytest.mark.author
def test_non_existent_author(client):
    response = client.get(f"/author/abcdefghijklmnopqrstuvwxyz")
    assert response.status_code == 404


@allure.title("Verify if get all author response returns 200 with valid schema")
@pytest.mark.author
def test_get_author_list(client):
    response = client.get("/author")
    assert response.status_code == 200
    validate_json(data=response.json(), schema_file_name="author.json")
