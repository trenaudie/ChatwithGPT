from langchain.document_loaders import TextLoader

from langchain.indexes import VectorstoreIndexCreator

import os

# Determine the name of the environment variable you want to use for the OpenAPI key
env_var_name = "openai_api_key"

# Get the value of your OpenAPI key from the provider of the API
key_value = "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"


# Set the environment variable with the key value
os.environ[env_var_name] = key_value
loader = TextLoader('articles.txt')
index = VectorstoreIndexCreator(openai_api_key=os.environ[env_var_name] ).from_loaders([loader])