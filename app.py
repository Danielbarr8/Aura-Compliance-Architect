import streamlit as st
import sentry_sdk
from huggingface_hub import HfApi
import requests

# 1. INTEGRATE SENTRY (Monitoring)
# Place your Sentry DSN in the Streamlit Secrets 
sentry_sdk.init(dsn=st.secrets["SENTRY_DSN"], traces_sample_rate=1.0)

st.set_page_config(page_title="Aura AI Compliance", page_icon="⚖️")

# 2. THE ARCHITECT DASHBOARD
st.title("Aura: AI Compliance & Risk Auditor")
st.markdown("---")

# 3. HUGGING FACE INTEGRATION (The Audit)
st.subheader("🔍 Model Compliance Check")
model_id = st.text_input("Enter Hugging Face Model ID", "meta-llama/Llama-2-7b")

if st.button("Audit Model"):
    try:
        api = HfApi()
        model_info = api.model_info(model_id)
        
        # Super Logic: Checking for license compliance
        license_info = model_info.cardData.get('license', 'Unknown')
        st.write(f"**Model Name:** {model_id}")
        st.write(f"**License Found:** {license_info}")
        
        if "mit" in license_info.lower() or "apache" in license_info.lower():
            st.success("Compliance Status: HIGH (Permissive License)")
        else:
            st.warning("Compliance Status: CAUTION (Restrictive or Unknown License)")
            
    except Exception as e:
        st.error("Audit Failed.")
        sentry_sdk.capture_exception(e) # Sends error to Sentry!

# 4. LINKEDIN INTEGRATION (The Report)
st.sidebar.header("📢 Professional Outreach")
if st.sidebar.button("Share Audit to LinkedIn"):
    # This uses the LinkedIn API to post your compliance success
    linkedin_url = "https://api.linkedin.com/v2/ugcPosts"
    # (API Auth Logic goes here using st.secrets["LINKEDIN_TOKEN"])
    st.sidebar.info("Aura is now connecting to LinkedIn to share this report...")
