import streamlit as st
from streamlit_chat import message  # Ensure this is installed: pip install streamlit-chat
from Agentic_manager import healthcare_agent  # Import your healthcare agent

# Initialize session state for storing chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! How can I help you with healthcare and insurance today?"}
    ]

def main():
    st.title("Healthcare and Insurance Chatbot")

    # Display chat messages from history
    for msg in st.session_state["messages"]:
        if msg["role"] == "assistant":
            message(msg["content"], is_user=False)
        else:
            message(msg["content"], is_user=True)

    # User input area with form submission
    with st.form(key="user_input_form", clear_on_submit=True):
        user_input = st.text_input("Type your query here...", key="user_input")
        submit_button = st.form_submit_button(label="Send")

    # Process input when the form is submitted
    if submit_button and user_input:
        process_input(user_input)

def process_input(user_input):
    # Add user message to history
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Display the user's message immediately
    message(user_input, is_user=True)

    # Placeholder for the assistant's response
    response_placeholder = st.empty()

    # Display a spinner while processing
    with st.spinner("Processing your question..."):
        try:
            # Simulate processing time (replace with actual agent call)
            response = healthcare_agent.run(user_input)
            # Update the placeholder with the assistant's response
            response_placeholder.markdown(response.content)
            # Add assistant's response to history
            st.session_state["messages"].append({"role": "assistant", "content": response.content})
        except Exception as e:
            response_placeholder.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
