from dotenv import load_dotenv
load_dotenv()
import os
google_key = os.getenv('google_api')
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
    model = 'gemini-1.5-flash',
    google_api_key = google_key,
    max_tokens = 60
)
# messages = [
#     ('system',"you are a indian yoga instructor i will tell me about yoga"),
#     ('user','what is yoga')
# ]
# response = llm.invoke(messages)
# print(response.content)

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ('system','you are a math genius college teacher who is arrogant'),
    ('human','{input}')
])
# chain = prompt | llm
# response = chain.invoke({
#     'input': 'what is 1+1'
# })
# print(response.content)
import streamlit as slt
slt.title("enter math query")
from langchain_core.output_parsers import StrOutputParser
text = slt.text_input("enter your math query")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser
if text:
    slt.write(chain.invoke({'input':text}))
    
    
