###############################
# First test
###############################

# def test_check_math():
#     assert 7 * 7 == 49

# def test_check_78():
#     assert 7 * 8 ==56

##############################
# Fixtures
##############################
import pytest

@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.check
def test_name(user):
    assert user.name == "Olena"

@pytest.mark.check
def test_surname(user):
    assert user.surname == "Kapustina"