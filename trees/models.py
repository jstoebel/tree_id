######################################################################
##   Final Lab
##   Jacob Stoebel (stoebelj)
## CSC 326, Data Structures
## models.py
## Purpose: Defines a useful abstraction the underlying database table used in this application.
## Aknowledgements: (see readme.txt)

from django.db import models

# Create your models here.

class Node(models.Model):
    """
    This is the model for the trees_node table. It's columns are as follows: id, text, edge, and parent.
    See below comments for more details on these columns.
    """

    #the question asked at this node to proceed down the tree. For leaves this column is Null
    question = models.CharField(max_length=100, null=True)

    guess = models.CharField(max_length=100)

    #the text of the edge pointing to this node. For the root, this value is NULL
    edge = models.CharField(max_length=100, null=True)

    #the id of this node's parent. For the root node, value is NULL
    parent = models.ForeignKey('self', null=True)

    def __str__(self):
        """
        specifies how this class should be represented as text
        pre: none
        post: returns the value of the text column.
        """
        return self.guess

    def is_leaf(self):
        """
        pre: none
        post: returns if instance is a leaf node.
        """

        children = Node.objects.filter(parent_id=self.id)        # a leaf has no children. Let's see if there are any.
        return len(children) == 0

    def get_children(self):
        """
        pre: none
        post: returns this node's children
        """

        children = Node.objects.filter(parent_id=self.id)
        return children
