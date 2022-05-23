import pickle
from swords import Sword
from sklearn import tree


class DecisionTreePredict():

    model = None

    def __init__(self):
        self.model = pickle.load(open('decision-tree-model.sav', 'rb')) # loading the model

    def predict(self, data):
        prediction = self.model.predict([data])[0] # using predict method from DecisionTree model
        if prediction == 0:
            print('Model predicted: Not monster')
        else:
            print('Model predicted: Monster')
        return Sword(prediction) # return adequate sword enum

