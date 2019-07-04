# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 20:12:00 2019

@author: Ellick
"""
import matplotlib.pyplot as plt
ds = [20, 15, 14, 14, 18, 15, 17, 16, 16, 18, 15, 19, 12, 13, 9,
      19, 15, 15, 16, 15]
ds_sorted = sorted(ds)
rf_ds = [ds.count(i)/ len(ds) for i in range(9,21) ]
sum_rf_ds = [sum(rf_ds[0:i])for i in range (1,13)]
print(ds_sorted)
print(rf_ds)
print(sum_rf_ds)

plt.bar([i for i in range(9,21)], rf_ds)
plt.plot([i for i in range(9,21)], sum_rf_ds)

plt.show()