
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_groq import ChatGroq
# import streamlit as st
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Set Langsmith tracking environment variables
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# # Get Groq API key
# groq_api_key = os.getenv('GROQ_API_KEY')

# # Initialize the Groq model
# llm_groq = ChatGroq(
#     groq_api_key=groq_api_key,
#     model_name="mixtral-8x7b-32768",
#     temperature=0.2
# )

# # Define the prompt template
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant. Please respond to the user's queries."),
#     ("user", "{question}")
# ])

# # Streamlit UI setup
# st.title('Langchain Demo with Groq API')
# input_text = st.text_input("Search the topic you want.")

# # Set custom background color
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #00FFFF;  # Cyan color
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Create the processing chain
# output_parser = StrOutputParser()
# chain = prompt | llm_groq | output_parser

# # Process user input and display response
# if input_text:
#     try:
#         response = chain.invoke({'question': input_text})
#         st.write(response)
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")


# import streamlit as st
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv

# load_dotenv()

# if 'processed' not in st.session_state:
#     st.session_state.processed = False

# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # Set the page configuration to wide layout
# st.set_page_config(page_title="Code-Bot", page_icon="🤖", layout="wide")

# # Custom CSS to adjust the look and feel of the chatbot window
# st.markdown("""
#     <style>
#         .main {
#             max-width: 1200px;  
#             margin: 0 auto;  
#         }
        
        
#         .chatbot-container {
#             position: fixed;
#             bottom: 20px;
#             right: 20px;
#             width: 350px;  /* Adjust the width of the floating chatbot */
#             padding: 15px;
#             border: 3px solid #4CAF50;
#             border-radius: 20px;
#             background-color: white;
#             box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
#         }

#         .chat-message {
#             padding: 1.5rem;
#             border-radius: 0.5rem;
#             margin-bottom: 1rem;
#         }

#         .user-message {
#             background-color: #f0f7ff;
#             border-left: 5px solid #3b82f6;
#             color: #1e40af;
#         }

#         .bot-message {
#             background-color: #f8fafc;
#             border-left: 5px solid #64748b;
#             color: #334155;
#         }
#     </style>
# """, unsafe_allow_html=True)

# def process_input():
#     if st.session_state.user_input and not st.session_state.processed:
#         user_input = st.session_state.user_input
#         st.session_state.messages.append({"role": "user", "content": user_input})
        
#         try:
#             response = chain.invoke({'question': user_input})
#             st.session_state.messages.append({"role": "assistant", "content": response})
#         except Exception as e:
#             st.error(f"An error occurred: {str(e)}")
#             st.session_state.messages.pop()
        
#         st.session_state.processed = True
#         st.session_state.user_input = ""

# def clear_chat():
#     st.session_state.messages = []
#     st.session_state.processed = False

# # Initialize Groq LLM model
# llm_groq = ChatGroq(
#     groq_api_key=os.getenv('GROQ_API_KEY'),
#     model_name="mixtral-8x7b-32768",
#     temperature=0.2
# )

# # Define the prompt for chatbot
# prompt = ChatPromptTemplate.from_messages([
#    ("system", "You are a friendly and helpful assistant that answers programming questions. Respond with code only, and provide solutions in a warm and polite manner."),
#     ("user", "{question}")

# ])

# output_parser = StrOutputParser()
# chain = prompt | llm_groq | output_parser

# # Title of the chatbot
# st.title("🤖 Code-Bot Assistant")

# # Display previous chat messages
# for message in st.session_state.messages:
#     message_class = "user-message" if message["role"] == "user" else "bot-message"
#     st.markdown(f"""
#         <div class="chat-message {message_class}">
#             <strong>{'You' if message["role"] == "user" else '🤖 Bot'}:</strong>
#             <div>{message["content"]}</div>
#         </div>
#     """, unsafe_allow_html=True)

# # Input box for asking questions and button to clear chat
# col1, col2 = st.columns([6, 1])
# with col1:
#     st.text_input(
#         "Ask a question:",
#         key="user_input",
#         on_change=process_input,
#         label_visibility="collapsed"
#     )
# with col2:
#     st.button("Clear Chat", on_click=clear_chat)

# # Reset processing flag
# if st.session_state.processed:
#     st.session_state.processed = False









import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

if 'processed' not in st.session_state:
    st.session_state.processed = False

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Set the page configuration to wide layout
st.set_page_config(page_title="Code-Bot", page_icon="🤖", layout="wide")

# Custom CSS to adjust the look and feel of the chatbot window
st.markdown("""
    <style>
        .main {
            max-width: 1200px;  
            margin: 0 auto;  
        }
        
        /* Floating Chatbot (Bottom-right corner) */
        .chatbot-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 350px;  /* Adjust the width of the floating chatbot */
            padding: 15px;
            border: 3px solid #4CAF50;
            border-radius: 20px;
            background-color: white;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        }

        .chat-message {
            padding: 1.5rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }

        .user-message {
            background-color: #f0f7ff;
            border-left: 5px solid #3b82f6;
            color: #1e40af;
        }

        .bot-message {
            background-color: #f8fafc;
            border-left: 5px solid #64748b;
            color: #334155;
        }
    </style>
""", unsafe_allow_html=True)

def process_input():
    if st.session_state.user_input and not st.session_state.processed:
        user_input = st.session_state.user_input
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            response = chain.invoke({'question': user_input})
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.session_state.messages.pop()
        
        st.session_state.processed = True
        st.session_state.user_input = ""

def clear_chat():
    st.session_state.messages = []
    st.session_state.processed = False

# Initialize Groq LLM model
llm_groq = ChatGroq(
    groq_api_key=os.getenv('GROQ_API_KEY'),
    model_name="mixtral-8x7b-32768",
    temperature=0.2
)

# Define the prompt for chatbot
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful programming assistant."),
    ("system", "Provide only code when user start question with 'provide python code for..'."),
    ("user", "{question}")
])

output_parser = StrOutputParser()
chain = prompt | llm_groq | output_parser

# Title of the chatbot
st.title("🤖 Code-Bot Assistant")

# Display previous chat messages
for message in st.session_state.messages:
    message_class = "user-message" if message["role"] == "user" else "bot-message"
    st.markdown(f"""
        <div class="chat-message {message_class}">
            <strong>{'You' if message["role"] == "user" else '🤖 Bot'}:</strong>
            <div>{message["content"]}</div>
        </div>
    """, unsafe_allow_html=True)

# Input box for asking questions and button to clear chat
col1, col2 = st.columns([6, 1])
with col1:
    st.text_input(
        "Ask a question:",
        key="user_input",
        on_change=process_input,
        label_visibility="collapsed"
    )
with col2:
    st.button("Clear Chat", on_click=clear_chat)

# Reset processing flag
if st.session_state.processed:
    st.session_state.processed = False
