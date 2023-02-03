from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.resort_model import Resort
import os

# =============LANDING PAGE - READ ALL RESORTS===========
@app.route('/')
def index():
    all_resorts = Resort.get_all_resorts()
    return render_template('index.html', all_resorts = all_resorts)

# ============READ ONE - VIEW =============
@app.route('/resorts/<int:id>/show')
def show_resort(id):
    data = {
        'id' : id
    }
    maps_api_key = os.environ.get("FLASK_APP_API_KEY")
    this_resort = Resort.get_by_id(data)
    one_resort = Resort.get_all_trails(data)
    return render_template('resort_view_one.html', this_resort = this_resort, one_resort = one_resort, maps_api_key = maps_api_key)
