import os
from flask import Flask, send_from_directory
from flask import render_template, request, redirect, url_for
from werkzeug import secure_filename


app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        saved_files_urls = []
        for key, file in request.files.iteritems():
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                saved_files_urls.append(url_for('uploaded_file', filename=filename))
        return saved_files_urls[0]
        #return render_template('saved_files.html', urls=saved_files_urls)

    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER,
                               filename)
    

app.debug = True

if __name__ == '__main__':
    app.run()

