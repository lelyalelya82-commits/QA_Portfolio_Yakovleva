class TestProjectsAPI:

    # --- POST /api-v2/projects ---
    def test_create_project_positive(self, api_client):
        payload = {"title": "Новый проект для автотеста"}
        response = api_client.create_project(payload)

        assert response.status_code == 201
        assert "id" in response.json()

        # Очистка
        project_id = response.json()["id"]
        api_client.update_project(
            project_id,
            {"deleted": True}
        )

    def test_create_project_negative_no_title(self, api_client):
        response = api_client.create_project(
            {"description": "Без названия"}
        )
        assert response.status_code == 400

    # --- PUT /api-v2/projects/{id} ---
    def test_update_project_positive(self, api_client, created_project):
        project_id, _ = created_project
        new_payload = {"title": "Обновленное название"}

        response = api_client.update_project(project_id, new_payload)

        assert response.status_code == 200
        get_response = api_client.get_project(project_id)
        assert get_response.json()["title"] == new_payload["title"]

    def test_update_project_negative_not_found(self, api_client):
        invalid_id = "00000000-0000-0000-0000-000000000000"
        response = api_client.update_project(
            invalid_id,
            {"title": "Fail"}
        )
        assert response.status_code == 404

    # --- GET /api-v2/projects/{id} ---
    def test_get_project_positive(self, api_client, created_project):
        project_id, expected_payload = created_project
        response = api_client.get_project(project_id)

        assert response.status_code == 200
        assert response.json()["id"] == project_id
        assert response.json()["title"] == expected_payload["title"]

    def test_get_project_negative_not_found(self, api_client):
        invalid_id = "00000000-0000-0000-0000-000000000000"
        response = api_client.get_project(invalid_id)
        assert response.status_code == 404
