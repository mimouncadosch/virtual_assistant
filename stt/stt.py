import speech_recognition as sr
import os
import csv

UPLOAD_FOLDER = '/Users/mimoun/projects/audio/uploaded_data'
TRANSCRIPTS   = '/Users/mimoun/projects/audio/transcripts'

def transcribe(file_id):
	r = sr.Recognizer()
	file_url = os.path.join(UPLOAD_FOLDER,file_id)

	with sr.WavFile(file_url) as source:
		audio = r.record(source)

	try:
		list = r.recognize(audio,True)                  # generate a list of possible transcriptions
		with open(os.path.join(TRANSCRIPTS, file_id), "a") as myfile:
			for prediction in list:
				myfile.write(prediction["text"] + "\t (" + str(prediction["confidence"]*100) + "%) \n")
	except KeyError:                                    # the API key didn't work
		print("Invalid API key or quota maxed out")
	except LookupError:                                 # speech is unintelligible
		print("Could not understand audio")
		with open(os.path.join(TRANSCRIPTS, file_id), "a") as myfile:
			myfile.write("Could not understand audio")


def get_transcripts(file_id):
	with open (os.path.join(TRANSCRIPTS,file_id), 'rb') as csvfile:
		predictions = csv.reader(csvfile, delimiter='\t')
		res = []
		for p in predictions:
			res.append(p)
	return res