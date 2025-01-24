from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app=Flask(__name__)


DB_CONFIG={
    "dbname":"postgres",
    "user":"postgres.bcuikzykxmfawolkhifl",
    "password":"wvaNgOLyHmxC2JTl",
    "host":"aws-0-ap-south-1.pooler.supabase.com",
    "port":5432
}

app.config['SQLALCHEMY_DATABASE_URI']=f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"

CORS(app)

db=SQLAlchemy(app)

migrate=Migrate(app,db) #initialize migragtions

ma=Marshmallow(app)