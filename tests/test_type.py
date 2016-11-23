# -*- coding: utf-8 -*-

from thriftpy import load
from thriftpy.thrift import TType, TPayload


def test_set():
    s = load("type.thrift")

    assert s.Set.thrift_spec == {1: (TType.SET, "a_set", TType.STRING, True)}


class Struct(TPayload):
    thrift_spec = {
        1: (TType.MAP, 'tdict', (TType.I32, TType.I32), False),
        2: (TType.SET, 'tset', TType.I32, False),
        3: (TType.LIST, 'tlist', TType.I32, False),
    }

    default_spec = [
        ('tdict', {}),
        ('tset', set()),
        ('tlist', []),
    ]


# making an object with default values and then mutating the object should not
# change the default values

def test_mutable_default_dict():
    s1 = Struct()
    s1.tdict[1] = 2

    s2 = Struct()
    assert s2.tdict == {}


def test_mutable_default_list():
    s1 = Struct()
    s1.tlist.append(1)

    s2 = Struct()
    assert s2.tlist == []


def test_mutable_default_set():
    s1 = Struct()
    s1.tset.add(1)

    s2 = Struct()
    assert s2.tset == set()
