import psycopg2

import config


class PostgreSQL:
    
    def extract_id(self):
        with psycopg2.connect(config.db_url) as conn:
            print('Database opened')
            with conn, conn.cursor() as cur: 
                cur.execute('SELECT * FROM admin_file WHERE id = %s',(config.column_id))
                db_row = cur.fetchone()
                for row in db_row:
                    file_id = row['file_id']
                    print(file_id)
        return file_id
                    
                
            
        
    
        
  