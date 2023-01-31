
## load modules and files
import pandas as pd
import numpy as np
import pickle

input_path = "data/titanic.csv"
##

def load_data(pathtofile):
    return pd.read_csv(pathtofile)

data = load_data(input_path)

##
data.columns
##

import matplotlib.pyplot as plt
data.Age.hist()
plt.show()

