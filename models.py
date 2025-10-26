from pydantic import BaseModel, Field

class Campaign(BaseModel):
    name: str
    budget: float = Field(gt=0, description="Budget must be greater than zero")
    description: str | None = None
