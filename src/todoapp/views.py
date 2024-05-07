from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    # authentication_classes = [TokenAuthentication]
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.query_params.get('filter') == 'completed':
            queryset = queryset.filter(completed=True, owner=self.request.user)
        elif self.request.query_params.get('filter') == 'expired':
           queryset = queryset.filter(completed=False, owner=self.request.user, expiry__lt=str(timezone.now()))
        else:
            queryset = queryset.filter(owner=self.request.user)
            
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
    def update(self, request, *args, **kwargs):
        return Response({"detail": "Method Not Allowed"}, status=405)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "Method Not Allowed"}, status=405)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == request.user:  # Check if the owner of the todo matches the authenticated user
            self.perform_destroy(instance)
            return Response({"message": "Todo deleted successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No Todo matches the given query."}, status=status.HTTP_403_FORBIDDEN)
    
    def toggle_complete(self, request, pk=None):
        todo = self.get_object()
        if todo.owner == request.user:  # Check if the owner of the todo matches the authenticated user
            serializer = self.get_serializer(todo)
            serializer.toggle_complete()
            return Response(serializer.data)
        else:
            return Response({"message": "No Todo matches the given query."}, status=status.HTTP_403_FORBIDDEN)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user, context=self.get_serializer_context()).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user, context=self.get_serializer_context()).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
