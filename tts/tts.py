import requests, os, wave, urllib, urllib2
from werkzeug import secure_filename
import hashlib
from datetime import datetime
UPLOAD_FOLDER = '/Users/mimoun/projects/audio/uploaded_data'
TRANSCRIPTS   = '/Users/mimoun/projects/audio/transcripts'

def get_speech(phrase):

	language = 'en'
	url = 'http://translate.google.com/translate_tts'
	user_agent="Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5." 
	file_id = generateID()
	data_folder = os.path.join(UPLOAD_FOLDER, file_id)
	params = urllib.urlencode({'q':phrase, 'tl':language}) 	# Query parameters.
	request = urllib2.Request(url, params) 					# HTTP request

	request.add_header('User-Agent', user_agent) 			# Adding agent as header
	response = urllib2.urlopen(request)

	if response.headers['content-type'] == 'audio/mpeg':
		with open(data_folder, 'wb') as file:
			file.write(response.read())
		
		with open(os.path.join(TRANSCRIPTS, file_id), "a") as myfile:
			myfile.write(phrase + "\t (100%)")
		
		return file_id
	else:
		return False
	
def generateID():
	return hashlib.sha1(datetime.now().strftime("%Y-%m-%d %H:%M:%S")).hexdigest()

# http://mostovenko.blogspot.com/2012/04/voicing-messages-in-python-or-fun-with.html