import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Definir arquitetura da rede neural
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(3,)),  # 3 valores representando o estado do jogo
    layers.Dense(64, activation='relu'),
    layers.Dense(2)  # Saída representa a ação a ser tomada (por exemplo, [1, 3])
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=['accuracy'])

# Dados de treinamento (exemplo)
# Vamos supor que o estado inicial do jogo seja [2, 1, 3] e a ação tomada seja [1, 3]
# Então, o par de entrada seria [2, 1, 3] e o par de saída seria [1, 3]
X_train = np.array([[2, 1, 3], [2, 3, 1], [1, 3, 2], [1, 3, 2], [2, 1, 3]])
y_train = np.array([[2, 2], [1, 1], [3, 3], [2, 2], [1, 1]])

# Treinar o modelo
model.fit(X_train, y_train, epochs=20)

result = model.predict(np.array([[3, 1, 2]]))
print("Predict the array {}, the output is: {}".format([3, 1, 2], result))
print(result)

wantToSave: str = input("Do you want to save this model? Y/N? ")

if(wantToSave == "Y"):
    model.save("ai.keras")
