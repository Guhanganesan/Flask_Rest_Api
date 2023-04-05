from flask_restful import Api
from .Service import Service
#from .AngularService import AngularService
from app import app 
#import app instance from app.py

restServer=Api(app)
restServer.add_resource(Service,"/api/v1.0/task") # import your service and pass here