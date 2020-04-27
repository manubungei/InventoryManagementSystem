from app import db

class NewInventory(db.Model):
    __tablename__ = 'new_inventories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), nullable = False)
    type = db.Column(db.String(10), nullable = False)
    buying_price = db.Column(db.Float, nullable = False)
    selling_price = db.Column(db.Float, nullable = False)
    sales = db.relationship('New_sale', backref = 'inventory', lazy =True)
    stock = db.relationship("Add_stock", backref= "inventory", lazy = True)



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
        return cls.query.filter_by(id=id).first()