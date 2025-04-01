import json

class APISession:
    def __init__(self, client):
        self.client = client
        self.user_id = None

    def create_user(self):
        # Create a user and store the user ID. 
        response = self.client.post("/api/users", json={"name": "John Doe", "job": "Developer"})
        if response.status_code == 201:
            self.user_id = response.json().get("id")
            print(f"User created with ID: {self.user_id}")

        return response

    def read_users(self):
        # Fetch user list.
        response = self.client.get("/api/users?page=2")

        # Assertion: Check that the status code is 200 (OK)
        assert response.status_code == 200, f"Failed to fetch users: {response.status_code}"

        return response

    def update_user(self):
        #  Update an existing user. 
        if self.user_id:
            response = self.client.put(f"/api/users/{self.user_id}", json={"name": "Jane Doe", "job": "Manager"})

            # Assertion: Check that the status code is 200 (OK)
            assert response.status_code == 200, f"Failed to update user: {response.status_code}"
            
            print(f"User updated with ID: {self.user_id}")

            return response

    def delete_user(self):
        # Delete the created user. 
        if self.user_id:
            response = self.client.delete(f"/api/users/{self.user_id}")
            print(f"User deleted with ID: {self.user_id}")
            self.user_id = None

            return response