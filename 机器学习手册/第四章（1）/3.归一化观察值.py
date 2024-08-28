import numpy as np
from sklearn import preprocessing

x = np.array([[0.5,0.5],
              [1.1,3.4],
              [1.5,20.2],
              [1.63,34.4],
              [10.9,3.3]
              ])

normalizer = preprocessing.Normalizer(norm="l2")

x_normalizer = normalizer.transform(x)

print(x_normalizer)