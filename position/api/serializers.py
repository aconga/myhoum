from rest_framework import serializers
from position.models import Property, PropertyInfo

class PropertyInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyInfo
        fields = "__all__"


class PropertyListSerializer(serializers.ModelSerializer):
    property_details = PropertyInfoSerializer()
    address = serializers.CharField()

    class Meta:
        model = Property
        fields = ('id', 'address', 'latitude', 'longitude', 'register', 'start_date', 'finish_date', 'houm', 'property_details')


class PropertyCreateSerializer(serializers.ModelSerializer):
    address = serializers.CharField()

    class Meta:
        model = Property
        fields = ('id', 'address', 'latitude', 'longitude', 'register', 'start_date', 'finish_date', 'houm')


class FinishDateSerializer(serializers.ModelSerializer):
    # houm = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Property
        fields = ('finish_date',)

