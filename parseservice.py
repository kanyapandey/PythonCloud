import json, urllib
# import http.client
import httplib
import numpy as np

def getLearningData():
    # connection = http.client.HTTPSConnection('api.parse.com',443)
    connection = httplib.HTTPSConnection('api.parse.com',443)

    params = urllib.urlencode({"where":json.dumps({
           "diseaseType": { "$exists": True}
         })})

    connection.connect()
    connection.request('GET','/1/classes/Info?%s'%params,'', {
        "X-Parse-Application-Id":
        "xbIM6dI2SMzXRR1WZxYnBr6YZ3WTEiK1OOKjy6Jj",
        "X-Parse-REST-API-Key":
        "irtsK8M2927lMRU8EJc4yGovVNclOf9ALW8i2uBs"
            })

    #print(connection.getresponse().read().decode())
    response = json.loads(connection.getresponse().read())
    result = response['results']
    # print(result)

    # X = np.array([
    # (69,49,1,81),
    # (58,21,0,88),
    # (98,50,0,105),
    # (42,20,1,42),
    # (43,23,1,48),
    # (105,50,0,120)
    # ])

    X = np.array([ int(result[0]['Weight']) , int(result[0]['Age']), int(result[0]['Gender']), int(result[0]['heartRate']) ])
    y = np.array([])

    for info in result:
        data = np.array([
            int(info['Weight']),
            int(info['Age']),
            int(info['Gender']),
            int(info['heartRate'])
        ])

        X = np.vstack((X, data))
        y = np.append(y, int(info['diseaseType'] ))

    X = np.delete(X, 0, 0)
    return(X,y)
