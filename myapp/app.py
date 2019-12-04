from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

app = Flask(__name__)

@app.route('/')
def test():
    return "Welcome"

if __name__=="__main__":
    logger.debug("Application is starting")
    from api import *
    #app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
    app.run(debug=True)
    
"""
1. pip install flask_resful

"""