from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo import todo_router
import uvicorn

app = FastAPI() #FastAPI의 객체 생성

origins = [ "http://127.0.0.1:5500" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
    
    
    
    


@app.get("/") # @= 데코레이터 /는 0.0.0.0:8000/ 에서의 포트번호뒤에 /가 됨 만약 /abc를 작성했다면 0.0.0.0:8000/abc 가 됨
async def welcome() -> dict:
    return {
        "msg" : "hello world?"
    } #json 파일 형식으로 리턴

app.include_router(todo_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host = "127.0.0.1", port = 8080, reload=True)