from factories import modelFactory
import numpy as np

modelName = str(input("Input model name: "))

x = np.array([[2, 1, 3], [2, 3, 1], [1, 3, 2], [1, 3, 2], [2, 1, 3]])
y = np.array([[2, 2], [1, 1], [3, 3], [2, 2], [1, 1]])

modelFactory.ModelFactory.create(modelName, x, y)
