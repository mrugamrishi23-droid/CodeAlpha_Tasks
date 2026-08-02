import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# --- Page Configuration ---
st.set_page_config(page_title="AI Language Translator", page_icon="🌍", layout="centered")

# --- UI Header ---
st.title("🌍 AI Language Translation Tool")
st.markdown("Translate text between multiple languages and listen to the pronunciation!")

# --- Fetch Supported Languages ---
translator = GoogleTranslator()
languages_dict = translator.get_supported_languages(as_dict=True)
language_names = list(languages_dict.keys())

# --- User Interface: Language Selection ---
st.subheader("1. Select Languages")
col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox("Source Language:", ["auto"] + language_names)

with col2:
    default_target_index = language_names.index("spanish") if "spanish" in language_names else 0
    target_lang_name = st.selectbox("Target Language:", language_names, index=default_target_index)

# --- User Interface: Text Input ---
st.subheader("2. Enter Text")
text_to_translate = st.text_area("Type or paste the text you want to translate here:", height=150)

# --- Translation & Text-to-Speech Logic ---
if st.button("Translate Text", type="primary"):
    if text_to_translate.strip():
        try:
            with st.spinner("Translating..."):
                # 1. Map selected language names to their API codes
                src_code = "auto" if source_lang_name == "auto" else languages_dict[source_lang_name]
                tgt_code = languages_dict[target_lang_name]

                # 2. Process translation using the API
                translated_text = GoogleTranslator(source=src_code, target=tgt_code).translate(text_to_translate)
                
                # 3. Display the translated text clearly
                st.subheader("3. Translation Result")
                st.success(translated_text)
                
                # 4. Optional Feature: Text-to-Speech
                with st.spinner("Generating audio..."):
                    tts = gTTS(text=translated_text, lang=tgt_code, slow=False)
                    audio_file = "translation_audio.mp3"
                    tts.save(audio_file)
                    
                    st.markdown("**Listen to the translation:**")
                    st.audio(audio_file, format="audio/mp3")

        except Exception as e:
            st.error(f"An error occurred during translation: {e}")
    else:
        st.warning("Please enter some text before clicking translate.")

# --- Footer ---
st.markdown("---")
st.caption("Developed for CodeAlpha Artificial Intelligence Internship")