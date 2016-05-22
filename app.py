import falcon
from handler import *
from middlewares import *

api = falcon.API(middleware = [RequireJSON(), ParseJSON()])
app = Flask(api)
def add_routes(api):
    #api.add_route('/user/{account_id}', UserHandler())
    app.add_route('/user/{account_id}', NewUserHandler())
add_routes(api)
