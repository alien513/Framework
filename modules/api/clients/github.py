import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    # ----------------- Individual Part ---------------------
    def get_emojis_status(self):
        r = requests.get(f"https://api.github.com/emojis")
        status_code = r.status_code

        return status_code

    def get_commits(self):
        r = requests.get(f"https://api.github.com/repos/alien513/Framework/commits")
        body = r.json()

        return body