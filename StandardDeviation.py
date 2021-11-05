from numpy import sqrt
import pandas as pd
import statistics

df =  [float(i) for i in pd.read_csv("data.csv").columns.tolist()]
mean = statistics.mean(df)
df = [(i-mean)*(i-mean) for i in df]
sumOfSqrdList = 0.0
for i in df:
    sumOfSqrdList+=i    
stdir = sqrt(sumOfSqrdList/len(df))
print(stdir)