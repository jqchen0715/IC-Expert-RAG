🤖 IC-Expert: 集成电路专业知识库助手基于 RAG (检索增强生成) 的垂直领域 AI 助手，专为集成电路 (IC) 从业者设计。
<img width="1982" height="1678" alt="image" src="https://github.com/user-attachments/assets/57d935d7-fc13-480d-b37a-c03b07ec7070" />

📖 项目简介针对集成电路领域技术文档（如芯片 Datasheet、Verilog 规范）篇幅长、术语多、通用大模型易产生幻觉的问题，本项目开发了一套基于 RAG 架构的智能问答系统。它能够读取 PDF 文档，理解专业术语，并提供有理有据的回答。
核心痛点解决：
  专业性：针对 Verilog 代码和时序图描述优化了检索策略。
  准确性：通过 Prompt Engineering 强制模型基于参考文档回答，拒绝幻觉。
  可追溯：每次回答均提供 PDF 原文出处和页码引用。
✨ 核心功能
📄 文档解析：支持上传 PDF 格式的芯片手册、技术标准或论文。
🧠 语义检索：基于 ChromaDB 向量数据库，实现毫秒级精准检索。
💬 智能问答：集成 LLM (DeepSeek/OpenAI)，支持多轮专业对话。
💻 交互界面：基于 Streamlit 构建的现代化 Web 界面，开箱即用。
🛠️ 技术栈语言：Python 3.10+LLM 
框架：LangChain向量数据库：ChromaDB后端 API：FastAPI前端 UI：Streamlit数据校验：Pydantic
🚀 快速开始
1. 克隆项目git clone [https://github.com/jqchen0715/IC-Expert-RAG.git](https://github.com/你的用户名/IC-Expert-RAG.git)
cd IC-Expert-RAG
2. 环境配置建议使用 Conda 或 venv 创建虚拟环境：python -m venv .venv
# Windows
。venv\Scripts\activate
# Mac/Linux
source 。venv/bin/activate
安装依赖：pip install -r requirements.txt

3. 配置 API Key在项目根目录创建 .env 文件，填入你的 API Key：OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
OPENAI_API_BASE=[https://api.deepseek.com](https://api.deepseek.com)  # 或其他兼容 OpenAI 的接口

5. 启动服务后端服务：python server.py
   
前端界面：（打开新终端）streamlit run app.py

访问浏览器 http://localhost:8501 即可使用。📂 项目结构IC-Expert-RAG/
├── app.py              # Streamlit 前端入口
├── server.py           # FastAPI 后端服务
├── rag_core.py         # RAG 核心逻辑 (加载、切分、检索)
├── data/               # 存放 PDF 文档
├── chroma_db/          # 向量数据库缓存
├── .env                # 环境变量 (不要上传到 GitHub)
├── requirements.txt    # 项目依赖
└── README.md           # 项目说明书
👨‍💻 开发者Eric Chen｜北京航空航天大学 | 集成电路工程硕士专注 AI for IC 及 LLM 应用落地。本项目仅供学习交流使用。
