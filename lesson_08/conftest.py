import pytest
from api_client import YougileApi


@pytest.fixture
def api_client():
    return YougileApi()


@pytest.fixture
def created_project(api_client):
    payload = {"title": "Test Project for Deletion"}
    response = api_client.create_project(payload)

    if response.status_code != 201:
        pytest.fail(
            f"Не удалось создать проект. Ответ: {response.text}"
        )

    project_id = response.json()["id"]

    yield project_id, payload

    api_client.update_project(
        project_id,
        {"deleted": True}
    )
