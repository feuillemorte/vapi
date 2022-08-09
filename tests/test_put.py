"""Tests for PUT requests to the API."""
import pytest
from helpers import utils


def test_put(pets_url, pet):
    """Checks that it's possible to change the existing item."""
    pet_id = pet.get("id")
    new_name = {"name": "Daizy"}
    response = utils.put(f"{pets_url}/id/{pet_id}", new_name)
    assert response.get("id") == pet_id
    assert response.get("name") == "Daizy"

    response = utils.get(f"{pets_url}/id/{pet_id}")
    assert response.get("name") == "Daizy"


def test_put_pet_empty_name(pets_url, pet):
    """Checks that it's not possible to change the item with an empty name."""
    pet_id = pet.get("id")
    new_name = {"name": ""}

    with pytest.raises(ValueError) as err:
        utils.put(f"{pets_url}/id/{pet_id}", new_name)

    assert err.match(r"The pet name is empty. Empty names are not allowed")


def test_put_pet_not_exists(pets_url):
    """Checks that it's not possible to change a not existed item."""
    new_name = {"name": "Luna"}

    with pytest.raises(ValueError) as err:
        utils.put(f"{pets_url}/id/999999", new_name)

    assert err.match(r"Item with the name 'Luna' does not exists")
