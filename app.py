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
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"  # More powerful model
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

def generate_script(idea):
    # Premium prompt engineering
    prompt = f"""Create a VIRAL social media script about: {idea}
    
    REQUIREMENTS:
    1. HOOK (3-5 seconds): Must include [PAUSE] markers for editing
    2. SCRIPT (30-60 sec): Minimum 5 sentences with dramatic pacing
    3. CAPTION: 3 luxury hashtags + 1 CTA
    
    EXAMPLE FORMAT:
    🎯 HOOK: "What if I told you... [PAUSE] This changes everything! [PAUSE]"
    📜 SCRIPT: "First we... [beat] Then... [beat] The secret is..."
    📝 CAPTION: "Tag someone who needs this 👑 #LuxuryLife #GameChanger #Premium (Link in bio!)"
    """
    
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 500,
                    "temperature": 0.85,
                    "do_sample": True,
                    "wait_for_model": True
                }
            },
            timeout=45
        )
        
        if response.status_code == 200:
            full_output = response.json()[0]['generated_text']
            # Extract only the formatted parts
            formatted = []
            for line in full_output.split("\n"):
                if line.startswith(("🎯", "📜", "📝")):
                    formatted.append(line)
                elif "HOOK:" in line or "SCRIPT:" in line or "CAPTION:" in line:
                    formatted.append(line)
            
            return "\n\n".join(formatted) if formatted else create_fallback(idea)
        else:
            raise Exception(f"API Error: {response.text}")
            
    except Exception:
        return create_fallback(idea)

def create_fallback(idea):
    """Premium fallback content with proper structure"""
    topic = idea.split()[0] if idea else "luxury"
    return f"""
🎯 HOOK: "Stop scrolling! [PAUSE] This {topic} secret went viral... [PAUSE]"

📜 SCRIPT: "Here's why this works: [beat]\n1. First...\n2. Then...\n3. The key is...\n4. Most people miss...\n5. But you... [beat]"

📝 CAPTION: "Would you try this? 👇 #Viral{topic.capitalize()} #ContentGold #TrendingNow (DM for details!)"
    """

# --- User Input ---
idea = st.text_input("✨ Describe your premium content idea:", 
                    placeholder="e.g., 'Rolex watch unboxing experience'")

if st.button("Generate Viral Script", type="primary"):
    with st.spinner("🧠 Engineering virality..."):
        script = generate_script(idea)
        
        # Display with premium formatting
        st.success("🔥 Your Luxury Viral Blueprint:")
        st.markdown(f"```\n{script}\n```")  # Monospace for clarity
        
        # Add download button
        st.download_button(
            label="📥 Download Script",
            data=script,
            file_name="viral_script.txt",
            mime="text/plain"
        )

# --- User Input ---
idea = st.text_input("✨ Describe your premium content idea:", 
                    placeholder="e.g., 'Rolex watch unboxing experience'")

if st.button("Generate Viral Script", type="primary"):
    with st.spinner("Crafting luxury content..."):
        script = generate_script(idea)
        st.success("Here's your luxury viral script:")
        st.write(script)
