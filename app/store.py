# Store vector embeddings locally

import pickle

def store_embeddings(embeddings, embedding_store_file_name):
    """
        :param embeddings: the vector embeddings of input PDF file
        :param embedding_store_file_name: name of file in which vector embeddings will be stored
    """
    with open(f"{embedding_store_file_name}.pkl", "wb") as f:
        pickle.dump(embeddings, f)
    return True
