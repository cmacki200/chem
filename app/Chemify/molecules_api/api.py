from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
while True:

    #py script acts as a API wrapper using psycopg2 to perform basic CRUD operations on a postgres database Get requests can be performed 
    # within the command using py -m uvicorn main:app, while delete and update can be done via the test functions or postman.

    try:
        print('connecting to Postgres DB...')
        conn = psycopg2.connect(host='localhost', user='postgres', password='root',
                                cursor_factory=RealDictCursor)
        conn.autocommit = True

        #intialise PostgresDB connection, new instance of Postgres connects to postgres before any new dbs can be created. Code is
        #placed within a try block for exception and validation checks. For speed and to avoid having to commit to each statement, any action will
        #autocommit. Within dev this would not be the case as it may conpromise data integrity.
        cursor = conn.cursor()
        print('connection successful')
        break
    except Exception as error:
    #code handles error exception handling.
        print('connection failed')
        print(error)
        time.sleep(5)

    #code will purposefully reconnect every 5secs until it obtains a connection
    #where the block will break.


app = FastAPI()
#FastAPI is a web framework for creating APIs within python. 

@app.get('/')
#accessed at the root of the http request, this is the default instance when loading the script to the server.
def create_db():
    db_name = 'Reactions'
    cursor.execute('DROP DATABASE IF EXISTS ' + db_name)
#check connection for existing database and drop it.

    sql = 'CREATE DATABASE ' + db_name
    cursor.execute(sql)
    return {'message': 'Database created: ' + db_name}
#sql create statement which is executed within a cursor class.


@app.get('/tb1')
#route change triggers function call - script searches for match.
def create_table1():
    while True:
        try:
            conn = psycopg2.connect(host='localhost', database='reactions', user='postgres', password='root',
                                    cursor_factory=RealDictCursor)
            conn.autocommit = True
            #search for new database structure, by default postgres will create a postgres database. Database instance must be switched to 
            # insert table.
            cursor = conn.cursor()
            print("connection successful")
            break
        except Exception as error:
            print("connection failed")
            print(error)
            time.sleep(5)

    tb_name = "ReactionData"
    cursor.execute("DROP TABLE IF EXISTS " + tb_name)
    #statment checks if table matching the new_name exists and if so drops it.

    sql = '''CREATE TABLE ReactionData(
    reaxys_id CHAR(20) NOT NULL,
    smiles CHAR(20),
    name INT,
    formula CHAR(1),
    InChI_key FLOAT
    )'''
    #CREATE TABLE STATEMENT ReactionData with appropriate fields.

    cursor.execute(sql)
    return {"message": "Table created: " + tb_name}
    #server validation, input validation that table of the expected name has been created.


@app.get("/tb2")
async def create_table2():
    while True:
        try:
            conn = psycopg2.connect(host='localhost', database='reactions', user='postgres', password='root',
                                    cursor_factory=RealDictCursor)
            conn.autocommit = True
            cursor = conn.cursor()
            print("connection successful")
            break
        except Exception as error:
            print("connection failed")
            print(error)
            time.sleep(5)

    tb_name = "ReactionMetadata"
    cursor.execute("DROP TABLE IF EXISTS " + tb_name)

    sql = '''CREATE TABLE ReactionMetadata(
    n_references CHAR(20) NOT NULL,
    ma_publication_year CHAR(20),
    entry_date INT,
    update_date CHAR(20)
    )'''
    #SQL statement for second table.
    cursor.execute(sql)
    return {"message": "Table created" + tb_name}
    #server validation check.


@app.get("/add")
#insert API call.

def add_instance():

    while True:
        try:
            conn = psycopg2.connect(host='localhost', database='reactions', user='postgres', password='root',
                                    cursor_factory=RealDictCursor)
            conn.autocommit = True
            cursor = conn.cursor()
            print("connection successful")
            break
        except Exception as error:
            print("connection failed")
            print(error)
            time.sleep(5)

    sql = '''INSERT INTO ReactionMetadata (n_references,
    ma_publication_year, entry_date, update_date) VALUES ('test', '2022', 2022, '2022')'''
    #insert statement, holds dummy data but would plug into the input database.

    cursor.execute(sql)
    print('record inserted')
    #execute SQL and print for debug.

    cursor.execute('SELECT * from ReactionMetadata')
    data = cursor.fetchall()
    return {"detail": data}
    #fetch all row/s to validate insert - in our case simply prints one on the server line.


@app.put("/update")
#update API call, uses PUT request so requires postman or an API test case.
def update_call():

    while True:
        try:
            conn = psycopg2.connect(host='localhost', database='reactions', user='postgres', password='root',
                                    cursor_factory=RealDictCursor)
            conn.autocommit = True
            cursor = conn.cursor()
            print("connection successful")
            break
        except Exception as error:
            print("connection failed")
            print(error)
            time.sleep(5)

            update_r = 0
            #var to store row count.

    sql = """ UPDATE ReactionMetadata
                SET update_date = 2002
                WHERE n_references = 'test'"""
                #SQL to update existing record on the table by referring to the key within n_references.

    cursor.execute(sql)
    #execute update sql
    update_r = cursor.rowcount
    #check results and record row count.
    return {"detail": update_r}
    #return row count to validate the update statement.


@app.delete("/drop")
#delete API call, uses the delete request so requires direct call through postman or test case.
def delete_call():

    while True:
        try:
            conn = psycopg2.connect(host='localhost', database='reactions', user='postgres', password='root',
                                    cursor_factory=RealDictCursor)
            conn.autocommit = True
            cursor = conn.cursor()
            print("connection successful")
            break
        except Exception as error:
            print("connection failed")
            print(error)
            time.sleep(5)

    sql = """ DELETE FROM ReactionMetadata
            WHERE n_references = 'test'"""
            #DELETE SQL statmement, filtered by n_reference record

    cursor.execute(sql)
    return {"message": "dbdeleted"}
    #execute sql and display validation message on request body.