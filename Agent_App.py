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
    # Get the user input from session state
    user_input = st.session_state.get("user_input", "").strip()
    if not user_input:
        return  # Ignore empty inputs

    # Add user message to chat history
    st.session_state['messages'].append({"role": "user", "content": user_input})
    # Display the updated chat messages immediately
    display_messages()

    # Clear the input box
    st.session_state["user_input"] = ""  # This resets the input widget

    # Generate and display assistant's response
    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            try:
                response = healthcare_agent.run(user_input)  # Adjust this line to match your agent's method
                response_content = response.content if hasattr(response, "content") else str(response)
                st.markdown(response_content)
                # Add assistant's response to chat history
                st.session_state['messages'].append({"role": "assistant", "content": response_content})
            except Exception as e:
                error_message = f"An error occurred: {e}"
                st.error(error_message)
                # Add error message to chat history
                st.session_state['messages'].append({"role": "assistant", "content": error_message})

# Main function to run the app
def main():
    st.title("Healthcare and Insurance Chatbot")
    display_messages()

    # Input box for user queries
    # Use chat_input widget for user input handling
    user_input = st.chat_input("Type your query here...")
    if user_input:
        # Process input if user submits it via the chat input
        st.session_state["user_input"] = user_input
        process_input()

if __name__ == "__main__":
    main()
