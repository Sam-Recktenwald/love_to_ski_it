from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.trail_model import Trail
from flask_app.models import review_model, resort_model


# ============READ ONE - VIEW========
@app.route('/trails/<int:id>/show')
def show_trail(id):
    data = {
        'id' : id
    }
    this_trail = Trail.get_trail_by_id(data)
    all_reviews = review_model.Review.get_all_reviews(data)
    return render_template('trail_view_one.html', this_trail = this_trail, all_reviews = all_reviews)


