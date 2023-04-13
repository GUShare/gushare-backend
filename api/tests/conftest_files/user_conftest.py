import pytest
from django.urls import reverse
from rest_framework.request import QueryDict

from api.models import User


@pytest.fixture
def valid_user_json(workplace_object):
    """
    This fixture provides a valid (according to the BookingSerializer) JSON dictionary.
    :param room_object:
    :param room_object:
    :return: Dict
    """
    email = "test_0@test.com"
    first_name = "Testfirstname"
    last_name = "Testlastname"
    password = "Test_password"
    favorite_workplaces = [workplace_object.id]

    data = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
        "favorite_workplaces": favorite_workplaces,
    }

    return data


@pytest.fixture
def valid_user_querydict(valid_user_json):
    """
    This fixture creates a QueryDict out of the valid_user_json.
    :param valid_user_json:
    :return: QueryDict
    """
    qdict = QueryDict("", mutable=True)
    qdict.update(valid_user_json)
    return qdict


@pytest.fixture
def create_n_user_objects():
    """
    This fixture resembles a user object factory.
    Since the users are distinguished by email the factory generates emails of the format
    test<int>@test.com.
    :return: Function
    """
    email = "test{}@test.com"
    first_name = "Testfirstname"
    last_name = "Testlastname"
    password = "Test_password"

    def create_users(start_stop):
        return [
            User.objects.create_user(
                email=email.format(i),
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            for i in range(*start_stop)
        ]

    return create_users


@pytest.fixture
def user_object(create_n_user_objects):
    """
    This fixture creates a user object which resembles the standart user.
    The standart user symbolize the user sending requests to the api within tests.
    :param create_n_user_objects:
    :return: User
    """
    return create_n_user_objects((1,))[0]


@pytest.fixture
def user_object_json(user_object):
    data = {
        "email": user_object.email,
        "first_name": user_object.first_name,
        "last_name": user_object.last_name,
        "password": user_object.password,
    }
    return data


@pytest.fixture
def diff_user_object(create_n_user_objects):
    """
    This fixture creates a user object which resembles a user which tries to exploit the system by accessing other
    users data.
    :param create_n_user_objects:
    :return:
    """
    return create_n_user_objects((1, 2))[0]


@pytest.fixture
def user_object_password():
    """
    This fixture provides the password of the standart user in clean, unhashed form. It will be needed in the following
    fixture to access the users jwt.
    We can not access the clean, unhashed passwort via the user_object fixture since it's retrieved in a hashed form
    from the database.
    :return: string
    """
    return "Test_password"


@pytest.fixture
def user_object_jwt(user_object, client, user_object_password):
    """
    This fixture retrieves the standart users valid JWT.

    :param user_object:
    :param client:
    :param user_object_password:
    :return: string
    """
    user_response = client.post(
        path=reverse("jwt-create"),
        data={"email": user_object.email, "password": user_object_password},
    )
    return user_response.data["access"]
