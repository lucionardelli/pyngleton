#!/usr/bin/python3
# Copyright 2017 Ignacio Vizzo. All Rights Reserved.

from cnn_singleton import get_singleton_object
import test_provides
import test_requires
import test_yaml


if __name__ == "__main__":
    singleton = get_singleton_object()

    print("================================================================")
    singleton.use_foo()
    singleton.use_too()
    singleton.use_data_yaml()
    print("================================================================")
    print("Will print again foo var  now ==>", singleton['foo'])
    print("Will print again foo var  now ==>", singleton['too'])
    print("Will print data.yaml data now ==>", singleton['data_yaml'])
    print("================================================================")
