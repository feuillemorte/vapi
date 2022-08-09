"""Fixture for integration tests."""
import subprocess

import pytest

from tests.helpers import utils

API_URL = "http://127.0.0.1:5000"
PETS_URL = f"{API_URL}/pets"
FLOOF_PET_URL = f"{PETS_URL}/id/1"
SNOW_PET_URL = f"{PETS_URL}/id/2"


@pytest.fixture
def api_url():
    """Returns api url."""
    return API_URL


@pytest.fixture
def pets_url():
    """Returns url for pets api endpoint."""
    return PETS_URL


@pytest.fixture(scope="function", autouse=True)
def flask():
    """Runs flask api for every test and kill it after the test execution."""
    pid = subprocess.check_output("bash ./start.sh", shell=True)
    yield
    subprocess.check_output(f"kill {int(pid)}", shell=True)


@pytest.fixture
def all_pets():
    """Returns all pets from the API."""
    return utils.get(PETS_URL)


@pytest.fixture
def pet_floof():
    """Return the pre-defined Floof pet (id 1)."""
    return utils.get(FLOOF_PET_URL)


@pytest.fixture
def pet_snow():
    """Return the pre-defined Snow pet (id 2)."""
    return utils.get(SNOW_PET_URL)


@pytest.fixture
def pet():
    """Adds a new pet to the API."""
    new_pet = {"name": "Luna"}
    return utils.post(PETS_URL, new_pet)
