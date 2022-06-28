import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Tree
# Create your views here.
    

def get_tree(request):
    """
        Returns tree node list
    """
    records = Tree.objects.all()
    serializable_records = [item.to_dict() for item in records]

    return HttpResponse(serializable_records)

def get_subtree(request, node_pk):
    """
        Returns Tree node by key
    """
    node = get_object_or_404(Tree, pk=node_pk)
    return HttpResponse(f'{node.to_dict()}')