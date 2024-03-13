import numpy as np
from keras.models import load_model

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


