# Simple File Uploader

This provides a simple webservice that receives a file and stores it on a given location.

The directory for the upload is given by an local variable, the file name for the stored files is given as path parameter of the request and the file is send in the request body.

## Installation

* create a venv `python3 -m venv .venv`
* activate it `. ./.venv/bin/activate`
* install dependencies `pip install -r requirements.txt`

## Usage

* if necessary change the `UPLOAD_FOLDER` variable
* start it with `python main.py`
* test the upload with `curl -X PUT http://localhost:5000/upload/<target.file> --upload-file <source.file>`: