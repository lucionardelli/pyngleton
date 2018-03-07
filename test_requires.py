#!/usr/bin/python3
# Copyright 2017 Ignacio Vizzo. All Rights Reserved.

from cnn_singleton import require_vars


@require_vars('foo')
def use_foo(foo):
    print("Printing foo var inside test_requires module ==> ", foo)


@require_vars('too')
def use_too(too):
    print("Printing too var inside test_requires module ==> ", too)


@require_vars('data_yaml')
def use_data_yaml(data_yaml):
    print("Printing data_yaml inside test_requires module ==> ", data_yaml)
