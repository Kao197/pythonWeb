col_num = st.number_input("請輸入數字", min_value=1)
cols = st.columns(col_num)  # colums,cols[0]...cols[col_num-1]
for i in range(len(cols)):
    with cols[i]:
        st.button(
            f"按鈕{i+1}", key=f"button{i+10}"