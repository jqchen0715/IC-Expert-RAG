import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_core import get_rag_response  # <-- 改这里
# 1. 导入你昨天写好的 RAG 核心逻辑
# 注意：确保 rag_core.py 和 server.py 在同一个文件夹下
from rag_core import search_rag

# 2. 初始化 FastAPI 应用
app = FastAPI(
    title="IC-Expert RAG API",
    description="基于 RAG 的集成电路专业知识库助手后端服务",
    version="1.0.0"
)


# 3. 定义数据模型 (Pydantic)
# 这就是面试官问的“数据校验”：我们规定前端必须传一个叫 'question' 的字符串
class QueryRequest(BaseModel):
    question: str


# 4. 定义接口 (API Endpoint)

@app.post("/chat")
def chat_endpoint(request: QueryRequest):
    user_question = request.question
    print(f"📩 收到请求：{user_question}")

    try:
        # 调用新的函数：获取 AI 回答 + 来源文档
        answer_text, source_docs = get_rag_response(user_question)

        # 整理来源格式
        sources_list = []
        for doc in source_docs:
            sources_list.append({
                "content": doc.page_content,
                "source": doc.metadata.get("source", "未知").split('/')[-1]
            })

        return {
            "answer": answer_text,  # <-- 这是 AI 生成的人话
            "sources": sources_list  # <-- 这是参考的片段
        }

    except Exception as e:
        print(f"❌ 报错: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# 5. 启动服务
if __name__ == "__main__":
    print("🚀 正在启动后端服务...")
    # 在本地 8000 端口启动
    uvicorn.run(app, host="127.0.0.1", port=8000)