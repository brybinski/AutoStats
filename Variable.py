import scipy.stats as stats
import numpy as np
from typing import *
import DataType


# Class of descriptive statistics that are calculated from given set
class Variable:
    type: DataType
    mean: Union[float, None]        # arythmetic mean
    sd: Union[float, None]          # standard deviation
    median: Union[float, None]      # median
    sem: Union[float, None]         # standard error of mean
    max: Union[int, float, None]    # maximal value
    min: Union[int, float, None]    # minimal value
    series: np.ndarray

    def __init__(self, data: Iterable, type: DataType):
        self.type = DataType

        series = np.ndarray([])

        for i in data:
            np.append(series, i)

        self.series = series


    def countProperties(self):
        if
