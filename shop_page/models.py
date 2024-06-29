from project.settings import DB
class Product(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String(20), nullable = False)
    price = DB.Column(DB.Integer, nullable = False)
    description = DB.Column(DB.Text, nullable = False)
    count = DB.Column(DB.Integer, nullable = False)
    image = DB.Column(DB.String(100), nullable = False)
    discount = DB.Column(DB.Integer, nullable = False)

    def __repr__(self):
      return f"id - {self.id}; Назва товару - {self.name}"