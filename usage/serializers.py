from rest_framework import serializers

from .models import Usage
from .models import UsageTypes
from users.serializers import UserSerializer


class UsageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageTypes
        fields = ("id", "name", "unit", "factor")


class UsageListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    usage_type = UsageTypeSerializer()

    class Meta:
        model = Usage
        fields = ("id", "user", "usage_type", "usage_at", "amount")


class UsageSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        validated_data.pop("user", None)
        return super().update(instance, validated_data)

    class Meta:
        model = Usage
        fields = ("id", "user", "usage_type", "usage_at", "amount")
