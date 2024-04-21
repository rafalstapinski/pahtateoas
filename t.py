from typing import NotRequired, TypedDict, Unpack

from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.applications import HTMLResponse
from pydantic import BaseModel

from pathatoes.dom import *

z = html()[
    head()[title()["Hello, world!"],],
    body()[
        div()[
            p()["Hello, world!"],
            a(href="https://google.com")["Google"],
            img(src="https://via.placeholder.com/150"),
            span()["Hello, world!"],
        ],
    ],
]


output = z.to_html()

soup = BeautifulSoup(output, "html.parser")

print(soup.prettify())

i = img(src="https://via.placeholder.com/150")

app = FastAPI()


@app.get("/")
async def index() -> HTMLResponse:
    return HTMLResponse(content=output, status_code=200)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "t:app",
        host="0.0.0.0",
        port=8000,
        use_colors=True,
        log_level="info",
        reload=True,
    )
