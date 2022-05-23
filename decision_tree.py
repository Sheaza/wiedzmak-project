import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import pickle
from sklearn import tree

ready_monsters = np.array([[1,0,1,1,0,1,0,0,0], [1,1,1,1,0,0,0,0,1], [1,0,0,0,1,0,1,2,1], [0,0,0,0,1,0,0,3,0]])

# loading data
data = pd.read_excel('dataset.xlsx', index_col=0)

# split data to X - features, y - dependent variable
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values


# splitting data into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train = np.concatenate((X_train, ready_monsters[:, :-1]), axis=0)
y_train = np.concatenate((y_train, ready_monsters[:, -1]), axis=0)
# initializing and training the model
model = DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=5, min_samples_leaf=5)
model = model.fit(X_train, y_train)

# checking accuracy and std of all accuracies scores
accuracies = cross_val_score(estimator=model, X=X_train, y=y_train, cv=10)
print(f'Accuracy: {accuracies.mean()*100} %')
print(f'Std: {accuracies.std()*100} %')

# params for hyperparameters tuning
# params = {
#     'max_depth': [2, 3, 5, 10, 20],
#     'min_samples_leaf': [5, 10, 20, 50, 100]
# }
#
# # grid_search tuning
# grid_search = GridSearchCV(estimator=model,
#                            param_grid=params,
#                            scoring='accuracy',
#                            cv=10,
#                            n_jobs=-1)
#
# grid_search.fit(X_train, y_train)
# best_acc = grid_search.best_score_
# best_params = grid_search.best_params_
# print(f'Best Accuracy: {best_acc*100} %') # 100%
# print(f'Best Params: ', best_params) # max_depth=5, min_samples_leaf=5

# single prediction - leshy
print(model.predict([[1,0,0,0,1,0,1,2]])) # 1

# saving model
path = 'decision-tree-model.sav'
pickle.dump(model, open(path, 'wb'))

fig = plt.figure(figsize=(25, 20))
_ = tree.plot_tree(model, feature_names=data.columns[:-1], class_names=data.columns[-1], filled=True)
fig.savefig('decision-tree-graph.png')