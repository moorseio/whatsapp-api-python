from database.db import db
from database.repositories.MenuRepo import MenuRepo
from config.InitializeDatabase import InitializeDatabase
from utils.LoadYml import port
from flask import Flask
from controllers.webhook.WebhooksController import webhook

app = Flask(__name__)
app.register_blueprint(webhook)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
app.app_context().push()

with app.app_context():
    db.create_all()

if(len(MenuRepo.findAll()) == 0):
    InitializeDatabase.initialize()

app.run(host="localhost", port=port)