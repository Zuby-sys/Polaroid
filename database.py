import sqlalchemy as sqla
CONNECTION_STRING = "mysql+pymysql://root@localhost:3307/polaroid"

class Database():
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connection = self.engine.connect()
    
    def translate_to_dict(self,result_raw):
        result = []
        for r in result_raw:
            result.append(r._asdict())
        return result

    def add_db(self, name, id, way):
        query = sqla.text("UPDATE img_info SET name = :name WHERE id = :id")
        query = query.bindparams(sqla.bindparam("name", name))
        query = query.bindparams(sqla.bindparam("way", way))
        query = query.bindparams(sqla.bindparam("id", id))
        self.connection.execute(query)
        self.connection.commit()

if __name__ == "__name__":
    db = Database()
    db.del_animals