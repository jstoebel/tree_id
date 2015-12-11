import json
from django.core.management.base import BaseCommand
from trees.models import Node
import os

class Command(BaseCommand):
    help = 'Resets data.'


    def handle(self, *args, **options):
        clear_data()
        populate_data()

#HELPER FUNCTIONS

def clear_data():
    """
    pre: none
    post: all data are deleted from table trees_node
    """

    #first delete all data from the database.
    #select nodes ordered by largest id first. This ensures we never leave an orphan node.
    print 'Clearing data from trees_node ',
    # nodes = Node.objects.all()
    for node in Node.objects.all().order_by('-id'):
        node.delete()

    print '-> Done!'
def populate_data():
    """
    pre: none
    post: resets the database back to the initial state as follows:
        according the data in initial_data.json
    """
    print 'populating data '
    with open('trees/initial_data.json', 'r') as data_file:
        data = json.load(data_file)

    for record in data:

        print "record is", record

        node = Node(id=record['id'],
                    guess=record['guess'],
                    edge=record['edge'],
                    parent_id=record['parent_id'],
                    question=record['question']
                    )
        node.save()

    print ' -> Done!'



