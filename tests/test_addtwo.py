from cythondemo.addtwo import addtwo

def test_addtwo():
    assert addtwo(7) == 9
