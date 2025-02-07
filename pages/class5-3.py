import streamlit as st
from openai import OpenAI
import dotenv  # pip install python-dotenv -U
import os
import menu

menu.menu()
dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("猜迷小游戲")

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入訊息")  # 聊天輸入框元件
if message:
    st.session_state.history.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        temperature=1,
        messages=[
            {
                "role": "developer",
                "content": """
                只能用繁體中文(#zh-TW)和日文回應後續對話。
                請跟使用者玩一場猜謎遊戲，你需要先描述題目，接下來依照使用者回應的猜測給予提示
                提示只能說[是]與[否]，不可以提供太多資訊
                答案和迷題由你想(每次都要不一樣的迷題)
                    
                    """,
            },
        ]
        + st.session_state.history,
    )
    st.session_state.history.append(
        {"role": "assistant", "content": completion.choices[0].message.content}
    )
    st.rerun()
