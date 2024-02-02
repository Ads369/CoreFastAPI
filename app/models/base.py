from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from geoalchemy2 import Geometry as _Geometry
from sqlalchemy.types import UserDefinedType
from sqlalchemy import func

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Geometry(_Geometry):
    from_text = "ST_GeomFromText"
    cache_ok = True

    def bind_expression(self, bindvalue):
        return getattr(func, self.from_text)(bindvalue, self.srid, type_=self)

# class Geometry(UserDefinedType):
#     def get_col_spec(self):
#         return "GEOMETRY"

#     def bind_expression(self, bindvalue):
#         return func.ST_GeomFromText(bindvalue, type_=self)

#     def column_expression(self, col):
#         return func.ST_AsText(col, type_=self)