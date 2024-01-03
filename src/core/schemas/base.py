from humps.main import camelize
from pydantic import BaseModel as PydanticModel


def to_camel(string: str) -> str:
    return camelize(string)

class BaseModel(PydanticModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True