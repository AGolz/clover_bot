import psycopg2

import config


class PostgreSQL:
    
    def __init__(self, database):
        self.connect = psycopg2.connect(dbname=config.db_name, user=config.db_user, 
                        password=config.db_pass, host=config.db_host)
        self.cursor = connect.cursor()
        
    def select_all(self):
        with self.connect:
            return self.cursor.execute('SELECT * FROM admin_file').fetchall()
        
    def select_single(self, rownum):
        with self.connect:
            return self.cursor.execute('SELECT * FROM admin_file WHERE id = ?', (rownum,)).fetchall()[0]
        
    def count_rows(self):
        with self.connect:
            result = self.cursor.execute('SELECT * FROM admin_file').fetchall()
            return len(result)
        
    def close(self):
        self.connect.close()
         
