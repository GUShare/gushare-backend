import json

import pytest
from django.urls import reverse

from api.models import Booking, Building, Room, User, Workplace


class TestBuildingApiEndpoint:
    @pytest.mark.django_db
    def test_get_forbidden_without_jwt(self, client, building_object):
        """
        Test the detail Endpoint returns a 401 if no JWT is present.
        :param client:
        :param building_object:
        :return:
        """
        response = client.get(
            path=r"/buildings/",
            args=[building_object.id],
            content_type="application/json",
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_list_forbidden_without_jwt(self, client):
        """
        Test the list endpoint returns a 401 if no JWT is present.
        :param client:
        :return:
        """
        response = client.get(
            path="http://localhost:8000/buildings/",
            content_type="application/json",
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_create_forbidden_without_jwt(self, client, valid_building_json):
        """
        Test the create endpoint returns a 401 if no JWT is present.
        :param client:
        :param valid_building_json:
        :return:
        """
        response = client.post(
            path="http://localhost:8000/buildings/",
            data=json.dumps(valid_building_json),
            content_type="application/json",
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_put_forbidden_without_jwt(self, client, valid_building_json):
        """
        Test the PUT endpoint returns 401 if no JWT is present.
        :param client:
        :param valid_building_json:
        :return:
        """

        response = client.put(
            path="http://localhost:8000/buildings/",
            data=json.dumps(valid_building_json),
            content_type="application/json",
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_get_allowed(self, client, building_object, user_object_jwt):
        """
        Test the detail Endpoint returns a 200 if valid JWT is present.
        :param client:
        :param building_object:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.get(
            path=r"/buildings/",
            args=[building_object.id],
            content_type="application/json",
        )
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_list_allowed(self, client, user_object_jwt):
        """
        Test the list endpoint returns a 200 if valid JWT is present.
        :param client:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.get(
            path="http://localhost:8000/buildings/",
            content_type="application/json",
        )
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_put_not_allowed(
        self, client, valid_building_json, user_object_jwt
    ):
        """
        Test the PUT endpoint returns 405 if valid JWT is present.
        :param client:
        :param valid_building_json:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.put(
            path="http://localhost:8000/buildings/",
            data=json.dumps(valid_building_json),
            content_type="application/json",
        )
        assert response.status_code == 405

    @pytest.mark.django_db
    def test_patch_not_allowed(
        self, client, valid_building_json, user_object_jwt
    ):
        """
        Test the PATCH endpoint returns 405 if valid JWT is present.
        :param client:
        :param valid_building_json:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.patch(
            path="http://localhost:8000/buildings/",
            data=json.dumps(valid_building_json),
            content_type="application/json",
        )
        assert response.status_code == 405

    @pytest.mark.django_db
    def test_post_not_allowed(
        self, client, valid_building_json, user_object_jwt
    ):
        """
        Test the POST endpoint returns 405 if valid JWT is present.
        :param client:
        :param valid_building_json:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.post(
            path="http://localhost:8000/buildings/",
            data=json.dumps(valid_building_json),
            content_type="application/json",
        )
        assert response.status_code == 405


class TestRoomApiEndpoint:
    @pytest.mark.django_db
    def test_get_forbidden_without_jwt(self, client, room_object):
        """
        Test the detail Endpoint returns a 401 if no JWT is present.
        :param client:
        :param room_object:
        :return:
        """
        response = client.get(
            path=r"/rooms/",
            args=[room_object.id],
            content_type="application/json",
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_list_forbidden_without_jwt(self, client):
        """
        Test the list endpoint returns a 401 if no JWT is present.
        :param client:
        :return:
        """
        response = client.get(
            path="http://localhost:8000/rooms/",
            content_type="application/json",
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_create_forbidden_without_jwt(self, client, valid_room_json):
        """
        Test the create endpoint returns a 401 if no JWT is present.
        :param client:
        :param valid_room_json:
        :return:
        """
        response = client.post(
            path="http://localhost:8000/rooms/",
            data=json.dumps(valid_room_json),
            content_type="application/json",
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_put_forbidden_without_jwt(self, client, valid_room_json):
        """
        Test the PUT endpoint returns 401 if no JWT is present.
        :param client:
        :param valid_room_json:
        :return:
        """

        response = client.put(
            path="http://localhost:8000/rooms/",
            data=json.dumps(valid_room_json),
            content_type="application/json",
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_get_allowed(self, client, room_object, user_object_jwt):
        """
        Test the detail Endpoint returns a 200 if valid JWT is present.
        :param client:
        :param room_object:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.get(
            path=r"/rooms/",
            args=[room_object.id],
            content_type="application/json",
        )
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_list_allowed(self, client, user_object_jwt):
        """
        Test the list endpoint returns a 200 if valid JWT is present.
        :param client:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.get(
            path="http://localhost:8000/rooms/",
            content_type="application/json",
        )
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_put_not_allowed(self, client, valid_room_json, user_object_jwt):
        """
        Test the PUT endpoint returns 405 if valid JWT is present.
        :param client:
        :param valid_room_json:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.put(
            path="http://localhost:8000/rooms/",
            data=json.dumps(valid_room_json),
            content_type="application/json",
        )
        assert response.status_code == 405

    @pytest.mark.django_db
    def test_patch_not_allowed(self, client, valid_room_json, user_object_jwt):
        """
        Test the PATCH endpoint returns 405 if valid JWT is present.
        :param client:
        :param valid_room_json:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.patch(
            path="http://localhost:8000/rooms/",
            data=json.dumps(valid_room_json),
            content_type="application/json",
        )
        assert response.status_code == 405

    @pytest.mark.django_db
    def test_post_not_allowed(self, client, valid_room_json, user_object_jwt):
        """
        Test the POST endpoint returns 405 if valid JWT is present.
        :param client:
        :param valid_room_json:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.post(
            path="http://localhost:8000/rooms/",
            data=json.dumps(valid_room_json),
            content_type="application/json",
        )
        assert response.status_code == 405

    # todo: Test check booking endpoint


class TestDjoserCustomizing:
    @pytest.mark.django_db
    def test_delete_user_custom_serializer(
        self, user_object, user_object_jwt, client
    ):
        """
        Test if the user-delete view works with the specified custom UserSerializer.
        :param user_object:
        :param user_object_jwt:
        :param client:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        response = client.delete(
            path=reverse("user-me"),
            data={
                "email": user_object.email,
                "first_name": user_object.first_name,
                "last_name": user_object.last_name,
            },
        )
        assert response.status_code == 204
        assert not User.objects.filter(id=user_object.id).exists()

    @pytest.mark.django_db
    def test_put_user_custom_serializer(
        self, user_object, user_object_jwt, user_object_json, client
    ):
        """
        Test if the user/me/ PUT view works with the specified custom UserSerializer.
        :param user_object:
        :param user_object_jwt:
        :param client:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        put_data = user_object_json
        put_data["language"] = "de"
        response = client.put(
            path=reverse("user-me"),
            data=json.dumps(put_data),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert User.objects.get(id=user_object.id).language == "de"

    @pytest.mark.django_db
    def test_patch_user_custom_serializer(
        self, user_object, user_object_jwt, client
    ):
        """
        Test if the user/me/ PATCH view works with the specified custom UserSerializer.
        :param user_object:
        :param user_object_jwt:
        :param client:
        :return:
        """
        client.credentials(
            HTTP_AUTHORIZATION="Bearer {}".format(user_object_jwt)
        )
        put_data = {"language": "de"}
        response = client.patch(
            path=reverse("user-me"),
            data=json.dumps(put_data),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert User.objects.get(id=user_object.id).language == "de"
