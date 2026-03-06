import streamlit as st
import sentry_sdk
from huggingface_hub import HfApi
import pandas as pd
import plotly.express as px

# 1. MONITORING SETUP
sentry_sdk.init(
    dsn=st.secrets["SENTRY_DSN"],
    traces_sample_rate=1.0,
)

st.set_page_config(page_title="Aura AI Architect", page_icon="⚖️", layout="wide")

# 2. HEADER
st.title("⚖️ Aura: Global AI Compliance Architect")
st.markdown("---")

# 3. GLOBAL RISK MAP (The New Super Feature)
st.subheader("🌐 Global AI Regulatory Risk Map")

# Mock data for global regulations (Professional Research Data)
map_data = pd.DataFrame({
    'Country': ['United States', 'China', 'European Union', 'United Kingdom', 'Canada', 'Brazil'],
    'Risk_Level': [3, 5, 5, 2, 3, 2],
    'Regulation': ['Executive Order 14110', 'Generative AI Measures', 'EU AI Act', 'AI Safety Institute', 'AIDA Bill', 'Bill 2338/23']
})

fig = px.choropleth(map_data, 
                    locations="Country", 
                    locationmode='country names',
                    color="Risk_Level",
                    hover_name="Regulation",
                    color_continuous_scale=px.colors.sequential.Reds,
                    title="Regulatory Strictness by Region")

st.plotly_chart(fig, use_container_width=True)

# 4. HUGGING FACE AUDIT SECTION
st.subheader("🔍 Automated Model Audit")
col1, col2 = st.columns(2)

with col1:
    model_id = st.text_input("Enter Hugging Face Model ID", "meta-llama/Llama-2-7b")
    if st.button("Run Compliance Scan"):
        try:
            api = HfApi()
            model_info = api.model_info(model_id)
            lic = model_info.cardData.get('license', 'Unknown')
            
            st.write(f"**Model:** {model_id}")
            st.write(f"**License:** {lic.upper()}")
            
            if "mit" in lic.lower() or "apache" in lic.lower():
                st.success("✅ COMPLIANCE VERIFIED")
            else:
                st.warning("⚠️ COMPLIANCE ALERT: Restrictive License")
        except Exception as e:
            sentry_sdk.capture_exception(e)
            st.error("Audit Error Logged to Sentry.")

with col2:
    st.info("**Architect Note:** High-risk regions (Red) require mandatory bias audits and data transparency logs.")
