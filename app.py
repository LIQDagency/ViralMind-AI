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
    # Premium prompt template
    prompt = f"""Create a viral social media script about: {idea}
    
    FORMAT REQUIREMENTS:
    🎯 HOOK: [3-5 second attention-grabber with 2 PAUSE points]
    📜 SCRIPT: [30-60 second script with 5 key points]
    📝 CAPTION: [3 relevant hashtags + 1 CTA]
    
    EXAMPLE:
    🎯 HOOK: "You're doing it wrong! [PAUSE] Here's the luxury secret... [PAUSE]"
    📜 SCRIPT: "1. Start with... [beat] 
    2. Then add... [beat]
    3. The magic happens when... [beat]
    4. Most influencers miss... [beat]
    5. But you'll..."
    📝 CAPTION: "Who needs this? 👇 #{idea.replace(' ','')} #LuxuryHacks #ViralTips (Link in bio!)"
    """
    
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 600,
                    "temperature": 0.9,
                    "do_sample": True,
                    "wait_for_model": True
                }
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()[0]['generated_text']
            # Extract only the formatted parts
            return "\n\n".join([line for line in result.split("\n") 
                             if any(marker in line for marker in ["🎯", "📜", "📝", "HOOK:", "SCRIPT:", "CAPTION:"])])
        else:
            raise Exception(response.text)
            
    except Exception as e:
        st.toast("⚠️ Using premium fallback content", icon="✨")
        return f"""
🎯 HOOK: "This {idea.split()[0]} method went viral... [PAUSE] Here's why! [PAUSE]"

📜 SCRIPT: "1. The breakthrough... [beat]
2. Industry secrets... [beat]
3. Why this works... [beat]
4. Common mistakes... [beat]
5. Your advantage... [beat]"

📝 CAPTION: "Tag someone who needs this! #{idea.replace(' ','')} #ContentGold #TrendingNow (DM for details 👑)"
        """

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
