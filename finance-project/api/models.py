from pydantic import BaseModel, Field
from uuid import UUID


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 chars")


class BaseConfig:
    orm_mode = True


class AssetAdd(BaseModel):
    ticker: str = Field(description="The ticker symbol of the asset")


class AssetInfoBase(BaseModel):
    ticker: str
    name: str = Field(description="The name of the asset")
    country: str = Field(description="The country where the asset is located")

    class Config(BaseConfig):
        pass


class AssetInfoUser(AssetInfoBase):
    units: float = Field(description="Number of units of the asset that the user owns")


class AssetInfoPrice(AssetInfoBase):
    current_price: float = Field(description="Current price of the asset")
    currency: str = Field(description="The currency by which the price is expressed")
    today_low_price: float = Field(
        description="Lowest price of the asset during the current day"
    )
    today_high_price: float = Field(
        description="Highest price of the asset during the current day"
    )
    open_price: float = Field(
        description="Price of the asset at the beginning of the current day"
    )
    closed_price: float = Field(
        description="Price of the asset at the end of the previous day"
    )
    fifty_day_price: float = Field(
        description="Average price of the asset over the past fifty days"
    )


class UserInfo(BaseModel):
    id: UUID = Field(description="Universally unique identifier for the user")
    username: str
    stocks: list[AssetInfoBase] = Field(description="List of assets that the user owns")

    class Config(BaseConfig):
        pass
