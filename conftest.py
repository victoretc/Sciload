import requests
import pytest
from faker import Faker

faker = Faker()

email = faker.email()
data = {"email": email ,"lang":"en","password":"Poiass098","password_confirmation":"Poiass098","profile_attributes":{"degree":"nonProfitOrganization","degree_category":"association"}}
@pytest.fixture
def new_user():
    response = requests.post('https://sciamp.com/auth' , json = data)
    return response
