import glob
import hashlib
import os

from flask import Flask, make_response, request, send_file

app = Flask(__name__)


FILEROOT = 'store/'


def create_name(file):
    hasher = hashlib.md5()
    for chunk in file_chunks(file.stream):
        hasher.update(chunk)
    return hasher.hexdigest()


def file_chunks(file, chunk_size: int = 8192):
    chunk = file.read(chunk_size)
    while len(chunk) > 0:
        yield chunk
        chunk = file.read(chunk_size)

    file.seek(0)


def save_file(filehash, newfile, extension):
    fullpath = FILEROOT + filehash[0:2]
    filename = filehash + extension
    if os.path.exists(fullpath):
        if check_file(filehash):
            return make_response('File already exists', 422)
        else:
            newfile.save(os.path.join(fullpath, filename))
            return filehash
    else:
        os.mkdir(fullpath, 0o755)
        newfile.save(os.path.join(fullpath, filename))
        return filehash


@app.route('/upload', methods=['POST'])
def upload():
    newfile = request.files['file']
    _, extension = os.path.splitext(newfile.filename)
    filehash = create_name(newfile)
    response = save_file(filehash, newfile, extension)
    return response


def check_file(name):
    fullpath = FILEROOT + name[0:2]
    filename = os.path.join(fullpath, name + '.*')
    found_files = glob.glob(filename)
    if len(found_files) > 0:
        return found_files[0]


@app.route('/download/<filehash>', methods=['GET'])
def download(filehash):
    filename = check_file(filehash)
    if filename:
        return send_file(filename)
    else:
        return make_response('File doesn\'t exist', 404)


@app.route('/delete/<filehash>', methods=['DELETE'])
def delete(filehash):
    filename = check_file(filehash)
    if filename:
        os.remove(filename)
        return 'File deleted'
    else:
        return make_response('File doesn\'t exist', 404)


if __name__ == '__main__':
app.run(debug=True)