import streamlit as st
from utils import get_chat_response

st.title('Hello llama3.2 😭')

with st.sidebar:
    api_key = st.text_input('API Key:', type='password')
    st.markdown("[api key](https://platform.openai.com/account/api-keys)")

if "memory" not in st.session_state:
    st.session_state["messages"] = [
      {"role": "ai",
       "content": "唷？你有問題？哇係 llama3.2"}
    ]

for message in st.session_state["messages"]:
    if message["role"] == "ai":
        st.write(f'🦙: {message["content"]}')
    else:
        st.write(f'👤: {message["content"]}')

prompt = st.chat_input()
if prompt:
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(f'👤: {prompt}')

    with st.spinner("AI is thinking..."):
        response = get_chat_response(prompt)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(f'🦙: {response}')