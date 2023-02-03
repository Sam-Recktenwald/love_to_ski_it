from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import resort_model, review_model
from flask import flash

class Trail:
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.trail_name = data['trail_name']
        self.difficulty = data['difficulty']
        self.resort_id = data['resort_id']

# ===========GET TRAIL BY ID========
    @classmethod
    def get_trail_by_id(cls, data):
        query = """
            SELECT * FROM trails
            WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False 
        return cls(results[0])