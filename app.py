import streamlit as st
import sentry_sdk
from huggingface_hub import HfApi
import pandas as pd

# 1. MONITORING SETUP
# This ensures any errors are sent to Sentry immediately.
sentry_sdk.init(
    dsn=st.secrets["SENTRY_DSN"],
    traces_sample_rate=1.0,
)

st.set_page_config(page_title="Aura AI Auditor", page_icon="⚖️")

# 2. INTERFACE
st.title("Aura: AI Compliance Architect")
st.markdown("---")

# 3. CORE LOGIC: HUGGING FACE AUDIT
st.subheader("🔍 Automated Model Audit")
model_id = st.text_input("Enter Hugging Face Model ID", "meta-llama/Llama-2-7b")

if st.button("Run Compliance Scan"):
    with st.spinner("Auditing AI Model..."):
        try:
            api = HfApi()
            model_info = api.model_info(model_id)
            
            # Logic to check compliance
            lic = model_info.cardData.get('license', 'Unknown')
            downloads = model_info.downloads
            
            # Display Results in a Professional Table
            data = {
                "Audit Category": ["License", "Popularity", "Status"],
                "Result": [lic.upper(), f"{downloads:,} Downloads", "SCAN COMPLETE"]
            }
            df = pd.DataFrame(data)
            st.table(df)
            
            if "mit" in lic.lower() or "apache" in lic.lower():
                st.success("✅ COMPLIANCE VERIFIED: Permissive architecture detected.")
            else:
                st.warning("⚠️ COMPLIANCE ALERT: Restrictive license detected.")

        except Exception as e:
            st.error("Audit Interrupted. Details sent to Sentry.")
            sentry_sdk.capture_exception(e)

st.sidebar.info("Aura: Independent AI Governance Framework")
