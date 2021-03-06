'''
working exercise from sentex tutorials. with mods for clarification + api doc references.
How to program the Best Fit Slope - Practical Machine Learning Tutorial with Python p.8
https://youtu.be/SvmueyhSkgQ?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v
linear regression model  y=mx+b
m = mean(x).mean(y) -  mean (x.y)
    ------------------------------
    (mean(x)^2 - mean(x^2)
'''
style.use('fivethirtyeight')

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs = [1,2,3,4,5,6]
ys = [5,4,6,5,6,7]
#plt.scatter(xs, ys)
#plt.show()


xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope(xs, ys):
    m = (mean(xs) * mean(ys) - mean(xs*ys)) / ( mean(xs)*mean(xs) - mean(xs*xs) )
    return m

m = best_fit_slope(xs, ys)

print (m)
plt.scatter(xs, ys)
plt.plot(xs, xs*m)
plt.xlabel('xs')
plt.ylabel('ys')
plt.title("plot y=mx using linear regression")
plt.show()
