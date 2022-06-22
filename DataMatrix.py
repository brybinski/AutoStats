import pandas as pd
import numpy as np
import pyreadstat
import scipy as sp
from typing import *
from VarSet import VarSet
from Constants import Constants
import scipy.io as sio


class DataMatrix:
    df: pd.DataFrame
    history: list[str]
    name: str

    def print_history(self):
        for i in self.history:
            print(i)

    def splitByColumn(self):
        raise NotImplementedError

    def removeNANs(self):
        raise NotImplementedError

    def toVarSet(self):
        return VarSet(self.df, self.name)

    def __init__(self, df: pd.DataFrame, name=None):
        if name is None:
            self.name = 'DataMatrix' + str(Constants.dfCounter)
            Constants.dfCounter += 1
        else:
            self.name = name

        self.df = df


def readSPSS(path) -> DataMatrix:
    df, metadata = pyreadstat.read_sav(path, apply_value_formats=False)
    return DataMatrix(df)


x = readSPSS('D:\\pythonProject1\\kns.sav')

