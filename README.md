# PDF QnA Bot with OpenAI LLMs

Welcome to the Streamlit-based PDF Chatbot, leveraging OpenAI's Language Models for intuitive interactions. Users can upload PDF files, extract text content, and pose questions about the document. Key components of this project include:

- **PDF Text Extraction**: Utilizing PyPDF2 to extract text from PDF files, enabling seamless access to the document's content.

- **Text Splitting**: Implementation of a custom text splitter for breaking down extracted text into manageable chunks for efficient processing.

- **Embeddings and Vector Stores**: Generating embeddings using OpenAI's Language Models and creating a Vector Store with FAISS for effective text similarity searches.

- **Question Answering**: Integration of OpenAI's LLMs to provide precise answers to user queries about the PDF content.

- **Persistence**: Implementation of data persistence by storing generated embeddings for accelerated future queries.

## Getting Started

To run this project locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/khimraj/Pdf-QnA-Bot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Pdf-QnA-Bot
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file inside `app` directory and set your environment variables.

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Run the Streamlit app:

    ```bash
    streamlit run app/main.py
    ```

## Usage

1. Upload a PDF file using the "Browse Files" button.

2. Ask questions about the PDF file using the text input field.

3. The chatbot will use OpenAI's models to answer your questions based on the PDF content.
