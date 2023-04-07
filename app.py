from getchain import get_chain
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from ingest import save_file_to_database
import traceback
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import json
from utils.logger import logger

os.environ['OPENAI_API_KEY'] = "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"
print(os.environ['OPENAI_API_KEY'])
os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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"


def getattributes(obj): return [attr for attr in dir(
    obj) if attr.startswith('__') is False]


app = Flask(__name__)

prompt_template = """Use the context below to write a 100 word blog post about the topic below:
    Context: {context}
    Topic: {topic}
    Blog post:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "topic"]
)

chat_history = []
vectordb = Chroma(persist_directory='dbdir',embedding_function=OpenAIEmbeddings())
chain = get_chain(vectordb, PROMPT)
print(vectordb._collection.metadata)


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
        save_file_to_database(vectordb, filepath)
        logger.info(f"number of documents in db: {vectordb._collection._client._count('langchain')}")
        # Remove the temporary file
        os.remove(filepath)

        return 'File uploaded and saved to the database.', 200
    else:
        return 'No file was uploaded.', 400


@app.route('/qa', methods=['POST'])
def answerQuestion():
    try:
        data = request.get_json()
        question = data['text']
        #only add chat_history if conversationalRetriever
        answer = chain({'question': question, 'chat_history': chat_history})
        chat_history.append((question, answer['answer']))

        for k in chat_history:
            logger.info(k)
        
        logger.info(answer['source_documents'])
        logger.info('-----------------')
        page_contents = [doc.page_content for doc in answer['source_documents']]

        # Convert the list of page contents to a JSON object
        page_contents_json = json.dumps(page_contents)

        # Combine the `processed_text` and `page_content` JSON objects into a single dictionary
        response_data = {
            'processed_text': answer['answer'],
            'page_contents': page_contents_json
}
        return jsonify(response_data)
    
    except Exception as e:
        # Log the full traceback of the exception
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5006, debug=True)

