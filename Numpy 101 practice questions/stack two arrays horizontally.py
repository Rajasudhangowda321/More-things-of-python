import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c=np.concatenate([a, b], axis=1)
d=np.hstack([a,b])
e=np.c_[a,b]
print(c)
print(d)
print(e)
