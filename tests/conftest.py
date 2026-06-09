from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_data


@pytest.fixture(autouse=True)
def reset_activities():
    original = deepcopy(activities_data)
    try:
        yield
    finally:
        activities_data.clear()
        activities_data.update(original)


@pytest.fixture
def client():
    return TestClient(app)
