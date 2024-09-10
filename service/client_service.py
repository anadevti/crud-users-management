from models.client import Client
from database import db

class ClientService():

    def getAll(self):
        Client.query.all()
        
    def getById(self, id:int):
        Client.query.get(id)

    def create(self, client:Client):
        db.session.add(client)
        db.session.commit()

    def update(self, client:Client):
        db.session.add(client)
        db.session.commit()
    
    def delete(self, client:Client):
        db.session.delete(client)
        db.session.commit()
