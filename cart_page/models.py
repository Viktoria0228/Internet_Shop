from project.settings import DB

class Order(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String(30), nullable = False)
    surname = DB.Column(DB.String(30), nullable = False)
    email = DB.Column(DB.String(70), nullable = False)
    phone_number = DB.Column(DB.String(30), nullable = False)
    city_recepient = DB.Column(DB.String(30), nullable = False)
    post_office = DB.Column(DB.String(50), nullable = False)
    add_wishes = DB.Column(DB.Text, nullable = False)

    def __repr__(self):
      return f"id користувача - {self.id}; Email користувача {self.email}; Місто користувача {self.email}; Поштове відділення користувача {self.email};"
    