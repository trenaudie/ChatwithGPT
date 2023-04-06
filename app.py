from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from ingest import save_file_to_database
import traceback
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['document']
    if uploaded_file:
        # Save the file temporarily
        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join('temp', filename)
        uploaded_file.save(filepath)

        # Process the file and save it to the database
        # You will need to implement this part based on the type of database you are using
        save_file_to_database(filepath)

        # Remove the temporary file
        os.remove(filepath)

        return 'File uploaded and saved to the database.', 200
    else:
        return 'No file was uploaded.', 400


@app.route('/process-text', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        input_text = data['text']

        # Process the input_text and generate the processed_text
        # Just an example, replace with your processing logic
        processed_text = input_text.upper()

        return jsonify({'processed_text': processed_text})
    except Exception as e:
        # Log the full traceback of the exception
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port= 5005)
