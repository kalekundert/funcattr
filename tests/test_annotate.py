#!/usr/bin/env python3

from funcattr import annotate

def test_annotate_0():

    @annotate()
    def f():
        pass

    # No-op: just check that this doesn't raise.

def test_annotate_1():

    @annotate(a=1)
    def f():
        pass

    assert f.a == 1

def test_annotate_2():

    @annotate(a=1, b=2)
    def f():
        pass

    assert f.a == 1
    assert f.b == 2

