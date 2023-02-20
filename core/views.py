# Create your views here.

from rest_framework import views
from rest_framework.response import Response

from .serializers import TranSerializer

class TranView(views.APIView):

    def post(self, request, model=0):
        results = TranSerializer(request.data, many=True).data
        return Response(results)