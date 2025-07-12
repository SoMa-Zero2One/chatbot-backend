from fastapi import FastAPI, HTTPException
from langchain_openai import ChatOpenAI
from app.schemas import ChatRequest, ChatResponse
import os

MODEL_NAME = "gpt-4o-mini"


OPENAI_API_KEY = ""

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


app = FastAPI()


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500, detail="환경 변수 OPENAI_API_KEY가 설정되지 않았습니다."
        )

    llm = ChatOpenAI(model=MODEL_NAME)

    reply = await llm.ainvoke(request.prompt)
    print(reply)
    return ChatResponse(response=reply.content)
