from hexbytes import HexBytes
from decimal import *


def dict_to_json_serializable(dictval):
    for k in dictval:
        v = dictval[k]
        if type(v) == bytes or type(v) == HexBytes:
            dictval[k] = v.hex()
        elif type(v) == dict:
            dictval[k] = dict_to_json_serializable(v)
        elif type(v) == list:
            dictval[k] = list_to_json_serializable(v)
        elif type(v).__name__ == "AttributeDict":
            dictval[k] = dict_to_json_serializable(dict(v))
    return dictval


def list_to_json_serializable(listval):
    for k in range(0, len(listval)):
        v = listval[k]
        if type(v) == bytes or type(v) == HexBytes:
            listval[k] = v.hex()
        elif type(v) == dict:
            listval[k] = dict_to_json_serializable(v)
        elif type(v).__name__ == "AttributeDict":
            listval[k] = dict_to_json_serializable(dict(v))
        elif type(v) == list:
            listval[k] = list_to_json_serializable(v)
    return listval


def to_raw_units(_qty, _decimals):
    return int(_qty * (10 ** _decimals))


def from_raw_units(_qty, _decimals):
    return round(_qty / (10 ** _decimals), _decimals)

