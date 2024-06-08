import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""


@pytest.mark.check
def test_name(user):
    assert user.name == "Olena"


@pytest.mark.check
def test_surname(user):
    assert user.surname == "Kapustina"
