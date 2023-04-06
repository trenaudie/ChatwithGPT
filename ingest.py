import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document

# Determine the name of the environment variable you want to use for the OpenAPI key
env_var_name = "OPENAI_API_KEY"
env_var_name_huggingface = "HUGGINGFACEHUB_API_TOKEN"
# Get the value of your OpenAPI key from the provider of the API
key_value = "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" #most recent one
keyvalue_huggingface = "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"
# Set the environment variable with the key value
os.environ[env_var_name] = key_value
os.environ[env_var_name_huggingface] = keyvalue_huggingface

def getDocsendwithtxt():
    """Returns list of Document() objects from articles.txt files"""
    for file in os.listdir():
        if file.endswith(".txt"):
            with open(file, "r") as f:
                github_url = f"{file}"
                yield Document(page_content=f.read(), metadata={"source": github_url})



def getChunks(contentdict):
    """Returns list of Document() objects from {file:filecontent} dictionary"""
    for file in contentdict.keys():
        sourcename = file
        yield Document(page_content=contentdict[file], metadata= {"source": sourcename})



def saveDBStore(contentdict: dict, dbdir: str):
    textchunks = getChunks(contentdict)
    search_index = Chroma.from_documents(textchunks, OpenAIEmbeddings(), persist_directory = dbdir)
    search_index.persist()


def save_file_to_database(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
        contentDict = {filepath: content}
        print(contentDict)
        dbdir = f"{filepath}_dbstore"
        saveDBStore(contentDict, dbdir)


if __name__=='__main__':
    save_file_to_database("article.txt")
