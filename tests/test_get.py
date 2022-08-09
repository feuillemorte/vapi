"""Tests for GET requests to the API."""
import pytest
from helpers import utils


def test_get_all_pets(all_pets):
    """Checks that the API returns pre-defined pets on a basic GET request."""
    names = ["Floof", "Snow"]
    for pet in all_pets:
        assert pet.get("name") in names


def test_get_pet_by_id(pet_floof, pet_snow):
    """Checks that pets can be accessed by id."""
    assert pet_floof.get("name") == "Floof"
    assert pet_snow.get("name") == "Snow"


def test_get_pet_by_id_empty(pets_url):
    """Checks the empty response from API if there is no such id."""
    assert utils.get(f"{pets_url}/id/99999999") == {}


@pytest.mark.parametrize("pet_name", ["Floof", "Snow"])
def test_get_pet_by_name(pets_url, pet_name):
    """Checks that pets can be accessed by name and it's case insensitive."""
    pet = utils.get(f"{pets_url}/name/{pet_name.lower()}")
    assert pet.get("name") == pet_name

    pet = utils.get(f"{pets_url}/name/{pet_name.upper()}")
    assert pet.get("name") == pet_name


def test_get_pet_by_name_not_exists(pets_url):
    """Checks the empty response from API if there is no such name."""
    pet = utils.get(f"{pets_url}/name/Molly")
    assert pet == {}


def test_get_openapi(api_url):
    """Checks that the API serves openapi definition json file."""
    response = utils.get(f"{api_url}/docs/openapi.json")
    assert response.get("info", {}).get("title") == "Small vulnerable API (DO NOT USE IN PRODUCTION)"
