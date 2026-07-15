# 🚀 My first AI Chat Assistant from Scratch

Welcome! This repository marks the very first project in my **AI Learning Series**, where I build hands-on AI tools from scratch and document my journey. 

This project is a functional, real-time AI Chat Assistant that supports integration with top-tier language models while maintaining a seamless conversation state.

---

## 🔧 What I Built & Key Features
- **Dual-Model Support:** Fully compatible with both **OpenAI GPT** as the primary LLM and **Gemini 2.5 Flash** as an alternative model option.
- **Session State Management:** The assistant retains context and remembers earlier questions across the entire active session until explicitly cleared.
- **Real-Time Q&A:** Successfully tested with general knowledge and complex science questions.
- **Streamlit-Based UI:** A clean, intuitive, and highly responsive local web interface designed for smooth interaction.
- **State Reset Automation:** Includes a dedicated "Clear Chat" option to wipe session states instantly and start fresh.

---

## 💡 Key Technical Insights
Getting a chat interface right is about more than just hitting an API endpoint. The real engineering challenge lies in **state management**. Managing user/assistant message histories and maintaining context cleanly across a session is what makes an AI assistant feel smooth. This project serves as the foundational architecture required for building advanced, agent-based AI tools.

---

## 🛠️ Tech Stack & Architecture
- **Frontend / UI:** Streamlit (Python)
- **AI Models:** OpenAI API (GPT), Google AI Studio API (Gemini 2.5 Flash)
- **Environment Management:** Virtual Environments (`.myenv`)
- **Version Control:** Git & GitHub

---

## 📦 Local Setup Instructions

Follow these steps to run a local copy of this chat assistant on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com
cd 3-Capstoneproject
```

### 2. Setup Virtual Environment & Dependencies
Create and activate your isolated Python environment, then install the required packages:
```bash
# Initialize and activate environment
python3 -m venv .myenv
source .myenv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 3. Configure Your Environment Variables
Create a file named `.env` in your root folder and supply your API keys (this file is fully secured and ignored by Git):
```text
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
```

### 4. Run the Application
Launch the local Streamlit application server:
```bash
streamlit run app.py
```

### 🔄 Switching Between Models
To switch the underlying LLM from OpenAI to Gemini (or vice versa):
1. Stop the running server in your terminal by pressing `Ctrl + C`.
2. Open your source code file and update the model configuration variable to your choice.
3. Save the file.
4. Restart the application by running `streamlit run app.py` again.

---

## 🛡️ Repository Hygiene & Best Practices
This project is built following professional version control standards:
- **Private Credentials (`.env`):** Strictly restricted to the local environment to prevent accidental credential leakage.
- **System Trash / Artifacts:** Hidden system files like `__pycache__/`, `.DS_Store`, and `.agents/` are managed and blocked via `.gitignore`.
- **Environment Isolation:** Local dependencies are kept inside `.myenv/` and mapped neatly to a lightweight `requirements.txt` file.

---

## 👤 Author
- **Sumeet Saharan**
- GitHub: [@SumeetSaharan82](https://github.com)

