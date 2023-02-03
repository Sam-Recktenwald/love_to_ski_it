from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import trail_model
from flask import flash

class Review:
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.description = data['description']
        self.rating = data['rating']
        self.date = data['date']
        self.name = data['name']
        self.trail_id = data['trail_id']

# ==========CREATE A REVIEW========
    @classmethod
    def create_review(cls, data):
        query = """
        INSERT INTO reviews (description, rating, date, name, trail_id)
        VALUES (%(description)s, %(rating)s, %(date)s, %(name)s, %(trail_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)

# =========SHOW ALL REVIEWS FOR ONE TRAIL==========
    @classmethod
    def get_all_reviews(cls, data):
        query = """
            SELECT * FROM reviews
            LEFT JOIN trails
            ON trails.id = reviews.trail_id
            WHERE trails.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        all_reviews = []
        if results:
            for row in results:
                this_review = cls(row)
                trail_data = {
                    **row,
                    'id' : row['trails.id'],
                    'created_at' : row['trails.created_at'],
                    'updated_at' : row['trails.updated_at']
                }
                this_trail = trail_model.Trail(trail_data)
                this_review.active_trail = this_trail
                all_reviews.append(this_review)
        return all_reviews

# =========VALIDATE=========
    @staticmethod
    def validator(form_data):
        is_valid = True

        if len(form_data['description']) < 1:
            flash("Please provide a review")
            is_valid = False
        
        # Added required field on radio input instead of below
        # if form_data['rating'] == False:
        #     flash("Please provide a valid rating")
        #     is_valid = False
        
        if len(form_data['date']) <1:
            flash("Please provide a date")
            is_valid = False

        if len(form_data['name']) <1:
            flash("Name is required")
            is_valid = False
        
        return is_valid