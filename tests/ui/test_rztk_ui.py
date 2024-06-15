from modules.ui.page_objects.rztk_cart_page import SignInPage
import pytest


@pytest.mark.ui
def test_add_to_cart():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    assert sign_in_page.check_add_to_cart()
    sign_in_page.close()
