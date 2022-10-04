import requests
from locust import HttpUser, task, between
from faker import Faker

faker = Faker()
response_jokes = requests.get('https://api.chucknorris.io/jokes/random')
joke = response_jokes.json()['value']


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/marketplace")

    @task
    def new_user(self):
        email = faker.email()
        self.client.post('/auth', json={"email": email ,"lang":"en","password":"Poiass098","password_confirmation":"Poiass098","profile_attributes":{"degree":"nonProfitOrganization","degree_category":"association"}})
    
    
    @task
    def why_us(self):
        self.client.get("/whysciamp")

    @task
    def for_whom(self):
        self.client.get("/for/scientific-organizations")

    @task 
    def expert(self):
        self.client.get("/expert-council")


   
##    @task(3)
##    def view_items(self):
##        for item_id in range(10):
##           self.client.get(f"/item?id={item_id}", name="/item")
##            time.sleep(1)
##
##   def on_start(self):
##        self.client.post("/login", json={"username":"foo", "password":"bar"})