
def h(x):
    return 3*x
def g(t):
    return -2*t - 2 - h(t)
def f(n):
    return -5*n*n + h(n)
print (h(g(8)))