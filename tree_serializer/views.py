import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Tree
# Create your views here.


def index(request):
    """
        Returns tree node list
    """
    records = Tree.objects.all()
    serializable_records = [{
        "id": item.pk,
        "name": item.name,
        "parent": item.parent_pk
    } for item in records]

    return HttpResponse(serializable_records)
