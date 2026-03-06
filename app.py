import streamlit as st
import sentry_sdk
from huggingface_hub import HfApi
import requests
import pandas as pd
import plotly.express as px

# 1. MONITORING SETUP
sentry_sdk.init(
    dsn=st.secrets["SENTRY_DSN"],
    traces_sample_rate=1.0,
)

st.set_page_config(page_title="Aura AI Architect", page_icon="⚖️", layout="wide")

# 2. THE HEARTBEAT (New Feature)
def check_hf_status():
    try:
        response = requests.get("https://huggingface.co/api/models", timeout=5)
        return "Online" if response.status_status == 200 else "Down"
    except:
        return "Offline"

# SIDEBAR STATUS
status = check_hf_status()
if status == "Online":
    st.sidebar.success(f"🟢 System Heartbeat: {status}")
else:
    st.sidebar.error(f"🔴 System Heartbeat: {status}")

# 3. HEADER & MAP
st.title("⚖️ Aura: Global AI Compliance Architect")
st.markdown("---")
st.subheader("🌐 Global AI Regulatory Risk Map")

map_data = pd.DataFrame({
    'Country': ['United States', 'China', 'European Union', 'United Kingdom', 'Canada', 'Brazil'],
    'Risk_Level': [3, 5, 5, 2, 3, 2],
    'Regulation': ['Executive Order 14110', 'Generative AI Measures', 'EU AI Act', 'AI Safety Institute', 'AIDA Bill', 'Bill 2338/23']
})

fig = px.choropleth(map_data, locations="Country", locationmode='country names',
                    color="Risk_Level", hover_name="Regulation",
                    color_continuous_scale=px.colors.sequential.Reds)
st.plotly_chart(fig, use_container_width=True)

# 4. HUGGING FACE AUDIT
st.subheader("🔍 Automated Model Audit")
model_id = st.text_input("Enter Hugging Face Model ID", "meta-llama/Llama-2-7b", help="Example: 'meta-llama/Llama-2-7b'")

if st.button("Run Compliance Scan"):
    try:
        api = HfApi()
        model_info = api.model_info(model_id)
        lic = model_info.cardData.get('license', 'Unknown')
        st.write(f"**License Detected:** {lic.upper()}")
        
        if "mit" in lic.lower() or "apache" in lic.lower():
            st.success("✅ COMPLIANCE VERIFIED")
        else:
            st.warning("⚠️ COMPLIANCE ALERT: Restrictive License")
            
    except Exception as e:
        sentry_sdk.capture_exception(e)
        st.error("Error detected. Details logged to Sentry.")
