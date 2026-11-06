# src/ingest.py
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

def criar_base_vetorial():
    caminho_arquivo = "data/sample.txt"
    if not os.path.exists(caminho_arquivo):
        print(f"Ficheiro {caminho_arquivo} não encontrado!")
        return

    loader = TextLoader(caminho_arquivo, encoding="utf-8")
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        docs, 
        embeddings, 
        persist_directory="./chroma_db"
    )

    print("Base vetorial criada e salva com sucesso na pasta ./chroma_db!")

if __name__ == "__main__":
    criar_base_vetorial()
