from database import db


class Client(db.Model):

    __tablename__ = "client"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email
