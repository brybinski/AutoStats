import scipy.stats as stats
import numpy as np
from typing import *
import DataType


# Class of descriptive statistics that are calculated from given set
class Variable:
    datatype: DataType
    mean: Union[float, None]  # arythmetic mean
    sd: Union[float, None]  # standard deviation
    median: Union[float, None]  # median
    sem: Union[float, None]  # standard error of mean
    max: Union[int, float, None]  # maximal value
    min: Union[int, float, None]  # minimal value
    iqr: Union[int, float, None]  # interquartile range
    mode: Any

    series: np.ndarray  # values

    def __init__(self, data: Iterable, datatype: DataType):
        for check in data, datatype:
            if check is None:
                raise TypeError(f'NoneType parameter was passed to Variable constructor')

        self.datatype = datatype

        ValType = None
        if datatype == 1:
            ValType = int
        if datatype == 0:
            ValType = float
        if ValType is not None:
            self.series = np.fromiter(data, dtype=ValType)

        self.countProperties()

    # TODO: CHECK IF DATA IS PROPER
    # TODO: Impplement non numerical value counting

    def countProperties(self):
        if self.datatype <= 1:
            self.sem = stats.sem(self.series)
            self.mean = float(np.mean(self.series))
            self.sd = float(np.std(self.series))
            self.max = float(np.max(self.series))
            self.min = float(np.min(self.series))
            self.iqr = stats.iqr(self.series)

        if self.datatype <= 2:
            self.median = float(np.mean(self.series))

        if self.datatype <= 3:
            self.mode = stats.mode(self.series)


x = Variable([1, 2, 3, 4, 5], 1)
print(x.mean)
