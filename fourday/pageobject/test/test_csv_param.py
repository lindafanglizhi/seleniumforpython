import pytest
from util.get_csvdata import get_csv_data

test_login_data = get_csv_data("test_data1.csv")


@pytest.fixture()
def login_data( request):
    data=request.param
    return data

@pytest.mark.parametrize("login_data", test_login_data, indirect=True)
def test_login(login_data):
    username=login_data[0]
    print("用户名: %s "% username)


