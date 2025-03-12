import matplotlib.pyplot as plt
import numpy as np

y = np.array([63, 234])
mylabels = [ "active", "tot_users"]

def absolute_value(val):
    a  = np.round(val/100.*y.sum(), 0)
    return int(a)


plt.pie(y, labels=mylabels, autopct=absolute_value, shadow=False)
#plt.pie(y, labels = mylabels)
plt.legend()
plt.show()
