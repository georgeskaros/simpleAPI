import psycopg2

# db connections to simplify the code
class Database:
    def __init__(self, config):
        self.database = config["database"]
        self.user = config["user"]
        self.password = config["password"]
        self.host = config["host"]
        self.port = config["port"]
        self.con = None
        self.connect()

    def connect(self):
        self.con = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)
        self.con.autocommit = True

    def cursor(self):
        return self.con.cursor()

    def query(self, query, arguments=()):
        cursor = self.cursor()
        cursor.execute(query, arguments)
        results = cursor.fetchall()
        cursor.close()
        return results


db = Database({
    "database": "Margera_exercise",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",
    "port": "5433"
})
