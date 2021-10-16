"""Simple Server to receive files with a http PUT request."""

from flask import request, jsonify, Flask
from shutil import copyfileobj

# where to store the files
UPLOAD_FOLDER = '/tmp/'

app = Flask(__name__)

@app.route('/upload/<filename>', methods=['PUT'])
def upload(filename):
  """
  Takes the filename from the requests path parameter
  and stores the request body as a file under this 
  name in the UPLOAD_FOLDER.
  """
  
  with open(f'{UPLOAD_FOLDER}/{filename}', 'wb') as f:
        copyfileobj(request.stream, f)

  resp = jsonify({'message': f'{filename} saved'})
  resp.status_code = 200
  return resp

# let's go...
if __name__ == "__main__":
    app.run()