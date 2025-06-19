import pytest
from unittest.mock import MagicMock
from app.app import app
from fastapi.testclient import TestClient

mock_session = MagicMock()


@pytest.fixture()
def mock_db():
    return MagicMock()
