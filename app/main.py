# External libraries
import streamlit as st
import time
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# Internal file imports
from extract import extract_text
from embeddings import create_embeddings
from store import store_embeddings
from chat import chat_with_pdf

#Loading env variables
load_dotenv()

# Start of streamlit application
st.title("PDF QnA Bot using LLM 💬")

# Intitialization
st.header("File upload")
file = st.file_uploader("Choose a file (PDF)", type="pdf", help="file to be parsed")

if file is not None:
    # @st.cache_data
    data = extract_text(file)

    # Create, display, search and query the embeddings
    embedding_store_file_name = file.name[:-4]
    vector_store = create_embeddings(
        data, embedding_store_file_name
    )

    # Storing the vector embeddings
    if store_embeddings(vector_store, embedding_store_file_name):
        st.success("Data saved successfully...", icon="✅")
    else:
        st.error("Operation not successful. Please reach out to support...", icon="❌")

else:
    st.error("Upload the file to proceed further", icon="🚨")

st.header("Chat with your PDF...")

user_input = st.text_input("Enter your query to retrieve answer from my knowledge(in case of multiple queries seprate by comma)...")

if user_input:
    response = chat_with_pdf(
        vector_store, user_input)
    st.write(response)
