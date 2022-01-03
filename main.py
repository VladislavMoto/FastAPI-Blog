from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'Main page'}

@app.get('/about')
def about():
    return {'data': 'About Page'}