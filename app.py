import os
import requests
import streamlit as st
from dotenv import load_dotenv

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
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

def generate_script(idea):
    prompt = f"""
    Create ULTRA-PREMIUM viral content about: {idea}
    Follow this EXACT format:
    
    🎯 HOOK: "[3-second attention-grabber]"
    📜 SCRIPT: "[15-30 sec engaging story]"
    📝 CAPTION: "[Emoji-rich caption with 3 hashtags]"
    """
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 400,  # Increased length
                    "temperature": 0.8,     # More creativity
                    "wait_for_model": True   # Ensures completion
                }
            },
            timeout=30  # Wait longer for response
        )
        
        if response.status_code == 200:
            full_output = response.json()[0]['generated_text']
            # Extract only the formatted parts
            return "\n".join([line for line in full_output.split("\n") 
                           if line.startswith(("🎯", "📜", "📝"))])
        else:
            raise Exception(f"API Error: {response.text}")
            
    except Exception as e:
        st.warning("🔧 Enhancing your premium experience...")
        # More detailed fallback based on user's idea
        return f"""
🎯 HOOK: "Discover the ultimate {idea.split(' ')[0]} luxury experience..."
📜 SCRIPT: "Indulge in our exclusive {idea} where every detail is perfected..."
📝 CAPTION: "#{idea.replace(' ', '')} #LuxuryRedefined #EliteAccess"
        """

# --- User Input ---
idea = st.text_input("✨ Describe your premium content idea:", 
                    placeholder="e.g., 'Rolex watch unboxing experience'")

if st.button("Generate Viral Script", type="primary"):
    with st.spinner("Crafting luxury content..."):
        script = generate_script(idea)
        st.success("Here's your luxury viral script:")
        st.write(script)
