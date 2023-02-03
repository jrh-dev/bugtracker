from app.interface import DBI
import vcr

@vcr.use_cassette()
def test_get_bugs():
    dbi = DBI('http://127.0.0.1:8000')
    res = dbi.get_bugs()
    assert all(res['Bug ID'].values == ([1, 2, 3, 4, 5]))

@vcr.use_cassette()
def test_get_users():
    dbi = DBI('http://127.0.0.1:8000')
    res = dbi.get_users()
    assert all(res['User ID'].values == ([1, 2, 3]))