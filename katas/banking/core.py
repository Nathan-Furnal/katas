from decimal import Decimal
import datetime
from dataclasses import dataclass
import enum
from typing import Any

_AmountType = Decimal | int | float | tuple | str


class TransactionStatus(enum.Enum):
    SUCCESS = enum.auto()
    FAILURE = enum.auto()


@dataclass(frozen=True)
class Transaction:
    timestamp: datetime.datetime
    amount: Decimal
    status: TransactionStatus


class Account:
    def __init__(self) -> None:
        self._history: list[Transaction] = []
        self._balance: Decimal = Decimal(0)

    def _check_amount(self, amount: Any) -> Decimal:
        if isinstance(amount, Decimal):
            return abs(amount)
        elif isinstance(amount, (int, str, tuple, float)):
            return abs(Decimal(amount))
        else:
            raise ValueError(f"Not a valid decimal number: {amount}")

    def deposit(self, amount: _AmountType) -> None:
        amount = self._check_amount(amount)
        self._history.append(
            Transaction(
                timestamp=datetime.datetime.now(),
                amount=amount,
                status=TransactionStatus.SUCCESS,
            )
        )
        self._balance += amount

    def withdraw(self, amount: _AmountType) -> None:
        amount = self._check_amount(amount)
        timestamp = datetime.datetime.now()
        if amount > self._balance:
            self._history.append(
                Transaction(
                    timestamp=timestamp,
                    amount=-amount,
                    status=TransactionStatus.FAILURE,
                )
            )
        else:
            self._history.append(
                Transaction(
                    timestamp=timestamp,
                    amount=-amount,
                    status=TransactionStatus.SUCCESS,
                )
            )
            self._balance -= amount

    @property
    def balance(self) -> Decimal:
        return self._balance

    @property
    def history(self) -> tuple[Transaction, ...]:
        return tuple(self._history)
