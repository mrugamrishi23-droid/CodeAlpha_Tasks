import streamlit as st
import json
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Download Required NLTK Data ---
# These are necessary for tokenization and text filtering
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

# --- Page Setup ---
st.set_page_config(page_title="CodeAlpha Support Bot", page_icon="💬", layout="centered")
st.title("💬 CodeAlpha FAQ Support Chatbot")
st.markdown("Ask me anything about the CodeAlpha internship program, perks, or submission rules!")

# --- 1. Load FAQ Dataset ---
@st.cache_data
def load_faqs():
    with open("faqs.json", "r") as file:
        return json.load(file)

faqs = load_faqs()
faq_questions = [item["question"] for item in faqs]
faq_answers = [item["answer"] for item in faqs]

# --- 2. NLP Preprocessing Function ---
def preprocess_text(text):
    """Tokenizes, lowercases, and removes punctuation/stopwords from text."""
    # Tokenize the text into words
    tokens = word_tokenize(text.lower())
    # Define punctuation and stop words to filter out
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)
    
    # Filter tokens
    cleaned_tokens = [
        w for w in tokens if w not in stop_words and w not in punctuation
    ]
    
    # Rejoin tokens into a clean string for vectorization
    return " ".join(cleaned_tokens)

# Preprocess all target FAQ questions ahead of time
preprocessed_faq_questions = [preprocess_text(q) for q in faq_questions]

# --- 3. Chat Logic & Similarity Matching ---
def get_bot_response(user_query):
    """Finds the most similar FAQ using TF-IDF and Cosine Similarity."""
    cleaned_query = preprocess_text(user_query)
    
    # If the user input is empty after cleaning, handle gracefully
    if not cleaned_query.strip():
        return "I'm sorry, I didn't quite catch that. Could you please rephrase your question?"

    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    
    # Combine the preprocessed dataset questions with the new user query
    all_texts = preprocessed_faq_questions + [cleaned_query]
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Compute cosine similarity between the user query (last item) and all FAQ questions
    vectors = tfidf_matrix.toarray()
    query_vector = vectors[-1].reshape(1, -1)
    faq_vectors = vectors[:-1]
    
    similarities = cosine_similarity(query_vector, faq_vectors)[0]
    
    # Find the index of the highest similarity score
    best_match_idx = similarities.argmax()
    highest_score = similarities[best_match_idx]
    
    # Define a confidence threshold (e.g., 0.20). If match is lower, trigger fallback response.
    if highest_score > 0.20:
        return faq_answers[best_match_idx]
    else:
        return "I'm sorry, I couldn't find a direct match for that question. Please try asking about 'perks', 'submission rules', 'GitHub naming', or contact support directly at services@codealpha.tech."

# --- 4. Streamlit Interactive Chat Interface ---
# Initialize session state for persistent chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your CodeAlpha Assistant. How can I help you with your internship tasks today?"}
    ]

# Display the ongoing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Handle new user input
if user_input := st.chat_input("Type your question here..."):
    # Display user message in chat message container
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
        
    # Generate and display bot response
    bot_response = get_bot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)