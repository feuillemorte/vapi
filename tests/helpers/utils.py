"""Helpers for tests."""
import requests


def get(url):
    """Sends GET request to the API."""
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        return response.json()
    raise ValueError(f"Got an error from the API: {response.json()}")


def post(url, data):
    """Sends POST request to the API."""
    response = requests.post(url, json=data)
    if response.status_code == requests.codes.created:
        return response.json()
    raise ValueError(f"Got an error from the API: {response.json()}")


def put(url, data):
    """Sends PUT request to the API."""
    response = requests.put(url, json=data)
    if response.status_code == requests.codes.OK:
        return response.json()
    raise ValueError(f"Got an error from the API: {response.json()}")


def delete(url):
    """Sends DELETE request to the API."""
    response = requests.delete(url)
    if not response.status_code == requests.codes.no_content:
        raise ValueError(f"Got an error from the API: {response.json()}")
