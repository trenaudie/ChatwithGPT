
"""Create a ChatVectorDBChain for question/answering."""
from langchain.callbacks.base import AsyncCallbackManager
from langchain.callbacks.tracers import LangChainTracer
from langchain.chains import ChatVectorDBChain
from langchain.chains.chat_vector_db.prompts import (CONDENSE_QUESTION_PROMPT,
                                                     QA_PROMPT)
from langchain.chains.llm import LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.vectorstores.base import VectorStore

from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain


def get_chain(vectorstore: VectorStore) -> ChatVectorDBChain:
    qa_chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="stuff")
    qa = RetrievalQAWithSourcesChain(combine_documents_chain=qa_chain, retriever=vectorstore.as_retriever())
    return qa