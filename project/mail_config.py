import flask_mail
from .settings import shop

shop.config['MAIL_SERVER'] = 'smtp.gmail.com'
shop.config['MAIL_PORT'] = 587
shop.config['MAIL_USE_TLS'] = True
shop.config['MAIL_USE_SSL'] = False
shop.config['MAIL_USERNAME'] = 'boyarkina.ar@gmail.com'
shop.config['MAIL_PASSWORD'] = 'djiw yjpu zujg hxls'
shop.config['MAIL_DEFAULT_SENDER'] = "boyarkina.ar@gmail.com"

mail = flask_mail.Mail(app = shop)
