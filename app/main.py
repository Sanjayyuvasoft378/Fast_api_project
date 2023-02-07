import uvicorn

if __name__ == "_main_":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8080, reload=True)