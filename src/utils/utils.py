import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import json

from ast import literal_eval


def dict_to_list(dict_str):
    """
    Parses a json dictionary into a list
    """
    try:
        genre_dict = literal_eval(dict_str)
        return list(genre_dict.values())
    except (ValueError, SyntaxError):
        return None
    
def str_to_list(str):
    """
    Parses a string which includes values seperated by commas and returns a list
    """
    try:
        return str.split(", ")
    except AttributeError:
        return None

# Helper functions for processing JSON-like columns
def str_to_list(entry):
    try:
        return [d['name'] for d in literal_eval(entry)]
    except:
        return []