

## Init
```
uv init
uv add fastapi
uv add uvicorn --extra standard
uv add langchain-chroma langchain-openai langchain

uv sync
```

## Run dev
```
uv run uvicorn app.main:app --reload
```


### Run prod
```
docker build -t chatbot-backend .
docker run -d -p 80:80 chatbot-backend
```
