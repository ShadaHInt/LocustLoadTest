from locust import HttpUser, task, between,tag
from session import APISession  # Import the session class
from tags import Tags  # Import the Tags class
class CRUDUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
     #  Initialize API session when the user starts.
        self.api = APISession(self.client)

    @tag(Tags.Create)
    @task(5)
    def create_user(self):
        self.api.create_user()

    @task(3)
    def read_users(self):
        self.api.read_users()

    @task(2)
    def update_user(self):
        self.api.update_user()

    @task(1)
    def delete_user(self):
        self.api.delete_user()   