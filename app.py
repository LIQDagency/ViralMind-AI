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
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

def generate_script(idea):
    # Premium prompt engineering
    prompt = f"""Create a VIRAL 60-second social media script about: {idea}
    
    REQUIREMENTS:
    1. HOOK (3-5 sec): Must include [PAUSE] markers and be shocking/curiosity-driven
    2. SCRIPT (5 key points): Each point separated by [beat] with concrete examples
    3. CAPTION: 3 custom hashtags + 1 CTA
    
    EXAMPLE FOR "Luxury Cars":
    🎯 HOOK: "You're photographing cars wrong! [PAUSE] This $0 trick went viral... [PAUSE]"
    📜 SCRIPT: "1. Find the golden hour light [beat] 
    2. Use a polarizer for reflections [beat]
    3. Shoot from 3/4 angles [beat]
    4. Edit ONLY these settings [beat]
    5. The dealership secret nobody shares"
    📝 CAPTION: "Which car needs this? 👇 #LuxuryCarPhotography #ProShots #CarGram (Free guide 🔗)"
    """
    
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 650,
                    "temperature": 0.85,
                    "repetition_penalty": 1.2,
                    "wait_for_model": True
                }
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()[0]['generated_text']
            
            # Enforce minimum quality standards
            if all(marker in result for marker in ["🎯", "📜", "📝"]):
                return result
            else:
                raise Exception("Incomplete response format")
        else:
            raise Exception(f"API Error: {response.text}")
            
    except Exception as e:
        st.toast("✨ Using enhanced premium template", icon="💎")
        return create_dynamic_fallback(idea)

def create_dynamic_fallback(idea):
    """Generates high-quality fallback content"""
    topic = idea.split()[0] if idea else "luxury"
    return f"""
🎯 HOOK: "Most {topic} content fails because... [PAUSE] Until now! [PAUSE]"

📜 SCRIPT: "1. The {topic} breakthrough... [beat]
2. Industry secrets exposed... [beat]
3. Why this works today... [beat]
4. Common mistakes to avoid... [beat]
5. Your unfair advantage... [beat]"

📝 CAPTION: "Who needs this? 👇 #{topic}Secrets #Viral{topic.capitalize()} #TrendingNow (DM 'GUIDE' 📩)"
    """

# --- User Input ---
idea = st.text_input(
    "✨ Describe your viral content idea:",
    placeholder="e.g., 'Luxury watch photography tricks'",
    key="unique_input_key"
)

if st.button("Generate Viral Script", type="primary", key="unique_button_key"):
    with st.spinner("🔮 Engineering virality..."):
        script = generate_script(idea)
        
        # Premium display
        st.success("💎 Your Viral Masterpiece:")
        st.markdown("""
        <div style="
            background: #1E1E2D;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #FFD700;
            font-family: monospace;
            white-space: pre-wrap;
        ">{}</div>
        """.format(script), unsafe_allow_html=True)

# --- User Input (WITH UNIQUE KEY) ---
idea = st.text_input(
    "✨ Describe your premium content idea:",
    placeholder="e.g., 'Rolex watch unboxing experience'",
    key="main_input"  # 👈 Unique key fix
)

if st.button("Generate Viral Script", type="primary", key="main_button"):
    with st.spinner("🧠 Engineering virality..."):
        script = generate_script(idea)
        
        # Display with premium formatting
        st.success("🔥 Your Luxury Viral Blueprint:")
        st.code(script, language="markdown")
        
        # Download button
        st.download_button(
            "📥 Download Script",
            script,
            file_name=f"viral_script_{idea[:20]}.txt",
            mime="text/plain"
        )
