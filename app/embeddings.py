# Create embeddings of the extracted text for futhrer preprocessing

## Steps involved are:
## - Create chunks of the text so that we can handle bulk data if any
## - Create embeddings using the OpenAI embedding class
## - Store embedding as pickle file

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
import pickle

def create_embeddings(text, embedding_store_file_name):
    """
        :param text: text extracted from the PDF file
        :param embedding_store_file_name: name of file in which vector embeddings will be stored
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
    chunks = text_splitter.split_text(text=text)
 
    if os.path.exists(f"{embedding_store_file_name}.pkl"):
        with open(f"{embedding_store_file_name}.pkl", "rb") as f:
            vector_store = pickle.load(f)
    else:
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    return vector_store
