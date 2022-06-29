import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Tree


def bypass_tree(node_pk: int):
    current_node = get_object_or_404(Tree, pk=node_pk)
    serialization = current_node.to_short_dict()
    serialization["children"] = [bypass_tree(item.pk)
                                 for item in Tree.objects.filter(parent=current_node)]
    return serialization


def get_tree(request):
    """
        Returns tree serialization
    """
    tree_serialization = [bypass_tree(item.pk)
                          for item in Tree.objects.filter(parent=None)]
    return HttpResponse(json.dumps(tree_serialization), content_type="application/json")


def get_subtree(request, node_pk):
    """
        Returns node subtree serialization
    """
    subtree_serialization = bypass_tree(node_pk)
    return HttpResponse(json.dumps(subtree_serialization), content_type="application/json")
