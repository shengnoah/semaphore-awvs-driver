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
    print("==================")
    import awvs 
    ins = awvs.AWVS("testcase.com")
    print ins.domain
    print("*********")
    print(ins.send(1))
    ins.addTask(['lua.ren\n','candylab.net\n'])
    print("*********")
    assert 2==1+1          


@pytest.mark.scan
def test_5(setup_module):
    print('Test_5 called.\n')
    print("==================")
    #print('Test_5 called.')
    #print('*************.')
    #from jsonrpc.proxy import ServiceProxy
    #s = ServiceProxy('http://localhost:5000/json/') 
    #ret = s.myapp.autoscan('candylab.net')
    #print(ret['result'][0])
    #assert ret['result'][0] <> "abc"
    assert 1==1


@pytest.mark.scan
def test_6(setup_module):
    print('Test_6 called.\n')
    print("==================")
    import awvs 
    ins = awvs.AWVS("testcase.com")
    ins.auth({"email":"name", "password":"pwd"})
    print ins.domain
    assert 1==1



@pytest.mark.scan
def test_7(setup_module):
    print('Test_7 called.\n')
    print("==================")
    import awvs 
    ins = awvs.AWVS("test1.com")
    ins.auth({"email":"name", "password":"pwd"})
    ins.addTask(['lua.ren\n','candylab.net\n'])
    print ins.domain
    assert 1==1
