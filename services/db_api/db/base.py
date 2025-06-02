
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, DeclarativeBase
from sqlalchemy.sql.annotation import Annotated

class BaseModel(DeclarativeBase):
    pass


# intpk = Annotated[int, mapped_column(primary_key=True)]