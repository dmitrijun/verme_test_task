import json
from re import T
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render, get_object_or_404
from .models import Tree
# Create your views here.


def bypass_tree(node_pk: int):
    current_node = get_object_or_404(Tree, pk=node_pk)
    serialization = current_node.to_short_dict()
    serialization["children"] = [bypass_tree(item.pk)
                                 for item in Tree.objects.filter(parent=current_node)]
    return serialization


def get_tree(request):
    """
        Returns tree node list
    """
    records = Tree.objects.all()
    serializable_records = [item.to_dict() for item in records]


def get_subtree(request, node_pk):
    """
        Returns Tree node by key
    """
    subtree_serialization = bypass_tree(node_pk)
    return HttpResponse(json.dumps(subtree_serialization), content_type="application/json")
