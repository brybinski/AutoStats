import scipy.stats as stats
import numpy as np
from typing import *
import DataType


# Class of descriptive statistics that are calculated from given set
class Variable:
    datatype: DataType
    mean: Union[float, None]      # arythmetic mean
    sd: Union[float, None]        # standard deviation
    median: Union[float, None]    # median
    sem: Union[float, None]       # standard error of mean
    max: Union[int, float, None]  # maximal value
    min: Union[int, float, None]  # minimal value
    iqr: Union[int, float, None]  # interquartile range
    mode: Any

    series: np.ndarray            # values

    def __init__(self, data: Iterable, datatype: DataType):
        self.datatype = datatype

        series = np.ndarray([])

        for i in data:
            np.append(series, i)

        self.series = series

    # TODO: CHECK IF DATA IS PROPER

    def countProperties(self):
        if self.datatype <= 1:
            self.sem = stats.sem(self.series)
            self.sd = float(np.std(self.series))
            self.max = float(np.max(self.series))
            self.min = float(np.min(self.series))
            self.iqr = stats.iqr(self.series)

        if self.datatype <= 2:
            self.median = float(np.mean(self.series))

        if self.datatype <= 3:
            self.mode = stats.mode(self.series)
