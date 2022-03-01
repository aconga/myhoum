from rest_framework.response import Response
from datetime import datetime, timedelta
import haversine as hs
from rest_framework.views import APIView
from position.models import Property, PropertyInfo
from position.api import serializers
from position.api.utils import extract_lat_lng, get_lat_lng_model
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status

class PropertyList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        register = self.request.query_params.get('register', None)
        propertys = Property.objects.all()
        if register:
            propertys = propertys.filter(register=register)
        speed = self.request.query_params.get('speed', None)
        if speed:
            propertys = propertys.filter(property_details__speed__gte=speed)
        serializer = serializers.PropertyListSerializer(propertys, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        body = request.data
        address = body.get('address')
        lat, lng = extract_lat_lng(address)
        now = datetime.now()
        body.update({
            "latitude": lat,
            "longitude": lng,
            "houm": self.request.user.id
        })
        serializer = serializers.PropertyCreateSerializer(data=body)
        obj_last, lat_last, long_last, start_last = get_lat_lng_model(Property)
        if serializer.is_valid():
            serializer.save()
            if obj_last:
                # register finish_date
                if obj_last.finish_date is None:
                    obj_last.finish_date = start_last + timedelta(hours=1)
                    obj_last.save()
                # get first coordinate
                loc1 = (lat_last, long_last)
                obj, lat, long, start = get_lat_lng_model(Property)
                # get first coordinate
                loc2 = (lat, long)
                # get speed of the coordinates
                distance = hs.haversine(loc1, loc2)
                total_time = abs(obj.start_date - obj_last.finish_date)
                total_time_hour = (total_time).total_seconds()/3600
                speed = round(distance/total_time_hour, 2)
                property_info = PropertyInfo(property=obj, speed=speed)
                property_info.save()
            return Response(body)
        else:
            return Response(serializer.errors)

class PropertyDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            property = Property.objects.get(id=id)
        except Property.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.PropertyListSerializer(property)
        return Response(serializer.data)
    
    def put(self, request, id):
        property = Property.objects.get(id=id)
        serializer = serializers.FinishDateSerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyInfoList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        propertysDetail = PropertyInfo.objects.all()
        serializer = serializers.PropertyInfoSerializer(propertysDetail, many=True)
        return Response(serializer.data)

