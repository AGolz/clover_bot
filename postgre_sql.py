import psycopg2

import config


class PostgreSQL:
    
    def __init__(self, database):
        self.conn = psycopg2.connect(config.db_url)
        self.cursor = conn.cursor()
        print("Database opened")
        
