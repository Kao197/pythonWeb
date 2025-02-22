## Python 課程筆記

### 1. **成績登記系統**
此系統使用 `dict` 結構儲存學生的各科成績，每個科目包含 3 次測驗分數。

#### **程式碼**
```python
# 成績登記系統，key 為學生姓名，value 為成績資料
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65], "英文": [95, 85, 75]},
    "小美": {"國文": [88, 78, 68], "數學": [83, 73, 63], "英文": [93, 83, 73]},
    "小華": {"國文": [86, 76, 66], "數學": [81, 71, 61], "英文": [91, 81, 71]},
}
```

#### **基本查詢**
```python
# 取得小明的數學成績
print(grade["小明"]["數學"])  # [85, 75, 65]

# 取得小美的第一次英文成績
print(grade["小美"]["英文"][0])  # 93

# 取得小華的第二次國文成績
print(grade["小華"]["國文"][1])  # 76
```

#### **計算平均成績**
```python
# 計算每位學生的國文平均成績
for name, subject in grade.items():
    avg = sum(subject["國文"]) / len(subject["國文"])
    print(f"{name} 的國文段考平均成績為 {avg}")

for name, subject in grade.items():
    total = 0
    for score in subject.values():
        total += sum(score)
        avg = total / 9  # 每位學生共有 9 次考試成績 (3 科 x 3 次)
    print(f"{name} 的總平均成績為 {avg}")
```

#### **計算全校各科平均成績**
```python
# 找出所有科目
subjects = list(grade["小明"].keys())

# 建立字典存放各科目成績
avg_grade = {subject: [] for subject in subjects}

# 彙總各科目成績
for subject in subjects:
    for name, scores in grade.items():
        avg_grade[subject] += scores[subject]

# 計算各科平均成績
for subject, scores in avg_grade.items():
    avg = sum(scores) / len(scores)
    print(f"{subject} 的平均成績為 {avg}")
```

---

### 2. **OpenAI Chatbot 程式**
本段程式碼使用 OpenAI API 並結合 `Streamlit` 建立簡單聊天機器人。

#### **安裝必要套件**
```bash
pip install openai streamlit python-dotenv
```

#### **環境變數設定**
需在 `.env` 檔案中設定 `OPENAI_API_KEY`：
```
OPENAI_API_KEY=your_api_key_here
```

#### **基本聊天機器人**
```python
import streamlit as st
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("聊天AI")

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入訊息")
if message:
    st.session_state.history.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "只能使用繁體中文(#zh-TW)和日文回應。"},
        ] + st.session_state.history,
    )
    st.session_state.history.append({"role": "assistant", "content": completion.choices[0].message.content})
    st.rerun()
```

---

### 3. **猜謎遊戲機器人**
此程式讓 AI 生成隨機謎題，使用者需猜測答案，AI 只回應 **「是」** 或 **「否」**。

#### **程式碼**
```python
import streamlit as st
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("猜謎遊戲")

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入答案")
if message:
    st.session_state.history.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        temperature=1,
        messages=[
            {
                "role": "developer",
                "content": """
                只能用繁體中文(#zh-TW)和日文回應。
                你需要設計一個猜謎遊戲，每次都生成不同的謎題。
                當玩家猜測時，只能回答「是」或「否」，不能提供額外線索。
                """,
            },
        ] + st.session_state.history,
    )
    st.session_state.history.append({"role": "assistant", "content": completion.choices[0].message.content})
    st.rerun()
```

---

### **結論**
1. **成績管理系統** 使用 Python 的 `dict` 來儲存與處理學生的成績，並計算個人及全校平均。
2. **OpenAI 聊天機器人** 使用 `Streamlit` 開發，能根據對話歷史與 API 回應來互動。
3. **猜謎遊戲機器人** 透過 `OpenAI API` 生成隨機謎題，並限制 AI 回應方式。

這些程式展示了 **Python 字典操作、API 互動、GUI 應用與資料處理** 等核心概念，適合作為學習範例。