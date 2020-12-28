import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c=np.concatenate([a, b], axis=0)
d=np.vstack([a,b])
e=np.r_[a,b]
print(c)
print(d)
print(e)
