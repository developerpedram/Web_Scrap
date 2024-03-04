from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/pedram")
def read_root():
    return {"name": "Pedram", "Family":"Mmmmajidi"}

#decorator
#path parameter
# ? query parameters
# Osouli nist ASSSlannnn

@app.get("/books/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    try:
        with open('books.csv', 'r') as lines:
            for line in lines:
                if item_id == int(line.split(';')[0]):
                    name= line.split(';')[1]
                    img= line.split(';')[2]
                    price= line.split(';')[3]

                    return {"status" : "ok", "id": str(item_id), "name": name, 'image':img, "price":price}
    except:
        return {"status":"Err!"}
    return {"item_id": item_id, "q": q}