from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.review_model import Review
from flask_app.models import trail_model

# ==========CREATE REVIEW - ACTION======
@app.route('/reviews/create', methods=['POST'])
def create_review():
    id = request.form['trail_id']
    if not Review.validator(request.form):
        return redirect(f"/trails/{id}/show")
    review_data = {
        **request.form,
    }
    id = request.form['trail_id']
    Review.create_review(review_data)
    return redirect(f"/trails/{id}/show")


