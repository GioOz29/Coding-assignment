import requests
import pytest
import requests_mock
from typing import List
from AppAPI import APIClient, DataService, Post, User, Geo, Address, Company

# Fixtures for setup and teardown
@pytest.fixture
def api_client() -> APIClient:
    """Fixture for APIClient initialization."""
    return APIClient(base_url="https://jsonplaceholder.typicode.com")

@pytest.fixture
def data_service(api_client: APIClient) -> DataService:
    """Fixture for DataService initialization."""
    return DataService(client=api_client)

# Mock response data
MOCK_POSTS = [
    {"userId": 1,
     "id": 1,
     "title": "Post 1",
     "body": "Body 1"},
    {"userId": 2,
     "id": 2,
     "title": "Post 2",
     "body": "Body 2"},
]

MOCK_USERS = [
    {"id": 1,
     "name": "User 1",
     "username": "user1",
     "email": "user1@example.com",
     "address": {
        "street": "123 Main St",
        "suite": "Apt. 1",
        "city": "Copenhagen",
        "zipcode": "55555-1234",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
            }
        },
        "phone": "1-333-333-4444 x12345",
        "website": "example1.org",
        "company": {
            "name": "Company User 1",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    {"id": 2,
     "name": "User 2",
     "username": "user2",
     "email": "user2@example.com",
     "address": {
        "street": "456 Main St",
        "suite": "Apt. 2",
        "city": "Copenhagen",
        "zipcode": "55555-5678",
        "geo": {
            "lat": "-43.9509",
            "lng": "-34.4618"
            }
        },
        "phone": "1-333-333-4444 x67890",
        "website": "example2.org",
        "company": {
            "name": "Company User 2",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chain"
        }
    },
]

# Test success scenarios for fetching posts
def test_get_posts_success(data_service: DataService, requests_mock: requests_mock.Mocker) -> None:
    requests_mock.get("https://jsonplaceholder.typicode.com/posts", json=MOCK_POSTS)
    posts: List[Post] = data_service.get_posts()
    assert len(posts) == 2
    assert posts[0].title == "Post 1"
    assert posts[1].user_id == 2

# Test success scenarios for fetching users
def test_get_users_success(data_service: DataService, requests_mock: requests_mock.Mocker) -> None:
    requests_mock.get("https://jsonplaceholder.typicode.com/users", json=MOCK_USERS)
    users: List[User] = data_service.get_users()
    assert len(users) == 2
    assert users[0].name == "User 1"
    assert users[1].email == "user2@example.com"

# Parametrized test for testing different endpoints
@pytest.mark.parametrize("endpoint, mock_data, expected_count", [
    ("posts", MOCK_POSTS, 2),
    ("users", MOCK_USERS, 2)
])
def test_fetch_data_parametrized(api_client: APIClient, requests_mock: requests_mock.Mocker, endpoint: str, mock_data: List[dict], expected_count: int) -> None:
    requests_mock.get(f"https://jsonplaceholder.typicode.com/{endpoint}", json=mock_data)
    data = api_client.fetch_data(endpoint)
    assert len(data) == expected_count

# Test failure scenarios
def test_fetch_data_failure(api_client: APIClient, requests_mock: requests_mock.Mocker) -> None:
    requests_mock.get("https://jsonplaceholder.typicode.com/posts", status_code=404)
    with pytest.raises(requests.exceptions.HTTPError):
        api_client.fetch_data("posts")

# Categorize tests using markers
@pytest.mark.integration
def test_integration_get_posts(data_service: DataService, requests_mock: requests_mock.Mocker) -> None:
    requests_mock.get("https://jsonplaceholder.typicode.com/posts", json=MOCK_POSTS)
    posts: List[Post] = data_service.get_posts()
    assert len(posts) == 2

@pytest.mark.unit
def test_unit_get_users(data_service: DataService, requests_mock: requests_mock.Mocker) -> None:
    requests_mock.get("https://jsonplaceholder.typicode.com/users", json=MOCK_USERS)
    users: List[User] = data_service.get_users()
    assert len(users) == 2
