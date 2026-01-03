import streamlit as st
import google.generativeai as genai

st.title("MANIBOT")

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ✅ Use supported model
model = genai.GenerativeModel("gemini-2.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        conversation = "\n".join(
            [f"{m['role']}: {m['content']}" for m in st.session_state.messages]
        )
        response = model.generate_content(conversation)
        reply = response.text
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
