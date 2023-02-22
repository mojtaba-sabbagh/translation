from rest_framework import serializers

class TranSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   source = serializers.CharField()
   destination = serializers.CharField()
