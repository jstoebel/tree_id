from django.test import TestCase
from trees.models import Node
from django.db import IntegrityError

class TestNode(TestCase):
    """
    tests related to the Node model
    """

    """here are two objects to run tests against"""
    n = Node(guess='test guess',
            edge='test edge',
            parent_id=None,
            question='test question')

    n2 = Node(guess='test guess2',
              edge='test edge2',
              question='test question2')

    def test_clean_insert(self):
        """
        tests inserting a record into the database.
        pre: none
        post: confirms that a valid record can be inserted into the database.
        """

        n = self.n
        n.save()
        self.assertTrue(True)
        n.delete()

    def test_guess_not_null(self):
        """
        pre: none
        post: confirms that a record may not be saved without a value for guess
        """
        n = Node(guess=None)

        with self.assertRaises(IntegrityError):
            n.save()

    def test_str(self):
        """
        pre: none
        post: tests the __str__() method
        """

        n = self.n
        self.assertEqual(str(n), n.guess)

    def test_is_leaf(self):
        """
        pre: none
        post: tests that node is a leaf
        """

        n = self.n
        self.assertEqual(n.is_leaf(), True)

    def test_not_leaf(self):
        """
        pre: none
        post: tests that n is not a leaf
        """

        n = self.n
        n.save()        #currently n is a leaf
        n2 = self.n2
        n2.parent_id = n.id
        n2.save()       #now n is a parent and not a leaf!

        self.assertEqual(n.is_leaf(), False)
        n.delete()      #clear out the database
        n2.delete()

    def get_children(self):
        """
        pre: none
        post: confirms that n2 is the single child of n
        """

        n = self.n
        n.save()
        n2 = self.n2
        n2.parent_id = n.id
        n2.save()   #n2 is now a child of n

        self.assertEqual(n.get_children() == [n2])      #.get_children() returns children as a list, so wrap n2 in a list as well.

        n.delete()  #clear out database
        n2.delete()


class TreesViewsTestCase(TestCase):
    """
    tests related to the views
    """

    """
    once again, here are two example objects for testing.
    """
    n = Node(guess='test guess',
            edge='test edge',
            parent_id=None,
            question='test question')

    n2 = Node(guess='test guess2',
              edge='test edge2',
              question='test question2')

    def test_index(self):
        """
        pre: none
        post: confirms a 200 response from /trees/
        """
        resp = self.client.get('/trees/')
        self.assertEqual(resp.status_code, 200)

    def test_show_node_get(self):
        """
        pre: none
        confirms a 200 response from /trees/show_node via a get request
        """

        n = self.n
        n.id = 1
        n.save()
        resp = self.client.get('/trees/show_node')
        self.assertEqual(resp.status_code, 200)
        n.delete()      #clear out database

    def test_show_node_post(self):
        """
        pre: none
        post: confirms a 200 response from /trees/show_node via a post request
        """

        n = self.n
        n.id = 1
        n.save()

        #POST data using with n's id as a parameter
        resp = self.client.post('/trees/show_node', {'answer': n.id})
        self.assertEqual(resp.status_code, 200)
        n.delete()      #clear out database

    def test_learn(self):
        """
        pre: none
        post: confirms a 200 response from /trees/learn/id via a get request
        """

        n = self.n
        n.save()
        resp = self.client.get('/trees/learn/{}'.format(n.id))      #get request using n's id as a parameter
        self.assertEqual(resp.status_code, 200)
        n.delete()      #clear out database

    def test_learn_fail(self):
        """
        pre: none
        post: confirms that an IndexError is thrown when an id of a non existant node is given
        """

        n = self.n
        n.save()
        with self.assertRaises(IndexError):
            resp = self.client.get('/trees/learn/99')       #get request using a bogus id
        n.delete()      #clear out database


    def test_learn_confirm(self):
        """
        pre: none
        post: confirms a 200 response from /trees/learn_confirm
        """

        n = self.n
        n.save()

        params = {
            'question': 'new question1',
            'guess1': 'guess1',
            'edge1': 'edge1',
            'guess2': 'guess2',
            'edge2': 'edge2',
            'parent_id': n.id

        }       #valid parameters from the learn form
        resp = self.client.post('/trees/learn_confirm', params)
        self.assertEqual(resp.status_code, 200)

        #delete all nodes
        nodes = Node.objects.all()
        for node in nodes:
            node.delete()