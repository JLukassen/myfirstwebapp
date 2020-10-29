from datetime import datetime
import requests


def undo_snake_case_key(key: str) -> str:
    assert isinstance(key, str)
    new_key = key.split('__')
    int_key = '-'.join(new_key)
    new_key = int_key.split('_')
    return new_key[0] + ''.join([it.title() for it in new_key[1:]])


  