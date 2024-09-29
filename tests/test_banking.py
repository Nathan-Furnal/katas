from katas.banking.core import Account, TransactionStatus
import pytest
from decimal import Decimal


@pytest.fixture
def account() -> Account:
    return Account()


def test_deposit_in_account(account):
    account.deposit(100)
    assert account.balance == 100


def test_withdraw_from_account(account):
    account.deposit(100)
    account.withdraw(50)
    assert account.balance == 50


def test_withdraw_with_insufficient_balance(account):
    account.deposit(100)
    account.withdraw(150)
    assert account.history[-1].status == TransactionStatus.FAILURE
    assert account.balance == 100


def test_balance_is_correct(account):
    account.deposit(100)
    expected = Decimal(100)
    assert account.balance == expected
    account.withdraw(32.4)
    expected -= Decimal(32.4)
    assert account.balance == expected
    account.deposit(27)
    expected += Decimal(27)
    assert account.balance == expected
    account.withdraw(Decimal(1 / 3))
    expected -= Decimal(1 / 3)
    assert account.balance == expected


def test_history_is_correct(account):
    account.deposit(11)
    account.withdraw(20)
    account.deposit(30)
    account.withdraw(20)
    assert [
        TransactionStatus.SUCCESS,
        TransactionStatus.FAILURE,
        TransactionStatus.SUCCESS,
        TransactionStatus.SUCCESS,
    ] == [t.status for t in account.history]
