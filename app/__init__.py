from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import urllib.parse

password = 'pscale_pw_Y3pL0WXFSEiEVQzmrOJCRqI6jvK9Z84lpPUuufqIwMA'
encoded_password = urllib.parse.quote_plus(password)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///swiggato.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql -h aws.connect.psdb.cloud -u qksjvd420hbi3xsvepqr -ppscale_pw_Y3pL0WXFSEiEVQzmrOJCRqI6jvK9Z84lpPUuufqIwMA --ssl-mode=VERIFY_IDENTITY --ssl-ca=/etc/ssl/certs/ca-certificates.crt'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://qksjvd420hbi3xsvepqr:pscale_pw_Y3pL0WXFSEiEVQzmrOJCRqI6jvK9Z84lpPUuufqIwMA@aws.connect.psdb.cloud/database_name?ssl_ca=/etc/ssl/certs/ca-certificates.crt'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://qksjvd420hbi3xsvepqr:{encoded_password}@aws.connect.psdb.cloud/database_name?ssl_ca=/etc/ssl/certs/ca-certificates.crt'

db = SQLAlchemy(app)

# Import routes
from app import routes