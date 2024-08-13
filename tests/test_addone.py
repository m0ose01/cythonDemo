from cythondemo.addone import addone

def test_addone():
    assert addone(5) == 6
