from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import search_tickers, get_quote

@api_view(['GET'])
def api_search(request, query):
    return Response({"stocks": search_tickers(query)})

@api_view(['GET'])
def api_quote(request, symbol):
    return Response(get_quote(symbol))
