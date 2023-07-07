import json

from aiohttp.web_response import Response


async def index(request):
    response = {'title': 'Hello world!'}
    return Response(body=json.dumps(response), status=200)
