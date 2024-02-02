from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from .base import Base


class Car(Base):
    """
    Пример модели
    Которой не нужны
    """

    __tablename__ = "example"

    id = Column(
        "id",
        Integer(),
        primary_key=True,
        nullable=False,
        info={"verbose_name": "Идентификатор"},
    )

    color = Column(
        "color",
        String(length=225),
        nullable=False,
        default="",
        server_default="",
        info={"verbose_name": "Цвет", "blank": True},
    )

    deleted: Column = Column(
        "deleted",
        Boolean(),
        server_default="false",
        default=False,
        info={"verbose_name": "Удален"},
    )

    organization_id: Column = Column(
        "organization_id",
        ForeignKey("organization.id"),
        nullable=True,
        info={"verbose_name": "Внешний ключ на объект типа Organization"},
    )
    organization = relationship(
        "Organization",
        foreign_keys="Car.organization_id",
        backref=backref("cars", lazy="dynamic"),
        info={"verbose_name": "Собственник", "display_field": "name"},
    )
