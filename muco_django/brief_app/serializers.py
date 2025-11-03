from rest_framework import serializers
from .models import Brief, BriefImage
from user_app.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class BriefSerializer(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField()
    company = UserSerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(source='company', write_only=True, queryset=User.objects.all())
    image = serializers.ImageField(write_only=True, required=False)
    class Meta:
        model = Brief
        fields = '__all__'
        extra_fields = ['cover']
    def get_cover(self, obj):
        return obj.images.first().image.url if obj.images.first() else None
    def create(self, validated_data):
        image = validated_data.pop('image')
        brief = Brief.objects.create(**validated_data)
        BriefImage.objects.create(brief=brief, image=image)
        return brief