#!/usr/bin/python3
# Copyright 2017 Ignacio Vizzo. All Rights Reserved.
import yaml
from cnn_singleton import provide_vars


@provide_vars('data_yaml')
def load_data_yaml():
    try:
        print("Opening default data file data.yaml from log folder")
        f = open('data.yaml', 'r')
        data_yaml = yaml.load(f)
    except:
        print("Error opening data yaml file...")
        quit()
    return data_yaml
