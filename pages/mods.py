import streamlit as st
from openai import OpenAI
import dotenv  # pip install python-dotenv -U
import os
import menu

menu.menu()
dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("寫程式AI")

if "history3" not in st.session_state:
    st.session_state.history3 = []

for message in st.session_state.history3:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入訊息")  # 聊天輸入框元件
if message:
    st.session_state.history3.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        messages=[
            {
                "role": "developer",
                "content": "你是一個寫程式機器人，只能用繁體中文(#zh-TW)和日文回應後續對話。",
            },
        ]
        + st.session_state.history3,
    )
    st.session_state.history3.append(
        {"role": "assistant", "content": completion.choices[0].message.content}
    )
    st.rerun()
