import os
import time
from typing import ClassVar, Optional

import redis
from redis_om import HashModel, Field


class Account(HashModel):
    _id_counter: ClassVar[int] = 100000
    account_number: str = Field(default_factory=lambda: Account._next_id(), index=True)
    account_type: str = Field(index=True)
    balance: float
    profile_id: str = Field(index=True)
    created_at: int = Field(default_factory=time.time, index=True)
    updated_at: str = Field(default_factory=time.time, index=True)

    class Meta:
        database = redis.Redis(
            host=os.environ.get("REDIS_URL"), port=13807, db=0,
            password=os.environ.get("REDIS_PWD"), decode_responses=True)

    @classmethod
    def _next_id(cls) -> str:
        cls._id_counter += 1
        return f"ACC{cls._id_counter:06d}"


# ----------------------------------------------------------------------------------------------------------
class ClientGoal(HashModel):
    _id_counter: ClassVar[int] = 100000
    goal_number: str = Field(default_factory=lambda: ClientGoal._next_id(), index=True)
    goal_type: str = Field(index=True)
    target_amount: float
    current_savings: float
    target_date: int = Field(index=True)
    profile_id: str = Field(index=True)
    created_at: int = Field(default_factory=time.time, index=True)
    updated_at: int = Field(default_factory=time.time, index=True)

    class Meta:
        database = redis.Redis(
            host=os.environ.get("REDIS_URL"), port=13807, db=0,
            password=os.environ.get("REDIS_PWD"), decode_responses=True)

    @classmethod
    def _next_id(cls) -> str:
        cls._id_counter += 1
        return f"CLG{cls._id_counter:06d}"


# ----------------------------------------------------------------------------------------------------------
class DividendPayout(HashModel):
    _id_counter: ClassVar[int] = 100000
    payout_number: str = Field(default_factory=lambda: DividendPayout._next_id(), index=True)
    account_number: str = Field(index=True)
    amount: float
    payment_date: int
    created_at: int = Field(default_factory=time.time, index=True)

    class Meta:
        database = redis.Redis(
            host=os.environ.get("REDIS_URL"), port=13807, db=0,
            password=os.environ.get("REDIS_PWD"), decode_responses=True)

    @classmethod
    def _next_id(cls) -> str:
        cls._id_counter += 1
        return f"DVP{cls._id_counter:06d}"


# ----------------------------------------------------------------------------------------------------------
class Investment(HashModel):
    _id_counter: ClassVar[int] = 100000
    inv_number: str = Field(default_factory=lambda: Investment._next_id(), index=True)
    account_number: str = Field(index=True)
    investment_type: str = Field(index=True)
    symbol: str = Field(index=True)
    quantity: float
    purchase_price: float
    current_price: float
    purchase_date: int
    created_at: int = Field(default_factory=time.time, index=True)
    updated_at: int = Field(default_factory=time.time, index=True)

    class Meta:
        database = redis.Redis(
            host=os.environ.get("REDIS_URL"), port=13807, db=0,
            password=os.environ.get("REDIS_PWD"), decode_responses=True)

    @classmethod
    def _next_id(cls) -> str:
        cls._id_counter += 1
        return f"INV{cls._id_counter:06d}"


# ----------------------------------------------------------------------------------------------------------
class Transaction(HashModel):
    _id_counter: ClassVar[int] = 100000
    txn_number: str = Field(default_factory=lambda: Transaction._next_id(), index=True)
    account_number: str = Field(index=True)
    amount: float
    txn_type: str = Field(index=True)
    description: Optional[str]
    created_at: int = Field(default_factory=time.time, index=True)

    class Meta:
        database = redis.Redis(
            host=os.environ.get("REDIS_URL"), port=13807, db=0,
            password=os.environ.get("REDIS_PWD"), decode_responses=True)

    @classmethod
    def _next_id(cls) -> str:
        cls._id_counter += 1
        return f"TXN{cls._id_counter:06d}"


# ----------------------------------------------------------------------------------------------------------
class StoreSession(HashModel):
    user_id: str = Field(index=True)
    profile_picture_url: Optional[str]
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    profile_type: str = Field(index=True)
    email: str = Field(index=True)

    class Meta:
        database = redis.Redis(
            host=os.environ.get("REDIS_URL"), port=13807, db=0,
            password=os.environ.get("REDIS_PWD"), decode_responses=True)
