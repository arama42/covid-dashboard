import pandas as pd
import json
import ast


def validate(data):
    return data if data else "N/A"


def todict(data):
    #data_dict = json.loads(data.replace("'", '"'))
    #data_dict = eval(data)
    #data_dict = {k: v for (k, v) in [s.split(':') for s in data.strip('{}').split(', ')]}
    return data


