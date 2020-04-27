from app import db

class NewInventory(db.Model):
    __tablename__ = 'new_inventories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    type = db.Column(db.String, nullable = False)
    buying_price = db.Column(db.Float)
    selling_price = db.Column(db.Float, nullable = False)


# adding inventories
    def add_inventories(self):
        db.session.add(self)
        db.session.commit()
#       session.add - adds records
#       session.commit - sends records to db

#  Fetch all records from database
    @classmethod
    def fetch_records(cls):
        inventory = cls.query.all()
        return inventory

#  Fetch records by ID
    @classmethod
    def fetch_by_id(cls,id):


        delete_record = cls.filter_id(id=id).first()
        if delete_record.first():
            delete_record.delete()
            db.session.commit()
            return True
        else:
            return False
