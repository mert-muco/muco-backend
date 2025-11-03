from .models import Order
from rest_framework import serializers
from brief_app.serializers import BriefSerializer
from bid_app.serializers import BidSerializer
from brief_app.models import Brief
from bid_app.models import Bid


class OrderSerializer(serializers.ModelSerializer):
    brief = BriefSerializer(read_only=True)
    bid = BidSerializer(read_only=True)
    brief_id = serializers.PrimaryKeyRelatedField(source='brief', queryset=Brief.objects.all(), write_only=True)
    bid_id = serializers.PrimaryKeyRelatedField(source='bid', queryset=Bid.objects.all(), write_only=True)
    class Meta:
        model = Order
        fields = '__all__'

























