import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import torch

app=Flask(__name__)
torch.hub.set_dir("torch")
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
RESULTS_FOLDER = os.path.join(path, 'results')
if not os.path.isdir(RESULTS_FOLDER):
    os.mkdir(RESULTS_FOLDER)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(f"filename= {filename}")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            # return redirect('/')
            results = model(f"./uploads/{filename}")
            results.save(save_dir="./results")
            #full_filename = f"{path}/results/{filename}"
            #return render_template("analize.html", user_image = full_filename)
            #
            https://stackoverflow.com/questions/68227626/python-flask-display-image-from-file-input
            image_b64 = base64.b64encode(image.read()).decode('utf-8')
            
            return render_template('analize.html', user_image = image)
        else:
            flash('Allowed file types are png, jpg, jpeg, gif')
            return redirect(request.url)


    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
    return render_template("analize.html", user_image = full_filename)


if __name__ == "__main__":
    app.run(host = '127.0.0.1',port = 5000, debug = False)