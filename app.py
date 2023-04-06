from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from ingest import save_file_to_database
from response import generate_blog_post
import traceback

from langchain.chains import LLMChain
from langchain.llms.fake import FakeListLLM
from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate

app = Flask(__name__)

prompt_template = """Use the context below to write a 100 word blog post about the topic below:
    Context: {context}
    Topic: {topic}
    Blog post:"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "topic"]
)

chat_history = []
llm = HuggingFaceHub()
chain = LLMChain(llm=llm, prompt=PROMPT)


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
        index_creator = save_file_to_database(filepath)

        # Remove the temporary file
        os.remove(filepath)

        return 'File uploaded and saved to the database.', 200
    else:
        return 'No file was uploaded.', 400


@app.route('/process_text', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        input_text = data['text']

        request = {"context": chat_history, "topic": input_text}

        # Process the input_text and generate the processed_text
        # Just an example, replace with your processing logic
        answer = chain.apply(input_text)

        chat_history.append((input_text, answer))

        return jsonify({'processed_text': answer})

    except Exception as e:
        # Log the full traceback of the exception
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5005)
