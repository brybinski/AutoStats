import pandas as pd
import numpy as np
import scipy as sp
from typing import *


class DataToProcess:
    df: pd.DataFrame
    max_values: Iterable
    stats: list[Dict]

    def __init__(self, df: pd.DataFrame):
        self.df = df

