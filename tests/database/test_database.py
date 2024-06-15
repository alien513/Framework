import pytest
from modules.common.database import Database
from sqlite3 import OperationalError


@pytest.mark.database
def test_database_connection():
    db = Database()
    con = db.test_connection()

    assert con == True


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    assert users != None


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    prod_qnt = db.select_product_qnt_by_id(4)

    assert prod_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    big_num = 999
    db.insert_product(99, "test", "data", big_num)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()

    # Check that order quantity equals 1
    assert len(orders) == 1

    # Check data structure
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


# ----------------- Individual Part ---------------------
@pytest.mark.database
def test_product_insert_invalid_id_type():
    try:
        db = Database()
        db.insert_product("r", "new product", "desc", 113)
        res = True
    except OperationalError:
        res = False
    finally:
        assert res == False


@pytest.mark.database
def test_order_insert_valid_data():
    try:
        db = Database()
        db.insert_order(99, 1, 1)
        res = True
    except OperationalError:
        res = False
    finally:
        db.delete_order_by_id(99)
        assert res == True


@pytest.mark.database
def test_user_insert():
    db = Database()
    db.insert_user(3, "Elena", "New Street", "Lviv", "79070", "Ukraine")
    user = db.get_user_name_by_id(3)

    assert user[0][0] == "Elena"


@pytest.mark.database
def test_user_name_update():
    db = Database()
    db.update_user_name_by_id(3, "Olena")
    user = db.get_user_name_by_id(3)

    assert user[0][0] == "Olena"


@pytest.mark.database
def test_user_delete():
    db = Database()
    db.insert_user(99, "Olena", "New Street", "Lviv", "79070", "Ukraine")
    db.delete_user_by_id(99)
    qnt = db.get_user_name_by_id(99)

    assert len(qnt) == 0
