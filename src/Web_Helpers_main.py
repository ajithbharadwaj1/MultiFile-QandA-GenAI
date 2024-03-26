import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

import sys
sys.path.append('H:/github_projects/MultiFile-QandA-GenAI/MultiFile-QandA-GenAI')
sys.path.append('H:/github_projects/MultiFile-QandA-GenAI/MultiFile-QandA-GenAI/utils')
from utils.web_helpers import *
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def main():
    st.title("Value Input and Storage")

    # Initialize an empty list to store values
    values = []

    # Display an input field for the user to enter a value
    user_input = st.text_input("Enter values separated by commas:")

    # Check if the user has entered a value and submitted it
    if st.button("Submit"):
        if user_input:
            # Split the input string by commas and remove any leading/trailing spaces
            input_values = [value.strip() for value in user_input.split(",")]

            # Extend the values list with the input values
            values.extend(input_values)
            st.success(f"Values '{', '.join(input_values)}' added to the list!")

            
            

    # Display the current list of values
    st.write("Current List of Values:")
    st.write(values)
    a = load_pages(values)
    if a=='success':
        st.write("Successfully written the pages")
    display_q_and_a()

def display_q_and_a():
    st.write("Let's start Q and A")
    user_question = st.text_input("Ask a Question from the PDF Files")
    if user_question:
        ans = q_and_a(user_question)
        st.write(ans)







if __name__ == "__main__":
    main()





