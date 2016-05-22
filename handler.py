import json
from sklearn import neighbors, datasets
import numpy as np
import parseservice
import flask import Flask

class UserHandler:
    def on_get(self, req, resp,account_id):

        resp.body = json.dumps({'status':account_id})
    def on_post(self, req, resp,account_id):
        data = req.context['json']
        #resp.body = json.dumps({'THIS IS':'POST'})
        resp.body = data

class NewUserHandler:
    def on_get(self, req, resp,account_id):
        # w=43&a=23&g=1&h=48

        w = float(req.get_param('w'))
        a = float(req.get_param('a'))
        g = float(req.get_param('g'))
        h = float(req.get_param('h'))

        #resp.body = json.dumps({'THIS IS':'POST'})
        #resp.body = json.dumps({'status':account_id})
        learning = parseservice.getLearningData()
        print( len(learning[0]) )
        print( len(learning[1]) )

        # X = np.array([
        # (69,49,1,81),
        # (58,21,0,88),
        # (98,50,0,105),
        # (42,20,1,42),
        # (43,23,1,48),
        # (105,50,0,120)
        # ])

        X = learning[0]

        y = learning[1]

#X,y = iris.data, iris.target

# Create knn Classifier Model
        knn = neighbors.KNeighborsClassifier(n_neighbors=3)

# Teach knn
        knn.fit(X, y)
        # result = knn.predict([ [98,50,0,105] ])
        result = knn.predict([ [w, a, g, h] ])

#result = knn.predict([ [98,50,0,105], [105,50,0,120],[43,23,1,48],[42,20,1,42],[69,49,1,81],[58,21,0,88] ])
# Let's knn predict
#result = knn.predict([ [98,50,0,105], [105,50,0,120],[43,23,1,48],[42,20,1,42],[69,49,1,81],[58,21,0,88] ])
#result = knn.predict([ [6.2,  3.4,  5.4,  2.3], [7.3,  2.9,  6.3,  1.8] ])
        #print (result)

        final = {'result': result[0]}
        print (final)
        resp.body = json.dumps(final)
        #print(final)
