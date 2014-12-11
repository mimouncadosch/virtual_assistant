import MySQLdb
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging
from config import DSN
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DSN
db = SQLAlchemy(app)

class File(db.Model):
	file_id = db.Column(db.String(255), primary_key=True)
	date 	= db.Column(db.String(120))
	read 	= db.Column(db.Boolean(120))

	def __init__(self, file_id, date, read):
		self.file_id = file_id
		self.date = date
		self.read = read

		def __repr__(self):
			return '<id %r>' % self.id

# Establish connection with database

# Save metadata
def save_metadata(file_id, date, is_read):
	print 'saving file with id', file_id, ' and isread', is_read
	new_file = File(file_id, date, is_read)
	db.session.add(new_file)
	db.session.commit()
	return True

def get_files():
	return File.query.all()

def get_unread_files():
	return File.query.filter_by(read=False).all()

def mark_as_read(id, read):
	res = File.query.filter_by(file_id=id).first()
	res.read = True
	db.session.commit()
	return True

def mark_as_unread(id, read):
	res = File.query.filter_by(file_id=id).first()
	res.read = False
	db.session.commit()
	return True