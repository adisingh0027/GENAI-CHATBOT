import os
from dotenv import load_dotenv
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from google import genai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env!")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Configure Google GenAI client
client =genai.Client(api_key="GOOGLE_API_KEY")

# Simple string parser
class StrOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please provide feedback to the people."),
        ("user", "question: {question}")
    ]
)

# Streamlit UI
st.title("AI chatbot made by Adi :)")
input_text = st.text_input("Search the topic you want: and I will help you")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    client=client,
    model="gemini-2.5-flash-lite",   # or "gemini-1.5-chat"
    temperature=0.7
)

# Create LLM chain
chain = LLMChain(llm=llm, prompt=prompt, output_parser=StrOutputParser())

# Display output
if input_text:
    response = chain.run({'question': input_text})
    st.write(response)

