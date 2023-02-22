# Create your views here.

from rest_framework import views
from rest_framework.response import Response
from .models import TranslationModel
from .serializers import TranSerializer
from .interactive import translator

def translate_text(text, model_id):
    translated_text = ''
    try:
        model_obj = TranslationModel.objects.get(model_id)
        translated_text = translator(text, model_obj)
    except:
        translated_text = 'Model not Found.'
    return translated_text

class TranView(views.APIView):

    def post(self, request, model=1):
        request.data['destination'] = translate_text(request.data['source'], model)
        results = TranSerializer(request.data, many=False).data
        return Response(results)