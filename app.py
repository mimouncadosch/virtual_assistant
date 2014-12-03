import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory

from werkzeug import secure_filename
from db import db
from stt import stt
# Config
app = Flask(__name__, static_folder='static', static_url_path='')

UPLOAD_FOLDER = '/Users/mimoun/projects/audio/uploaded_data'
TRANSCRIPTS = '/Users/mimoun/projects/audio/transcripts'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TRANSCRIPTS'] = TRANSCRIPTS

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav', 'mp3'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Protocol endpoints - Input
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file_id = request.form['id']
		file_date = request.form['date']
		file =  request.files['audio_input.wav']
		if file:
			filename = secure_filename(file_id)
			data_folder = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(data_folder)
			db.save_metadata(file_id, file_date, False)
			stt.transcribe(file_id)
			return 'file successfully uploaded and metadata saved'
	
	return """
			This endpoint is only used for POST requests. \n 
			Please visit README.txt
			"""

# Protocol endpoints - Output
@app.route('/files', methods=['GET'])
def get_messages():
	res = db.get_files()
	# return jsonify(files = res)
	return render_template("index.html", files = res)

@app.route('/unread/', methods=['GET'])
def get_unread_messages():
	res = db.get_unread_files()
	print res
	return res

# Client endpoints - Input
@app.route('/record', methods=['GET'])
def record():
	return render_template('record.html')

@app.route('/post', methods=['GET'])
def post():
	return render_template('post.html')

# @app.route('/markread/<file_id>', methods=['POST'])
@app.route('/markread/<file_id>', methods=['POST'])
def mark_as_read(file_id):
	read = request.json['read']
	db.mark_as_read(file_id, read)
	return 'marked', file_id, ' as read'
	# return "hello markread"

# Client endpoints - Output
@app.route('/')
def hello():
	files = db.get_files()
	transcripts = dict()
	for file in files:
		file.transcript = stt.get_transcripts(file.file_id)[0]

	return render_template('index.html', files=files, url=request.url) 

@app.route('/transcript/<file_id>')
def transcripts(file_id):
	stt.get_transcripts(file_id)
	return 'hola'


@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
	app.run(debug=True)
