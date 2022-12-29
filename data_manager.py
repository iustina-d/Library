from psycopg2._psycopg import cursor
from psycopg2.extras import RealDictCursor
import database_common

@database_common.connection_handler
def get_books(cursor):
    cursor.execute("SELECT * FROM books ;")
    return cursor.fetchall()