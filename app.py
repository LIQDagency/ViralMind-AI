import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from streamlit_lottie import st_lottie
import json

# --- Load Assets ---
def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# --- Luxury UI Setup ---
st.set_page_config(
    page_title="ViralMind AI",
    page_icon="🚀",
    layout="wide"
)

# --- 4K Animated Background ---
def add_bg():
    st.markdown(f"""
    <style>
    .stApp {{
        background: url("https://example.com/4k-bg.mp4");
        background-size: cover;
    }}
    </style>
    """, unsafe_allow_html=True)

add_bg()

# --- Gold Accent Styles ---
st.markdown("""
<style>
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

# --- Header with Logo ---
col1, col2 = st.columns([1, 3])
with col1:
    st.image("assets/logo.png", width=150)
with col2:
    st.title("VIRALMIND AI")
    st.caption("The World's First Emotion-Engineered Content Generator")

# --- AI Functionality ---
load_dotenv()
client = InferenceClient(token=os.getenv("HF_TOKEN"))

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
with st.container():
    idea = st.text_input("✨ Describe your premium content idea:", 
                        placeholder="e.g., 'Rolex watch unboxing experience'")
    
    if st.button("Generate Viral Script", type="primary"):
        with st.spinner("Crafting luxury content..."):
            script = generate_script(idea)
            
            st.balloons()
            st.success("Here's your luxury viral script:")
            
            # Luxury Result Display
            with st.expander("💎 PREMIUM SCRIPT", expanded=True):
                st.write(script)
            
            st.download_button("Download Script", script, file_name="luxury_script.txt")
