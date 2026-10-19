from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from app.database import get_db
from app.main import app


@pytest.mark.parametrize("available", [True, False])
def test_readiness(available):
    session = Mock()
    if not available:
        session.execute.side_effect = OperationalError(
            "SELECT 1", {}, Exception("private connection details")
        )
    app.dependency_overrides[get_db] = lambda: session
    try:
        with TestClient(app) as client:
            response = client.get("/ready")
        if available:
            assert response.status_code == 200
            assert response.json()["status"] == "ok"
        else:
            assert response.status_code == 503
            assert response.json() == {"detail": "Database unavailable"}
            assert client.get("/health").status_code == 200
    finally:
        app.dependency_overrides.pop(get_db, None)
