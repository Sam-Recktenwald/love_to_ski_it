from flask import Flask
import os
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET_KEY")
DATABASE = "love_to_ski_it_schema"
