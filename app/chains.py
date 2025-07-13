from functools import lru_cache
from typing import Any

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI


@lru_cache(maxsize=1)
def get_chat_chain() -> Any:
    """LangChain Runnable (prompt | llm) 반환"""
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            MessagesPlaceholder(name="messages"),
        ]
    )
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return prompt | llm
