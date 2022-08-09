"""Tests for POST requests to the API."""
import pytest
from helpers import utils


def test_add_pet(pets_url):
    """Checks that it's possible to create a new API item."""
    new_pet = {"name": "Luna"}
    response = utils.post(pets_url, new_pet)

    assert response.get("name") == "Luna"


def test_add_pet_empty_name(pets_url):
    """Checks that it's not possible to create a new item with empty name."""
    new_pet = {"name": ""}

    with pytest.raises(ValueError) as err:
        utils.post(pets_url, new_pet)

    assert err.match(r"The pet name is empty. Empty names are not allowed")


def test_add_pet_duplicate_name(pets_url, pet):
    """Checks that the API properly handles the duplicates."""
    new_pet = {"name": pet.get("name")}

    with pytest.raises(ValueError) as err:
        utils.post(pets_url, new_pet)

    assert err.match(f"Item with the name '{pet.get('name')}' is already exists")
