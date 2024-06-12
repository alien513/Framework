import pytest
from modules.api.clients.github import GitHub

class User:

    def __init__(self):
        self.name = None
        self.surname = None
        return None

    def create(self):
        self.name = "Olena"
        self.surname = "Kapustina"

    def remove(self):
        self.name = ""
        self.surname = ""

@pytest.fixture
def user():
    user = User()
    user.create()
    yield user
    user.remove()

@pytest.fixture
def github_api():
    api = GitHub()
    yield api