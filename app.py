from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from ingest import save_file_to_database
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
        print('about to use uploaded file')
        save_file_to_database(filepath)

        # Remove the temporary file
        os.remove(filepath)

        return 'File uploaded and saved to the database.', 200
    else:
        return 'No file was uploaded.', 400


@app.route('/process_text', methods=['POST'])
def process_text():
    user_text = request.json.get('text', '')

    # Process the user input and generate a response
    # This is just an example; replace it with your actual processing logic
    response_text = f"You entered: {user_text}"

    return jsonify(result=response_text)


def save_file_to_database(filepath):
    return False


if __name__ == '__main__':
    app.run(port= 5005)
