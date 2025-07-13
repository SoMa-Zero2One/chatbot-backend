from fastapi import FastAPI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.schema import HumanMessage
from langchain_core.runnables import Runnable
from app.llm import get_llm
from app.retrieval import get_retriever
from app.schemas import ChatRequest, ChatResponse
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


app = FastAPI()

system_prompt = """답변은 100자 이상으로 줘"""


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:

    llm = get_llm()
    retriever = get_retriever()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    chat_retriever_chain: Runnable = create_history_aware_retriever(
        llm, retriever, prompt
    )

    qa_system_with_context = """
    다음 검색된 컨텍스트를 참고해서 질문에 답해주세요.
    모르면 모른다고 하고, 간결하게 100자 이상으로 작성하세요.

    {context}
    """

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_with_context),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

    rag_chain = create_retrieval_chain(chat_retriever_chain, question_answer_chain)

    chat_history: list = []

    ai_msg = rag_chain.invoke({"input": request.prompt, "chat_history": chat_history})
    chat_history.extend([HumanMessage(content=request.prompt), ai_msg["answer"]])
    print(ai_msg["answer"])

    return ChatResponse(response=ai_msg["answer"])
