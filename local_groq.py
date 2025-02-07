from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Set Langsmith tracking environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Get Groq API key
groq_api_key = os.getenv('GROQ_API_KEY')



# Initialize the Groq model
llm_groq = ChatGroq(
    groq_api_key=groq_api_key,  
    model_name="mixtral-8x7b-32768",
    temperature=0.2
)


# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's queries."),
    ("user", "{question}")  # Simplified the template
])




# Streamlit UI setup
st.title('Langchain Demo with Groq API')
input_text = st.text_input("Search the topic you want.")

# Create the processing chain
output_parser = StrOutputParser()
chain = prompt | llm_groq | output_parser

# Process user input and display response
if input_text:
    try:
        response = chain.invoke({'question': input_text})
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

