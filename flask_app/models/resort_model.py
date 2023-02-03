from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import trail_model
from flask import flash

class Resort:
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.resort_name = data['resort_name']

# =======GET RESORT BY ID========
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM resorts WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False 
        return cls(results[0])

# =========GET ALL RESORTS=========
    @classmethod
    def get_all_resorts(cls):
        query = """
            SELECT * FROM resorts;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        resorts = []
        for row in results:
            resorts.append(cls(row))
        return resorts

# ==========GET ALL TRAILS FOR ONE RESORT==========
    @classmethod
    def get_all_trails(cls, data):
        query = """
            SELECT * FROM resorts
            LEFT JOIN trails
            ON trails.resort_id = resorts.id
            WHERE resorts.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            this_resort = cls(results[0])
            these_trails = []
            for row in results:
                trail_data = {
                    **row,
                    'id' : row['trails.id'],
                    'created_at' : row['trails.created_at'],
                    'updated_at' : row['trails.updated_at']
                }
                this_trail = trail_model.Trail(trail_data)
                these_trails.append(this_trail)
            this_resort.trails = these_trails
            return this_resort
            