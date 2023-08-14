import streamlit as st
import openai

# App title
st.set_page_config(page_title="text translate")

# Streamlit UI
st.title("AI Text Translator Chat")

# Sidebar for API key input
st.sidebar.title("OpenAI API Key")
api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")

# Check if API key is provided
if not api_key:
    st.warning("Please provide your OpenAI API key in the sidebar to use the translation feature.")
else:
    try:
        # Set OpenAI API key
        openai.api_key = api_key

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
