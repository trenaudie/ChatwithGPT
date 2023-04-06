import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document

def getDocs():
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
        dbdir = f"{filepath}_dbstore"
        saveDBStore(contentDict, dbdir)


