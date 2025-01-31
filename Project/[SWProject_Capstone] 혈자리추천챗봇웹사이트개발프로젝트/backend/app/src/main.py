from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from models import cosine_retrieve as cr

def format_docs(docs):
    return '\n\n'.join([d.page_content for d in docs])

def run():

    query = ""
    docs = cr.calc_cosine(query)
    
    # Template
    template = '''Answer the question based only on the following context:
    {context}

    Question: {question}
    '''

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI(
        model='gpt-4o-mini',
        temperature=0,
        max_tokens=500,
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({'context' : (format_docs(docs)) , 'question' : query})
    return response