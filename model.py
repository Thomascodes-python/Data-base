import sqlite3


def savedetails(name, password):
    connection = sqlite3.connect("login database.db")
    cursor = connection.cursor()

    createquery= """CREATE TABLE IF NOT EXISTS details
                    (NAME text,PASSWORD text)"""
    
    connection.execute(createquery)

    insert_query = """INSERT INTO details
                    (name,password)VALUES (?,?)"""
    
    insert_details = (name,password)

    cursor.execute(insert_query,insert_details )
    
    connection.commit()

    return True
