from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Wishes
from .serializer import CommonSerializer, UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            data =  request.data
            user_name = data.get("username")
            password = data.get("password")
            user = authenticate(request, username=user_name, password=password)
            if user:
                login(request, user)
                data={
                    "done":"done",
                }
                return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class WishesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        values = Wishes.objects.filter(user=user)
        serializer = CommonSerializer(values, many=True)
        return Response(serializer.data)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return redirect(LoginView.as_view())