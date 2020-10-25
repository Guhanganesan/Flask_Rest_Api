from flask import Flask
import logging as logger
from flask_cors import CORS
logger.basicConfig(level="DEBUG")

app = Flask(__name__)
CORS(app)

if __name__=="__main__":
    logger.debug("Application is starting")
    from api import *
    #app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
    app.run(debug=True)