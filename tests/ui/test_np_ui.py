from modules.ui.page_objects.np_search_ttn_page import SignInPage
import pytest


@pytest.mark.ui
def test_search_ttn():
    test_ttn = "12345678901234"
    test_title = "Трекінг Нова пошта - відстежити посилку, відслідковувати ТТН"

    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.search_ttn(test_ttn)
    assert sign_in_page.check_title(test_title)
    sign_in_page.close()
