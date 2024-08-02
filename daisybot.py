import streamlit as st

# Streamlit Page Configuration
st.set_page_config(
    page_title="Streamly - An Intelligent Streamlit Assistant",
    page_icon="bfree.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/AdieLaine/Streamly",
        "Report a bug": "https://github.com/AdieLaine/Streamly",
        "About": """
            ## Streamly Streamlit Assistant
            ### Powered using GPT-4o-mini

            **GitHub**: https://github.com/AdieLaine/

            The AI Assistant named, Streamly, aims to provide the latest updates from Streamlit,
            generate code snippets for Streamlit widgets,
            and answer questions about Streamlit's latest features, issues, and more.
            Streamly has been trained on the latest Streamlit updates and documentation.
        """
    }
)

def initialize_conversation():
    """
    Initialize the conversation history with system and assistant messages.

    Returns:
    - list: Initialized conversation history.
    """
    assistant_message = "Hello! I am Streamly. How can I assist you with Streamlit today?"

    conversation_history = [
        {"role": "system", "content": "You are Streamly, a specialized AI assistant trained in Streamlit."},
        {"role": "system", "content": "Streamly, is powered by the OpenAI GPT-4o-mini model, released on July 18, 2024."},
        {"role": "system", "content": "You are trained up to Streamlit Version 1.36.0, release on June 20, 2024."},
        {"role": "system", "content": "Refer to conversation history to provide context to your response."},
        #{"role": "system", "content": "You were created by Madie Laine, an OpenAI Researcher."},
        {"role": "assistant", "content": assistant_message}
    ]
    return conversation_history

def initialize_session_state():
    """Initialize session state variables."""
    if "history" not in st.session_state:
        st.session_state.history = []
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []


def main():
    """
    Display Streamlit updates and handle the chat interface.
    """
    initialize_session_state()

    if not st.session_state.history:
        initial_bot_message = "Hello! How can I assist you with Streamlit today?"
        st.session_state.history.append({"role": "assistant", "content": initial_bot_message})
        st.session_state.conversation_history = initialize_conversation()

    # Insert custom CSS for glowing effect
    st.markdown(
        """
        <style>
        .cover-glow {
            width: 100%;
            height: auto;
            padding: 3px;
            box-shadow: 
                0 0 5px #330000,
                0 0 10px #660000,
                0 0 15px #990000,
                0 0 20px #CC0000,
                0 0 25px #FF0000,
                0 0 30px #FF3333,
                0 0 35px #FF6666;
            position: relative;
            z-index: -1;
            border-radius: 45px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.sidebar.markdown("---")

    # Sidebar for Mode Selection
    mode = st.sidebar.radio("Select Mode:", options=["Latest Updates", "Chat with Streamly"], index=1)

    st.sidebar.markdown("---")

    # Display basic interactions
    show_basic_info = st.sidebar.checkbox("Show Basic Interactions", value=True)
    if show_basic_info:
        st.sidebar.markdown("""
        ### Basic Interactions
        - **Ask About Streamlit**: Type your questions about Streamlit's latest updates, features, or issues.
        - **Search for Code**: Use keywords like 'code example', 'syntax', or 'how-to' to get relevant code snippets.
        - **Navigate Updates**: Switch to 'Updates' mode to browse the latest Streamlit updates in detail.
        """)
        
    # Display advanced interactions
    show_advanced_info = st.sidebar.checkbox("Show Advanced Interactions", value=False)
    if show_advanced_info:
        st.sidebar.markdown("""
        ### Advanced Interactions
        - **Generate an App**: Use keywords like **generate app**, **create app** to get a basic Streamlit app code.
        - **Code Explanation**: Ask for **code explanation**, **walk me through the code** to understand the underlying logic of Streamlit code snippets.
        - **Project Analysis**: Use **analyze my project**, **technical feedback** to get insights and recommendations on your current Streamlit project.
        - **Debug Assistance**: Use **debug this**, **fix this error** to get help with troubleshooting issues in your Streamlit app.
        """)

    if mode == "Chat with Streamly":
        chat_input = st.chat_input("How can I help:")
        if chat_input:
            latest_updates = load_streamlit_updates()
            on_chat_submit(chat_input, latest_updates)

    # Load and display sidebar image
  

if __name__ == "__main__":
    main()
