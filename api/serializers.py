from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from places.models import Places, Comment

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ['id', 'name', 'discription', 'image', 'addres']

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Name length must be more than 4 characters.")
        return value

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'place', 'comment_text', 'stars_given', 'created_at']

class PlaceDetailApiView(APIView):
    def get(self, request, id):
        try:
            place = Places.objects.get(id=id)
        except Places.DoesNotExist:
            return Response({"error": "Place not found"}, status=404)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

class ReviewsApiView(APIView):
    def get(self, request):
        comments = Comment.objects.all().select_related('user', 'place')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
