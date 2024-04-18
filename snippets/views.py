from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserLoginSerializer, UserRegisterSerializer, SnippetSerializer, TagSerializer
from .models import Snippet, Tag
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse
from rest_framework.generics import ListAPIView


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            access_token = str(token.access_token)
            return Response({"access_token": access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class CreateSnippetAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SnippetDetailAPIView(generics.RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetUpdateAPIView(generics.UpdateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

class SnippetDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
            snippet.delete()
            
            remaining_snippets = Snippet.objects.all()
            
            serializer = SnippetSerializer(remaining_snippets, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Snippet.DoesNotExist:
            return Response({"error": "Snippet not found"}, status=status.HTTP_404_NOT_FOUND)
        

class TagListAPIView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        
        serializer = TagSerializer(tags, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            tag = Tag.objects.get(pk=pk)
            
            snippets = tag.snippet_set.all()
            
            serializer = SnippetSerializer(snippets, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tag.DoesNotExist:
            return Response({"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)
        

class OverviewAPIView(APIView):
    def get(self, request):
        total_count = Snippet.objects.count()

        snippets = Snippet.objects.all()

        serializer = SnippetSerializer(snippets, many=True)

        data = {
            "total_count": total_count,
            "snippets": serializer.data
        }

        return Response(data)


class SnippetListAPIView(ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def list(self, request, *args, **kwargs):
        snippets = self.get_queryset()
        serializer = self.get_serializer(snippets, many=True)
        data = serializer.data
        for snippet in data:
            detail_url = reverse('snippet-detail', kwargs={'pk': snippet['id']})
            snippet['detail_url'] = detail_url
        return Response(data)
