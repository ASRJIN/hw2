import sqlite3
import pandas as pd
import numpy as np

def max_val(input_list):
    """
    :param input_list: a nested list
    :return: the maximum value of each inner list
    """
    pass


# Update the value of the `Division` column to Hardware for the employee whose ID=3
sql_query_1 = " "

# Delete the entry for all employee whose STARS = 3
sql_query_2 = " "

def train_model():
    np.random.seed(42)
    utility = pd.read_csv('https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/utilities.csv',
                          index_col=0)

