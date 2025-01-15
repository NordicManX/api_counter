import asyncio
from django.http import StreamingHttpResponse
from django.http import HttpResponse

async def contador_gen(tempo):
    for segundos in range(tempo, -1, -1):
        yield f"data: Tempo restante: {segundos} segundos\n\n"
        await asyncio.sleep(1)
    yield "data: Tempo finalizado!\n\n"


async def contador_api(request):
    tempo = int(request.GET.get("tempo", 130))  
    response = StreamingHttpResponse(
        contador_gen(tempo),
        content_type="text/event-stream",
    )
    response["Cache-Control"] = "no-cache"
    return response