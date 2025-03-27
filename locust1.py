from locust import HttpUser, task, between

class CRUDUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between tasks (1 to 3 seconds)
    user_id = None

    @task(2)  # Create User (POST)
    def create_user(self):
        response = self.client.post("/api/users", json={"name": "John Doe", "job": "Developer"})
        if response.status_code == 201:
            self.user_id = response.json().get("id")
            print(f"User created with ID: {self.user_id}")

    @task(4)  # Read Users (GET)
    def read_users(self):
        self.client.get("/api/users?page=2")

    @task(2)  # Update User (PUT)
    def update_user(self):
        if self.user_id:
            self.client.put(f"/api/users/{self.user_id}", json={"name": "Jane Doe", "job": "Manager"})
            print(f"User updated with ID: {self.user_id}")

    @task(1)  # Delete User (DELETE)
    def delete_user(self):
        if self.user_id:
            self.client.delete(f"/api/users/{self.user_id}")
            print(f"User deleted with ID: {self.user_id}")
            self.user_id = None
