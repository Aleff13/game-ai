import numpy as np
from tensorflow import keras
from keras.models import load_model

class GameApi:

    def loadModel(modelPath: str = 'beat_game.keras'):
        return load_model(modelPath)

    def getCurrentOrder() -> str:
        return input("Digite a sequencia da lista: ")

    def transformInputs(inputs: str) -> list[int]:
        return list(int(x) for x in inputs.split(","))

    def normalizeValues(values):
        return np.array([values])

    def normalizeOutput(output):
        return np.round(output).astype(int)[0]

    def displayResult(normalizedOutput):
        print(normalizedOutput)
        print("Mova o objeto {} para a posicao {}". format(normalizedOutput[0], normalizedOutput[1]))

    def predictStep(model, normalizedValues):
        return model.predict([normalizedValues])

model = GameApi.loadModel()

state = GameApi.getCurrentOrder()
values = GameApi.transformInputs(state)
normalizedValues = GameApi.normalizeValues(values)

output = GameApi.predictStep(model, normalizedValues)

normalizedOutput = GameApi.normalizeOutput(output)

GameApi.displayResult(normalizedOutput)