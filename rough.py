import numpy as np
list1 = np.ones(10000)
s = np.arange(10000)
print("first time ")
print(s)
np.random.shuffle(s)
list2= list1[s[:300]]
print("second time ")
print(s)
print(s[:10])

