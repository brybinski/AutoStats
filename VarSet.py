import pandas as pd
import numpy as np
import pyreadstat
import scipy as sp
from typing import *
from Variable import Variable
from Constants import Constants


class VarSet:
    va_list: Dict[str, Variable]
    name: str

    def __init__(self, df, name=None):
        if name is None:
            self.name = "VAR"+str(Constants.varcounter)
            Constants.varcounter += 1
        else:
            self.name = name


path = 'D:\\pythonProject1\\kns.sav'
df, metadata = pyreadstat.read_sav(path, apply_value_formats=False)

print(df)
