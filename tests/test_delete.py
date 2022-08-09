"""Tests for DELETE requests to the API."""
import pytest
from helpers import utils


def test_delete(pets_url, pet):
    """Checks that it's possible to delete an item."""
    pet_id = pet.get("id")
    utils.delete(f"{pets_url}/id/{pet_id}")

    response = utils.get(f"{pets_url}/id/{pet_id}")
    assert not response


def test_delete_pet_not_exists(pets_url):
    """Checks the message if there is an attempt to delete a non-existing item."""
    with pytest.raises(ValueError) as err:
        utils.delete(f"{pets_url}/id/999999")

    assert err.match(r"Item does not exists")
