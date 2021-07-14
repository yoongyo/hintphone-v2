from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Theme
from .serializers import ThemeSerializer
from rest_framework import status


@api_view(['GET'])
def theme_list_create(request):
    if request.method == 'GET':
        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)  # 보내는 데이터가 여러개일 경우
        return Response(data=serializer.data)

@api_view(['GET', 'PUT'])
def theme_detail_update_delete(request, theme_pk):
    theme = get_object_or_404(Theme, pk=theme_pk)
    if request.method == 'GET':
        serializer = ThemeSerializer(theme)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if "reset" in request.data:
            theme.currentHint = ""
            theme.currentCount = 0
            theme.save()
        elif "addCount" in request.data:
            theme.currentHint = request.data["currentHint"]
            theme.currentCount = request.data["currentCount"]
            theme.save()
        else:
            serializer = ThemeSerializer(instance=theme, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

        return Response("success")
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


