import scipy.stats as stats
import numpy as np
from typing import *
import DataType
from Constants import Constants

import rpy2.robjects.numpy2ri
from rpy2.robjects.packages import importr
rpy2.robjects.numpy2ri.activate()
DescTools = importr('DescTools')


import pprint


def compute_skew(data, confidence_level=Constants.CONFIDENCE_LEVEL):
    """ Compute the skew and confidence interval using rpy2, DescTools
            @param data
            @return dict with keys: skew, skew_ci_lower, skew_ci_upper"""
    d = {}
    d["skew"], d["skew_ci_lower"], d["skew_ci_upper"] = DescTools.Skew(data, conf_level=confidence_level, method=2)
    return d


def compute_kurtosis(data, confidence_level=Constants.CONFIDENCE_LEVEL):
    d = {}
    d["Kurt"], d["Kurt_ci_lower"], d["Kurt_ci_upper"] = DescTools.Kurt(data, conf_level=confidence_level, method=2)
    return d

# Class of descriptive statistics that are calculated from given set
class Variable:
    isDiscreete: bool  # is Integer
    datatype: DataType
    mean: Union[float, None]  # arythmetic mean
    sd: Union[float, None]  # standard deviation
    median: Union[float, None]  # median
    sem: Union[float, None]  # standard error of mean
    max: Union[int, float, None]  # maximal value
    min: Union[int, float, None]  # minimal value
    iqr: Union[int, float, None]  # interquartile range
    ske: Union[float, None]  # Fisher-Pearson coefficient of skewness
    kurt: Union[float, None]  # kurtosis
    mode: Any

    series: np.ndarray  # values



    def countProperties(self):
        self.series = np.sort(self.series)
        if self.datatype <= 1:
            self.sem = stats.sem(self.series)
            self.mean = float(np.mean(self.series))
            self.sd = stats.tstd(self.series)
            self.max = float(np.max(self.series))
            self.min = float(np.min(self.series))
            self.iqr = stats.iqr(self.series)
            kurt = compute_kurtosis(self.series)
            ske = compute_skew(self.series)
            print(ske)
            self.kurt = stats.kurtosis(self.series, fisher=True, bias=False)
            self.ske = float(stats.skew(self.series, bias=False))

        if self.datatype <= 2:
            self.median = float(np.median(self.series))

        if self.datatype <= 3:
            self.mode = None
            # FIXME:    Write custom mode algorithm
            #           I want to calculate continious values mode from distirbution


    def __init__(self, data: Iterable, datatype: DataType):
        for check in data, datatype:
            if check is None:
                raise TypeError(f'NoneType parameter was passed to Variable constructor')

        # TODO: Implement non numerical value counting
        if datatype in [3, 4]:
            raise NotImplementedError('tbd')

        self.datatype = datatype

        ValType = None
        if datatype == 1:
            ValType = float
        if datatype == 0:
            ValType = float
        if ValType is not None:
            self.series = np.fromiter(data, dtype=ValType)

        self.countProperties()

    # TODO: CHECK IF DATA IS PROPER

    def __str__(self):
        return pprint.pformat(x.__dict__)


x = Variable([1.00,
              5.00,
              8.00,
              7.00,
              5.00,
              56.00,
              6.00,
              8.00,
              4.00,
              1.00], 1)

print(x)
