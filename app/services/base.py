from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar


_AdapterT = TypeVar('_AdapterT')

class BaseService(ABC):
    @abstractmethod
    def process(self, *args: Any, **kwargs: Any) -> Any:
        ...


class BaseAdapterService(BaseService, ABC, Generic[_AdapterT]):
    _adapter: _AdapterT

    def __init__(self, adapter: _AdapterT):
        self._adapter = adapter


class MultiAdapterService(BaseService, ABC):
    _adapters: dict[str,Any]

    def __init__(self, adapters: dict[str,Any]):
        self._adapters = adapters
