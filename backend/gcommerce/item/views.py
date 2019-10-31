from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Item, ItemCategory, ItemRating, ItemPhoto
from .serializers import ItemSerializer, ItemCategorySerializer, ItemRatingSerializer, ItemPhotoSerializer


@api_view(['GET'])
def get_item(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
