import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document

from langchain.chains import LLMChain
from langchain.llms.fake import FakeListLLM
from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate



def getattributes(obj):
    return [attr for attr in dir(obj) if attr.startswith('__') is False]


def generate_blog_post(topic, index_creator, chain):
    docs = index_creator.vectorstore.similarity_search(topic, k=4)
    for k in range(4):
        print(docs[k].page_content[:50])
    inputs = [{"context": doc.page_content, "topic": topic} for doc in docs]
    return chain.apply(inputs)
