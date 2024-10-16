import requests
from typing import List, Dict, Any

# API client class for interacting with the JSONPlaceholder API
class APIClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch_data(self, endpoint: str) -> List[Dict[str, Any]]:
        """Fetch data from the provided endpoint."""
        response = requests.get(f"{self.base_url}/{endpoint}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status() # This will raise HTTPError on 404 and other non-2xx codes
            return [] # MyPy check for errors

# Post class representing a blog post from the API
class Post:
    def __init__(self, post_id: int, user_id: int, title: str, body: str) -> None:
        self.user_id = user_id
        self.post_id = post_id
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return f"Post(user_id={self.user_id},\n id={self.post_id},\n title={self.title},\n body={self.body})"

# Geo sub-subclass of User, subclass of Address
class Geo:
    def __init__(self, lat: str, lng: str) -> None:
        self.lat = lat
        self.lng = lng
        
    def __repr__(self) -> str:
        return f"(lat={self.lat},\n\t lng={self.lng})"
        
# Address subclass of User
class Address:
    def __init__(self, street: str, suite: str, city: str, zipcode: str, geo: Geo) -> None:
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo
        
    def __repr__(self) -> str:
        return f"(street={self.street},\n\t suite={self.suite},\n\t city={self.city},\n\t zipcode={self.zipcode},\n\t geo={self.geo})"
        
# Company subclass of User
class Company:
    def __init__(self, name: str, c_frase: str, bs: str) -> None:
        self.name = name
        self.c_frase = c_frase
        self.bs = bs
   
    def __repr__(self) -> str:
        return f"(name={self.name},\n\t catchPhrase={self.c_frase},\n\t bs={self.bs})"

# User class representing a user from the API
class User:
    def __init__(self, user_id: int, name: str, username: str, email: str, address: Address, phone: str, website: str, company: Company) -> None:
        self.user_id = user_id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def __repr__(self) -> str:
        return f"User(id={self.user_id},\n name={self.name},\n username={self.username},\n email={self.email},\n address={self.address},\n phone={self.phone},\n website={self.website},\n company={self.company})"

# DataService class to handle the data processing and API fetching
class DataService:
    def __init__(self, client: APIClient) -> None:
        self.client = client

    def get_posts(self) -> List[Post]:
        """Fetches a list of posts from the API and returns Post objects."""
        posts_data: List[Dict[str, Any]] = self.client.fetch_data("posts")
        return [Post(post['id'], post['userId'], post['title'], post['body']) for post in posts_data]

    def get_users(self) -> List[User]:
        """Fetches a list of users from the API and returns User objects."""
        users_data: List[Dict[str, Any]] = self.client.fetch_data("users")
        return [self._create_user(user) for user in users_data]
    
    def _create_user(self, user_data: Dict[str, Any]) -> User:
        """Helper function to create a User object from raw API data."""
        geo = Geo(user_data['address']['geo']['lat'], user_data['address']['geo']['lng'])
        address = Address(user_data['address']['street'], user_data['address']['suite'], user_data['address']['city'], user_data['address']['zipcode'], geo)
        company = Company(user_data['company']['name'], user_data['company']['catchPhrase'], user_data['company']['bs'])
        return User(user_data['id'], user_data['name'], user_data['username'], user_data['email'], address, user_data['phone'], user_data['website'], company)

# Main function to fetch and print data
def main() -> None:
    # Initialize API client
    api_client: APIClient = APIClient(base_url="https://jsonplaceholder.typicode.com/")

    # Initialize data service
    data_service: DataService = DataService(client=api_client)

    # Fetch posts and print the first one
    print("Fetching Posts...")
    posts: List[Post] = data_service.get_posts()
    print(posts[0])

    # Fetch users and print the first one
    print("\nFetching Users...")
    users: List[User] = data_service.get_users()
    print(users[0])

if __name__ == "__main__":
    main()
