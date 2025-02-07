import streamlit as st
from openai import OpenAI
import dotenv  # pip install python-dotenv -U
import os
import menu

menu.menu()
dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("猜迷小游戲")

if "history2" not in st.session_state:
    st.session_state.history2 = []

for message in st.session_state.history2:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入訊息")  # 聊天輸入框元件
if message:
    st.session_state.history2.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        temperature=1,
        messages=[
            {
                "role": "developer",
                "content": """
                與使用者玩猜謎遊戲。您必須首先想出一個謎題，並保持主題秘密，不在語言中透露。 在回應使用者的猜測時，只能說「是」或「否」作為提示，避免提供過多資訊。 每回合應有一個獨特的謎題，且您應只用繁體中文（#zh-TW）和日文（#ja-JP）回應。

# 注意事項

- 避免直接揭露謎題的主題。
- 確保每個謎題在每回合中都是不同的。
                    
                    """,
            },
        ]
        + st.session_state.history2,
    )
    st.session_state.history2.append(
        {"role": "assistant", "content": completion.choices[0].message.content}
    )
    st.rerun()
