import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import streamlit as st
from llmproviders import run_llm

st.set_page_config(page_title="🤖 My first AI chat Assistant", page_icon=":robot_face:", layout="centered")
st.title ("🤖 -> My first AI chat Assistant")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state["history"]=[{"role": "assistant", "content": "How can I help you today?"}]

# Display chat history
for msg in st.session_state["history"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input    
if prompt := st.chat_input("Type your message here..."):
    # add user message
    st.session_state["history"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    reply=run_llm(st.session_state["history"])

    # add assistant response to memory
    st.session_state["history"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)


if st.button("Clear Chat ♻️"):
    st.session_state["history"] = [{"role": "assistant", "content": "How can I help you today?"}]
    st.rerun()