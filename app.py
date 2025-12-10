import streamlit as st
import requests
import json

# 后端 API 的地址
API_URL = "http://127.0.0.1:8000/chat"

# --- 页面配置 ---
st.set_page_config(page_title="IC-Expert 芯片助手", layout="wide")

st.title("🧐 IC-Expert: 集成电路专业知识库助手")

# --- 侧边栏：文件上传 ---
with st.sidebar:
    st.header("📚 知识库管理")
    uploaded_file = st.file_uploader("上传 IC 技术手册 (PDF)", type=["pdf"])
    if uploaded_file:
        st.success(f"已加载: {uploaded_file.name}")
        # 注意：这里我们暂时只做前端展示，上传逻辑 Day 9 才会和后端打通
        # 现在默认后端已经有了 Day 2 那个 verilog_guide.pdf

# --- 主界面：聊天记录 ---
# 初始化 session_state 用来保存聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- 输入框处理 ---
if prompt := st.chat_input("请输入关于 Verilog 或芯片的问题..."):
    # 1. 显示用户的问题
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. 调用后端 API
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🔄 正在检索数据手册...")

        try:
            # 发送 POST 请求给 Day 3 的 FastAPI
            response = requests.post(
                API_URL,
                json={"question": prompt}
            )

            if response.status_code == 200:
                data = response.json()

                # 1. 获取 AI 回答
                ai_answer = data.get("answer", "没生成出来...")

                # 2. 获取来源
                sources = data.get("sources", [])

                # 3. 组合显示内容
                # 先显示 AI 的回答
                full_response = f"{ai_answer}\n\n---\n### 📚 参考来源：\n"

                # 再把来源折叠显示（看起来更高级）
                for i, doc in enumerate(sources):
                    full_response += f"**[{i + 1}] {doc['source']}**\n> {doc['content'][:100]}...\n\n"

                message_placeholder.markdown(full_response)

                # 保存历史
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            else:
                message_placeholder.error(f"❌ 服务器报错: {response.text}")

        except Exception as e:
            message_placeholder.error(f"❌ 连接失败: {str(e)}")