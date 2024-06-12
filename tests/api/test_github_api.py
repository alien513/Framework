import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 58
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# ----------------- Individual Part ---------------------
@pytest.mark.api
def test_emojis_status(github_api):
    r = github_api.get_emojis_status()
    assert r == 200


@pytest.mark.api
def test_commit_count(github_api):
    r = github_api.get_commits()
    assert len(r) == 3


@pytest.mark.api
def test_commit_author(github_api):
    r = github_api.get_commits()
    for i in range(len(r)):
        assert r[i]["commit"]["author"]["name"] == "alien513"