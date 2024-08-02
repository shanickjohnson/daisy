import streamlit as st
import openai

# Set up OpenAI API key (replace with your own key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_response(prompt):
    """Generate a response from the OpenAI API."""
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the latest model or adjust as needed
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    # Set up Streamlit app
    st.title("Interactive Chat Bot")

    # Create a session state to store the conversation history
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # Define the form for user input
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("You:", "")
        submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            # Add user input to conversation history
            st.session_state.conversation_history.append(f"You: {user_input}")

            # Generate response from the chat bot
            prompt = "\n".join(st.session_state.conversation_history) + "\nChat Bot:"
            response = generate_response(prompt)

            # Add chat bot response to conversation history
            st.session_state.conversation_history.append(f"Chat Bot: {response}")

    # Display conversation history
    for line in st.session_state.conversation_history:
        st.write(line)

if __name__ == "__main__":
    main()
