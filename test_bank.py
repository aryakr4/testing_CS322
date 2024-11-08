import pytest
from bank import Account

def test_initial_balance():
    a = Account("Alice", 0)
    b = Account("Bob", 100)
    assert a.get_balance() == 0
    assert b.get_balance() == 100

def test_deposit():
    a = Account("Alice", 0)
    b = Account("Bob", 100)
    assert a.deposit(50) == 50
    assert b.deposit(50) == 150

def test_withdraw():
    a = Account("Alice", 10)
    b = Account("Bob", 100)
    assert a.withdraw(10) == 0
    assert b.withdraw(50) == 50
    
def test_deposit_negative_amount():
    b = Account("Bob", 100)
    try:
        b.deposit(-50)
        assert False
    except ValueError as e:
        assert True
    except:
        assert False, "Wrong exception raised"

def test_withdraw_more_than_balance():
    a = Account("Alice", 0)
    b = Account("Bob", 100)
    try:
        a.withdraw(10)
        b.withdraw(150)
        assert False
    except ValueError as e:
        assert True
    except:
        assert False, "wrong exception raised"
    

def test_withdraw_negative_amount():
    a = Account("Alice", 0)
    b = Account("Bob", 100)
    try:
        a.withdraw(-10)
        b.withdraw(-150)
        assert False
    except ValueError as e:
        assert True
    except:
        assert False, "wrong exception raised"