from dotenv import load_dotenv
load_dotenv()
import os
from langchain_community.llms import Ollama
import streamlit as slt
google_key = os.getenv('google_api')

llm = Ollama(model = 'deepseek-r1:1.5b')
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ('system','you are a math genius college teacher who is arrogant'),
    ('human','{input}')
])
import streamlit as slt
slt.title("enter math query")
from langchain_core.output_parsers import StrOutputParser
text = slt.text_input("enter your math query")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser
if text:
    slt.write(chain.invoke({'input':text}))