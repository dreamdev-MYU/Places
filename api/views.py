from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PlaceSerializer, CommentSerializer
from places.models import Places, Comment



class PlaceApiView(APIView):
    def get(self, request):
        places = Places.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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


