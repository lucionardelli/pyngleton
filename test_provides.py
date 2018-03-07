#!/usr/bin/python3
# Copyright 2017 Ignacio Vizzo. All Rights Reserved.

from cnn_singleton import provide_vars, require_vars


@provide_vars('foo')
def provide_foo_var():
    return [1, 2]


@provide_vars('too')
def provide_too_var():
    return [3, 4]
