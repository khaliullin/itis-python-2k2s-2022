from aiohttp import web


async def process_request(request):
    name = request.match_info.get("name", "no name given")
    response_text = f"Hello {name}"

    return web.Response(text=response_text)


app = web.Application()

app.add_routes([
    web.get("/", process_request),
    web.get("/{name}", process_request)
])


if __name__ == '__main__':
    web.run_app(app)
