from locust import HttpUser, task, between

class SumaUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_suma(self):
        self.client.post("/sumar", json={"a": 10, "b": 5})
