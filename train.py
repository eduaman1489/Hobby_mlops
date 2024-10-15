import pickle
import sklearn
from sklearn.datasets import load_diabetes
from sklearn.linear_model import BayesianRidge, Ridge

x, y = load_diabetes(return_X_y=True)

model = Ridge().fit(x, y)

with open("regmodel.pkl", 'wb') as file:
    pickle.dump(model, file)

