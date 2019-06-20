# -*- coding:utf-8 -*-
import pytest
@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_function called.")
        request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
        print('setup_function called.')

@pytest.fixture(scope='module')
def setup_module(request):
    def teardown_module():
        print("teardown_module called.")
        request.addfinalizer(teardown_module)
        print('setup_module called.')

@pytest.mark.website
def test_1(setup_function):
    print('Test_1 called.')
    print('*************.')

@pytest.mark.website
def test_2(setup_module):
    print('Test_2 called.')

@pytest.mark.website
def test_3(setup_module):
    print('Test_3 called.')
    assert 2==1+1          


@pytest.mark.scan
def test_4(setup_module):
    print('Test_4 called.\n')
    import awvs
    ins = awvs.AWVS("test.com")
    
    print ins.domain
    print ins.send(5)
    assert 2==1+1          


