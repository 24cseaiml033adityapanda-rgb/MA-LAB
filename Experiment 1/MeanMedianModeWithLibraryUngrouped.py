<<<<<<< HEAD
import numpy as np
import pandas as pd

l1 = list(eval(input("Enter dataset : ")))
series = pd.Series(l1)

mean = series.mean()
print("Mean : ",mean)

median = series.median()
print("Median : ",median)

mode = series.mode()
=======
import numpy as np
import pandas as pd

l1 = list(eval(input("Enter dataset : ")))
series = pd.Series(l1)

mean = series.mean()
print("Mean : ",mean)

median = series.median()
print("Median : ",median)

mode = series.mode()
>>>>>>> 2ec7c805dbf7078ab01857520d8d3823ebaf67d5
print("Mode : ",mode)