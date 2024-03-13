import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Input

inputs = np.array([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
outputs = np.array([[0, 0], [3, 2], [2, 1], [1, 0], [3, 2], [1, 0]])

model = Sequential()
model.add(Input(shape=(3,)))
model.add(Dense(10, activation='relu'))
model.add(Dense(2, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(inputs, outputs, epochs=1000, verbose=0)
model.save("beat_game.keras")

entrada_teste = np.array([[1, 3, 2]])
saida_prevista = model.predict(entrada_teste)
saida_prevista_int = np.round(saida_prevista).astype(int)
print("Entrada:", entrada_teste)
print("Saída prevista:", saida_prevista_int)