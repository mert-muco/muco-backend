from rest_framework import serializers
from .models import Bid


class BidPreviewSerializer(serializers.ModelSerializer):
    brief = serializers.SlugRelatedField(slug_field='title', read_only=True)
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)
    class Meta:
        model = Bid
        fields = ['id', 'brief', 'user', 'asked_budget', 'ai_score']

class BidSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)
    class Meta:
        model = Bid
        fields = '__all__'