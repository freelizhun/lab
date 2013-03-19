def setUp():
    print 'start'
def teardown():
    print 'finished'

def test():
    return 12
def test_numbers_3_4():
    assert test() == 12 

def test_strings_a_3():
    assert 'aaa' == 'aaa' 
