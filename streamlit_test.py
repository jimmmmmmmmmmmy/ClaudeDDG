import streamlit as st
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.anthropic import Claude
import sys

def main():
    st.title("Claude Web Search")

    # Sidebar for configuration
    st.sidebar.header("Configuration")
    
    # API Key input
    anthropic_api_key = st.sidebar.text_input("Enter your Anthropic API key:", type="password")
    
    # Temperature slider
    temperature = st.sidebar.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.9, step=0.1)
    
    # Max tokens slider
    max_tokens = st.sidebar.slider("Max Tokens:", min_value=100, max_value=4096, value=1024, step=100)
    
    # Custom system prompt input
    default_prompt = ("You are a helpful assistant with access to web search. "
                      "Always provide concise and accurate information. "
                      "Please limit 'meta-responses' to the user to as few words as possible.")
    system_prompt = st.sidebar.text_area("Custom System Prompt:", value=default_prompt, height=150)

    if anthropic_api_key:
        assistant = Assistant(
            llm=Claude(
                model="claude-3-5-sonnet-20240620",
                max_tokens=max_tokens,
                temperature=temperature,
                api_key=anthropic_api_key
            ),
            tools=[DuckDuckGo()],
            show_tool_calls=True
        )

        query = st.text_area("Search:", height=100)

        if st.button("Submit"):
            if query:
                full_prompt = f"{system_prompt}\n\nUser query: {query}"

                try:
                    response_placeholder = st.empty()
                    full_response = ""
                    for chunk in assistant.run(full_prompt, stream=True):
                        full_response += chunk
                        response_placeholder.markdown(full_response + "▌")
                    response_placeholder.markdown(full_response)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}. Please check your API key and try again.")

    else:
        st.warning("Please enter your Anthropic API key in the sidebar to use the application.")

    st.markdown("<br>" * 5, unsafe_allow_html=True)

    if st.button("Exit App", key="exit_button"):
        st.success("Exiting the app... You can close this window.")
        sys.exit()

if __name__ == "__main__":
    main()
