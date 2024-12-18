import psycopg2

#app_user is login info for normal user, they can only select, insert, delete rows from table
host = 'localhost' #172.16.37.250 - for ramy
dbname = 'postgres'
user = 'postgres' #app_user 
password = 'onepiece' #app_user
port = 5432

def connection():
    try:
        conn = psycopg2.connect(
            host = host,
            dbname = dbname,
            user = user,
            password = password,
            port = port
        )

        # this low diffs the error: 
        # current transaction is aborted, commands ignored until end of transaction block
        conn.autocommit = True 
        
        return conn

    except Exception as error:
        print(error)
        return None

