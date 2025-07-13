from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document


def get_retriever():
    documents = [
        Document(page_content="Hello, world!", metadata={"source": "example1"}),
        Document(
            page_content="This is another piece of text.",
            metadata={"source": "example2"},
        ),
    ]

    vectorstore = Chroma.from_documents(
        documents=documents, embedding=OpenAIEmbeddings()
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    )

    return retriever
