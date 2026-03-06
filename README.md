# ⚖️ Aura: AI Compliance Architect
**The next-generation framework for autonomous AI Governance and Risk Auditing.**

Aura is a high-performance auditing tool designed to bridge the gap between AI development and regulatory compliance. Built with a "Security-First" mindset, it integrates real-time model data with cloud-based telemetry to ensure every AI model in your pipeline meets professional standards.

## 🚀 Key Features
* **Autonomous Model Auditing:** Direct integration with Hugging Face API to scan for licensing compliance (MIT, Apache 2.0, etc.).
* **Real-time Telemetry:** Powered by **Sentry** to monitor system integrity and catch architectural errors instantly.
* **Cloud-Native Architecture:** Deployed via **Streamlit Cloud** with **Cloudflare**-ready security protocols.
* **Risk Mitigation:** Automated alerting system for "Restrictive" license detection.

## 🛠️ The Tech Stack
- **Engine:** Python 3.13
- **Frontend:** Streamlit
- **Monitoring:** Sentry SDK
- **Data Source:** Hugging Face Hub
- **Security:** TOML-encrypted Secrets Management

## 🏗️ Installation & Setup
1. Clone the repository to your local machine.
2. Install dependencies: `pip install -r requirements.txt`.
3. Configure `secrets.toml` with your Sentry DSN and Hugging Face Token.
4. Run the app: `streamlit run app.py`.

## 📜 License
This project is licensed under the **MIT License** - providing professional-grade legal protection and open-source flexibility.
