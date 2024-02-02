from typing import Iterable, Sequence, Union

from pydantic import ValidationError

def convert_to_int_list(raw: Union[int, str, Sequence, Iterable, None]) -> tuple[int]:
    match raw:
        case None:
            return None
        case int():
            return tuple([raw])
        case str():
            value = raw.split(",")
            if len(value) == 1:
                return tuple([int(raw)])
            result = tuple(int(x) for x in value)
            return result
        case _:
            if isinstance(raw, Iterable):
                return tuple([int(x) for x in raw])
            else:
                raise ValidationError