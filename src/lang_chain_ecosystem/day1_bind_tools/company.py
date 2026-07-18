from pydantic import BaseModel, Field


class Company(BaseModel):
    name: str = Field(description="The name of the company")
    ticker: str = Field(description="The ticker symbol of the company")
    founded_year: int = Field(description="The year the company was founded")
