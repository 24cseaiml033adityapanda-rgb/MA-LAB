import numpy as np
import pandas as pd

l1 = list(eval(input("Enter dataset : ")))
series = pd.Series(l1)

mean = series.mean()
print("Mean : ",mean)

median = series.median()
print("Median : ",median)

mode = series.mode()
print("Mode : ",mode)