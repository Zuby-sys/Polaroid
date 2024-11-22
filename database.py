import sqlalchemy as sqla
CONNECTION_STRING = "mysql+pymysql://is61-2:l0mr9025@192.168.3.111:3306/baseforpractice"

class Database():
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connection = self.engine.connect()
    
    def translate_to_dict(self,result_raw):
        result = []
        for r in result_raw:
            result.append(r._asdict())
        return result

    def add_db(self, name, url):
        query = sqla.text("INSERT INTO imga (name, url) VALUES (:name, :url)")
        query = query.bindparams(sqla.bindparam("name", name))
        query = query.bindparams(sqla.bindparam("url", url))
        #query = query.bindparams(sqla.bindparam("id", id))
        self.connection.execute(query)
        self.connection.commit()

if __name__ == "__name__":
    db = Database()
    