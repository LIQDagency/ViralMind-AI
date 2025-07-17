import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# --- Luxury UI Setup ---
st.set_page_config(
    page_title="ViralMind AI",
    page_icon="🚀",
    layout="wide"
)

# --- Gold Accent Styles ---
st.markdown("""
<style>
.stApp {
    background: #0F0F1A;
}
.stTextInput>div>div>input {
    background: rgba(15, 15, 30, 0.7) !important;
    color: white !important;
    border: 1px solid #FFD700 !important;
}
.stButton>button {
    background: linear-gradient(90deg, #FFD700, #FFAA00) !important;
    color: black !important;
    font-weight: bold !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://via.placeholder.com/150x50/0F0F1A/FFD700?text=YOUR+LOGO", width=150)
with col2:
    st.title("VIRALMIND AI")
    st.caption("The World's First Emotion-Engineered Content Generator")

# --- AI Functionality ---
load_dotenv()
client = InferenceClient(token=os.getenv("HF_TOKEN"), model="mistralai/Mistral-7B-Instruct-v0.1")

def generate_script(idea):
    prompt = f"""
    Create ULTRA-PREMIUM viral content about: {idea}
    Include:
    1. HOOK (3 seconds, luxury tone)
    2. SCRIPT (15-30 sec, high-end narrative)
    3. CAPTION (with luxury hashtags)
    """
    return client.text_generation(prompt, max_new_tokens=300)

# --- User Input ---
idea = st.text_input("✨ Describe your premium content idea:", 
                    placeholder="e.g., 'Rolex watch unboxing experience'")

if st.button("Generate Viral Script", type="primary"):
    with st.spinner("Crafting luxury content..."):
        script = generate_script(idea)
        st.success("Here's your luxury viral script:")
        st.write(script)
