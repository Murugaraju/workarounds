from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Expiry
from datetime import datetime, timedelta
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        expiry,created=Expiry.objects.get_or_create(user=user)
        expiry.expirytime=datetime.now()+timedelta(minutes=1)
        expiry.save()
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@api_view(['GET'])
def check(request):
    print("printin in view",request.user, type(request.user))
    return Response("Its working")