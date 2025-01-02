import streamlit as st
from Agentic_manager import healthcare_agent  # Ensure this imports your agent correctly

# Initialize session state for storing chat history
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "assistant", "content": "Hello! How can I assist you with healthcare and insurance today?"}
    ]

# Function to display chat messages
def display_messages():
    for message in st.session_state['messages']:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Function to process user input
def process_input():
    user_input = st.session_state.user_input
    if user_input:
        # Add user message to chat history
        st.session_state['messages'].append({"role": "user", "content": user_input})
        # Display the updated chat messages
        display_messages()
        # Clear the input box
        st.session_state.user_input = ""
        # Generate and display assistant's response
        with st.chat_message("assistant"):
            with st.spinner("Processing..."):
                try:
                    response = healthcare_agent.run(user_input)  # Adjust this line to match your agent's method
                    st.markdown(response.content)
                    # Add assistant's response to chat history
                    st.session_state['messages'].append({"role": "assistant", "content": response.content})
                except Exception as e:
                    st.error(f"An error occurred: {e}")

# Main function to run the app
def main():
    st.title("Healthcare and Insurance Chatbot")
    display_messages()
    # Input box for user queries
    st.chat_input("Type your query here...", key="user_input", on_submit=process_input)

if __name__ == "__main__":
    main()
