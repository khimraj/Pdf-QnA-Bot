# Chat component of app

from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain import OpenAI

def chat_with_pdf(vector_store, user_input):
    """
        :param vector_store: vector embeddings of the input pdf
        :param user_input: user query that need to be answered
    """

    user_queries = user_input.split(",")
    bot_response = []
    for user_query in user_queries:
        similarity_score = vector_store.similarity_search_with_score(query=user_input, k=1)[0][1]
        
        print(similarity_score)
        if similarity_score<0.2:
            bot_response.append({'Question':user_query.strip(),
            'Answer': "Data Not Available"})
        else:
            docsearch = vector_store.similarity_search(query=user_input, k=1)
            print(docsearch)
            llm = OpenAI(model='gpt-3.5-turbo')
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docsearch, question=user_query)
                print(cb)
            bot_response.append({'Question':user_query.strip(),
            'Answer': response})
    return bot_response
