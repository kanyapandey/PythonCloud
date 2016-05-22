from sklearn import neighbors, datasets
iris = datasets.load_iris()

X,y = iris.data, iris.target

# Create knn Classifier Model
knn = neighbors.KNeighborsClassifier(n_neighbors=3)

# Teach knn
knn.fit(X, y)

# Let's knn predict
result = knn.predict([ [7.3,  2.9,  6.3,  1.8] ])

response_data = {'result': result}
print (result) # [2]
print (response_data) # {'result': array([2])}  -> This is not json format
