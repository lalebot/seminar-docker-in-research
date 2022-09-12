from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from waitress import serve

ws = Flask(__name__)

@ws.route('/')
def index():
    return 'Index Page'

@ws.route('/hello')
def hello():
    return 'Hello, World'

@ws.route('/upload')
def upload_file():
   return render_template('upload.html')

@ws.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'



# MAIN #########################################################################
if __name__ == '__main__':
    serve(ws ,host="0.0.0.0", port=5000)