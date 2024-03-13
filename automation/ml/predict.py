from modelFactory import Model, ModelFactory
import numpy as np

model = Model()

model.loadModel("test.keras")
print(model.predict([[1, 3, 2]], True))

x = np.array([[2, 1, 3], [2, 3, 1], [1, 3, 2], [1, 3, 2], [2, 1, 3]])
y = np.array([[2, 2], [1, 1], [3, 3], [2, 2], [1, 1]])

ModelFactory.create("test", x, y)
