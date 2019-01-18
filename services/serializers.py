from rest_framework import serializers
from services.models import Meme

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ('name', 'url', 'first_visited_date', 'rank')