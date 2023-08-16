import streamlit as st
import openai

# App title
st.set_page_config(page_title="text translate")

# Streamlit UI
st.title(" AI Text Translator Chat")

# Sidebar for API key input
with st.sidebar:
    st.title('💬 OpenAI Translator..')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai.api_key = st.secrets['OPENAI_API_KEY']
    else:
        openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
        if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('API key set successfully!', icon='👍')

        # Text input
user_input = st.text_input("Enter text to translate:")

        # Language selection
source_lang = st.selectbox("Select source language:", ["en"])
target_lang = st.selectbox("Select target language:", ["es", "fr", "de", "ja", "zh", "ru"])

        # Translate button
if st.button("Translate"):
            if user_input:
                try:
                    # Perform translation using OpenAI
                    response = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=f"Translate the following {source_lang} text to {target_lang}: '{user_input}'",
                        max_tokens=200
                    )
                    if 'choices' in response and response.choices:
                        translation = response.choices[0].text.strip()
                        st.write(f"**Source ({source_lang}):** {user_input}")
                        st.write(f"**Translation ({target_lang}):** {translation}")
                        st.success("Translation successful!")
                        st.balloons()
                    else:
                        st.error("Translation failed. Please check your input and try again.")
                except openai.error.OpenAIError as e:
                    st.error(f"OpenAI Error: {e}")
                except Exception as e:
                   st.error("An error occurred. Please check your OpenAI API key and try again.")

# Display information in the sidebar
st.sidebar.markdown("Powered by OpenAI API")
