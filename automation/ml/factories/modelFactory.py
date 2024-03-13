import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from keras.models import load_model

class ModelFactory:
    def __createModel():
        model = models.Sequential([
            layers.Dense(64, activation='relu', input_shape=(3,)),  # 3 valores representando o estado do jogo
            layers.Dense(64, activation='relu'),
            layers.Dense(2)
        ])

        return model


    def __compileModel(model):
        model.compile(optimizer='adam',
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=['accuracy'])
    
    def __trainModel(model, inputs, outputs):
        model.fit(inputs, outputs, epochs=20)
    
    def create(name, inputs, outputs):
        model = ModelFactory.__createModel()

        ModelFactory.__compileModel(model)
        ModelFactory.__trainModel(model, inputs, outputs)

        model.save("{}.keras".format(name))

class Model:
    def __init__(self) -> None:
        self.model = None
        pass

    def loadModel(self, path: str):
        self.model = load_model(path)

    def predict(self, currentState: list[int], precision: bool):
        result = self.model.predict(np.array(currentState))

        if precision:
            return np.round(result).astype(int)[0]
        
        return result


