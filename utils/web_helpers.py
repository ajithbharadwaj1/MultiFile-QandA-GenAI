import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

def load_pages(webs):
    loader = WebBaseLoader(webs)
    docs = loader.load()
    # Combine doc
    combined_docs = [doc.page_content for doc in docs]
    text = " ".join(combined_docs)
    # Split them
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
    splits = text_splitter.split_text(text)
    
    vector_store = FAISS.from_texts(splits, embedding=embeddings)
    vector_store.save_local("../vector_db/Web_Vector_DB")
    return 'success'


def q_and_a(question):
    # Build a QA chain
    vectordb=FAISS.load_local("../vector_db/Web_Vector_DB",embedding=embeddings)
    qa_chain = RetrievalQA.from_chain_type(
    llm=ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3),
    chain_type="stuff",
    retriever=vectordb.as_retriever()
)






    

