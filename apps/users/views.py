from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

# User = get_user_model()

class PrivateView(APIView):

    def get(self, request):
        return Response({"message": "User is authenticated", "user": request.user.email})
