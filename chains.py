from langchain.chains import RetrievalQA

def get_qa_chain(llm, retriever):
    return RetrievalQA(llm=llm, retriever=retriever)