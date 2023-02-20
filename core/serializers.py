from rest_framework import serializers

class TranSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   translate = serializers.CharField()
