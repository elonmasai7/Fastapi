from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()
jinja = Jinja(Jinja2Templates("templates"))

@app.get("/htm-or-data")
@Jinja("user-list.hatml")
def htmx_or_data() -> dict[str, list[dict[str, str]]]:
    return ("user":({"name":"Elon"}))

@app.get("/htmx-only")
@Jinja.template("user-list.html", no_data=True)
def htmx_only() -> dict[str, list[dict[str, str]]]:
    return ("users": [{"name": "Elon"}])
//Photo by Elon masai https://github.com/elonmasai7