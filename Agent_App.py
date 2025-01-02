import streamlit as st
from dotenv import load_dotenv 
from Agentic_manager import healthcare_agent
load_dotenv()



import streamlit as st
from streamlit_chat import message  # Streamlit-Chat for a chatbot UI
from Agentic_manager import healthcare_agent  # Import your healthcare agent

# Initialize session state for storing chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I help you with healthcare and insurance today?"}]

def main():
    st.title("Healthcare and Insurance Chatbot")
    
    # Display chat messages from history
    for msg in st.session_state["messages"]:
        if msg["role"] == "assistant":
            message(msg["content"], is_user=False)
        else:
            message(msg["content"], is_user=True)

    # User input area
    user_input = st.text_input("Type your query here...", key="user_input", on_change=process_input)

def process_input():
    # Get user input
    user_input = st.session_state["user_input"].strip()
    if not user_input:
        st.warning("Please enter a valid question.")
        return

    # Add user message to history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.session_state["user_input"] = ""  # Clear input box

    # Get agent's response
    try:
        with st.spinner("Processing your question..."):
            response = healthcare_agent.run(user_input)
        st.session_state["messages"].append({"role": "assistant", "content": response.content})
    except Exception as e:
        st.session_state["messages"].append({"role": "assistant", "content": f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    main()