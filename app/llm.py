from fastapi import HTTPException
from langchain_openai import ChatOpenAI
import os


OPENAI_API_KEY = ""
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

MODEL_NAME = "gpt-4o-mini"


def get_llm():
    api_key = OPENAI_API_KEY
    if not api_key:
        raise HTTPException(
            status_code=500, detail="환경 변수 OPENAI_API_KEY가 설정되지 않았습니다."
        )

    llm = ChatOpenAI(model=MODEL_NAME)
    return llm
