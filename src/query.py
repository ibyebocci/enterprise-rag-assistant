# src/query.py
import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def perguntar_ao_rag(pergunta):
    if not os.environ.get("OPENAI_API_KEY"):
        print("Erro: A variável de ambiente OPENAI_API_KEY não está configurada.")
        return

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(
        persist_directory="./chroma_db", 
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    resposta = qa_chain.invoke({"query": pergunta})

    print(f"\nPergunta: {pergunta}")
    print(f"Resposta da IA: {resposta['result']}\n")

if __name__ == "__main__":
    pergunta_teste = "Qual é o limite diário de gastos com refeições?"
    perguntar_ao_rag(pergunta_teste)
