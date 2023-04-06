import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

from langchain.indexes import VectorstoreIndexCreator

# Determine the name of the environment variable you want to use for the OpenAPI key
env_var_name = "OPENAI_API_KEY"
env_var_name_huggingface = "HUGGINGFACEHUB_API_TOKEN"
# Get the value of your OpenAPI key from the provider of the API
key_value = "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"
keyvalue_huggingface = "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"
# Set the environment variable with the key value
os.environ[env_var_name] = key_value
os.environ[env_var_name_huggingface] = keyvalue_huggingface


def getDocs():
    """Returns list of Document() objects from articles.txt files"""
    for file in os.listdir():
        if file.endswith(".txt"):
            with open(file, "r") as f:
                github_url = f"{file}"
                yield Document(page_content=f.read(), metadata={"source": github_url})


def getChunks(contentdict):
    """Returns list of Document() objects from {file:filecontent} dictionary"""
    splitter = CharacterTextSplitter(
        separator=" ", chunk_size=512, chunk_overlap=0)
    sources = []

    for file in contentdict.keys():
        sourcename = file
        sources.append(
            Document(page_content=contentdict[file], metadata={"source": sourcename}))

    for source in sources:
        sourcename = file
        for chunk in splitter.split_text(source.page_content):
            yield Document(page_content=chunk, metadata=source.metadata)

# what about first search index


def saveDBStore(search_index: Chroma, contentdict: dict):
    textchunks = getChunks(contentdict)
    search_index.add_documents(textchunks)
    search_index.persist()


def save_file_to_database(search_index: Chroma, filepath: str):
    with open(filepath, 'r') as f:
        content = f.read()
        contentDict = {filepath: content}
        print(contentDict)
        saveDBStore(search_index, contentDict)
