import os
import time
from typing import ClassVar, Optional

import redis
from redis_om import Field, JsonModel


class Account(JsonModel):
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
        redis_conn = cls.Meta.database
        next_id = redis_conn.incr('account_number_counter')
        return f"ACC{next_id:06d}"


# ----------------------------------------------------------------------------------------------------------
class ClientGoal(JsonModel):
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
        redis_conn = cls.Meta.database
        next_id = redis_conn.incr('goal_number_counter')
        return f"CLG{next_id:06d}"


# ----------------------------------------------------------------------------------------------------------
class DividendPayout(JsonModel):
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
        redis_conn = cls.Meta.database
        next_id = redis_conn.incr('payout_number_counter')
        return f"DVP{next_id:06d}"


# ----------------------------------------------------------------------------------------------------------
class Investment(JsonModel):
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
        redis_conn = cls.Meta.database
        next_id = redis_conn.incr('inv_number_counter')
        return f"INV{next_id:06d}"


# ----------------------------------------------------------------------------------------------------------
class Transaction(JsonModel):
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
        redis_conn = cls.Meta.database
        next_id = redis_conn.incr('txn_number_counter')
        return f"TXN{next_id:06d}"


# ----------------------------------------------------------------------------------------------------------
class StoreSession(JsonModel):
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
