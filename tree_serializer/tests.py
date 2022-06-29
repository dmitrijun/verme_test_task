from urllib import response
from django.test import TestCase
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


class TreeSerializerTestCase(TestCase):
    _path = "/tree_serializer/"

    def setUp(self) -> None:
        Tree.objects.all().delete()

    def test_empty_tree(self):
        response = self.client.get(self._path)
        self.assertEqual(response.status_code, 200)

    def test_single_node(self):
        root = Tree(name="A", parent=None)
        root.save()

        response = self.client.get(self._path)

        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        self.assertEqual(len(response_data), 1)

        self.assertEqual(response_data[0]["id"], root.pk)
        self.assertEqual(response_data[0]["name"], root.name)
        self.assertEqual(len(response_data[0]["children"]), 0)

    def test_nested_nodes(self):
        root = Tree(name="A", parent=None)
        root.save()

        child = Tree(name="B", parent=root)
        child.save()

        response = self.client.get(self._path)

        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        self.assertEqual(len(response_data), 1)

        self.assertEqual(response_data[0]["id"], root.pk)
        self.assertEqual(response_data[0]["name"], root.name)
        self.assertEqual(len(response_data[0]["children"]), 1)

        result_child = response_data[0]["children"][0]

        self.assertEqual(result_child["id"], child.pk)
        self.assertEqual(result_child["name"], child.name)
        self.assertEqual(len(result_child["children"]), 0)

    def test_multiple_roots(self):
        root_1 = Tree(name="A", parent=None)
        root_2 = Tree(name="B", parent=None)
        root_1.save()
        root_2.save()

        child_1 = Tree(name="C", parent=root_1)
        child_1.save()

        response = self.client.get(self._path)

        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        self.assertEqual(len(response_data), 2)

        self.assertEqual(response_data[0]["id"], root_1.pk)
        self.assertEqual(response_data[0]["name"], root_1.name)
        self.assertEqual(len(response_data[0]["children"]), 1)

        self.assertEqual(response_data[1]["id"], root_2.pk)
        self.assertEqual(response_data[1]["name"], root_2.name)
        self.assertEqual(len(response_data[1]["children"]), 0)

        result_child = response_data[0]["children"][0]

        self.assertEqual(result_child["id"], child_1.pk)
        self.assertEqual(result_child["name"], child_1.name)
        self.assertEqual(len(result_child["children"]), 0)
