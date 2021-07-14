from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.models import Profile

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        profile = get_object_or_404(Profile, user=user)
        print(profile)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'profile_id': profile.pk
    })