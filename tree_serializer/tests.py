from logging import root
from re import A
from unicodedata import name
from urllib import response
from django.test import TestCase
from itsdangerous import json
from tree_serializer.models import Tree


class SubTreeSerializerTestCase(TestCase):
    __tree_list = []

    def setUp(self) -> None:
        Tree.objects.all().delete()

        single_root = Tree(name="Single root", parent=None)
        single_root.save()

        nested_parent = Tree(name="Nested parent", parent=None)
        nested_parent.save()

        nested_child = Tree(name="Nested child", parent=nested_parent)
        nested_child.save()

        self.__tree_list = [single_root, nested_parent, nested_child]

    def tearDown(self) -> None:
        Tree.objects.all().delete()

    def test_non_existent(self):
        response = self.client.get("/tree_serializer/4/")
        self.assertEqual(response.status_code, 404)

    def test_single(self):
        response = self.client.get(
            f"/tree_serializer/{self.__tree_list[0].pk}/")
        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        self.assertEqual(response_data["id"], self.__tree_list[0].pk)
        self.assertEqual(response_data["name"], self.__tree_list[0].name)
        self.assertEqual(len(response_data["children"]), 0)

    def test_nested(self):
        response = self.client.get(
            f"/tree_serializer/{self.__tree_list[1].pk}/")
        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        self.assertEqual(response_data["id"], self.__tree_list[1].pk)
        self.assertEqual(response_data["name"], self.__tree_list[1].name)
        self.assertEqual(len(response_data["children"]), 1)

        child_data = response_data["children"][0]

        self.assertEqual(child_data["id"], self.__tree_list[2].pk)
        self.assertEqual(child_data["name"], self.__tree_list[2].name)
        self.assertEqual(len(child_data["children"]), 0)

