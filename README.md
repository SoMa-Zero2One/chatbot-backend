

## Init
```
uv init
uv add fastapi
uv add uvicorn --extra standard

```

## Run dev
```
uv run uvicorn main:app --reload
```


### Run prod
```
docker build -t chatbot-backend .
docker run -d -p 80:80 chatbot-backend
```