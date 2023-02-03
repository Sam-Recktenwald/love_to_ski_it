from flask_app import app
from flask_app.controllers import resorts_controller, trails_controller, reviews_controller

if __name__=="__main__":
    app.run(debug=True, port=5001)