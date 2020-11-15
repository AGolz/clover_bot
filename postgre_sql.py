import psycopg2

import config


class PostgreSQL:
    
    def extract_id(self):
        with psycopg2.connect(config.db_url) as conn:
            print('Database opened')
            with conn, conn.cursor() as cur: 
                cur.execute("SELECT * FROM admin_file WHERE id = %d" % (config.column_id))
                file_id = cur.fetchone()[0]
                print(file_id)
        return file_id
                    
                
            
        
    
        
  