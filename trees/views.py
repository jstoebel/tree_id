######################################################################
##   Final Lab
##   Jacob Stoebel (stoebelj)
## CSC 326, Data Structures
## views.py
## Purpose: Provides the bussiness logic to be executed for each valid http request sent to this site.
## Aknowledgements: (see readme.txt)


from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Node
from .forms import LearnForm
from django.contrib import messages
# Create your views here.

def home(request):
    """
    The home page where the user may begin a new tree identifying process.
    :param request: an http request
    :return: an http response with the home tempalte.
    """
    template = loader.get_template('trees/home.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def show_node(request):
    """
    A dialogue page to ask the user a question and get a response.
    :param request: an http request
    :return: an http response with the show_node template

    NOTE: The main operation of my program lies in this function. In this function we look up the desired node
    based on incoming request parameters as well as that node's children. We then render the page with those objects.
    When the user answer the question another response comes to this function and we repeat the process until we
    have reached a leaf.

    The big O efficiency of this program is O(N) = NlogN.  Each database look up on an indexed column has a complexity
    of logN but since unlike a linked structure we can't keep track of the current node in between requests (we must
    find the current node by searching from the root each time) we are required to perform this action N times.
    """

    try:
        node_id = request.POST['answer']        #if we got post data, look there to determine which node to go to.
    except KeyError:
        node_id = 1     #otherwise go to the root (id=1)

    template = loader.get_template('trees/show_node.html')  #load the template to render
    node = Node.objects.filter(id=node_id)[0]      #find the requested node
    children = node.get_children()      #get that node's children
    context = RequestContext(request, {     #render the page, making these local variables availabe in the template
        'node': node,       #current node
        'children': children,          #node's children
        'post_params':request.POST
    })
    return HttpResponse(template.render(context))

def learn(request, node_id):
    """
    Renders an input form to add to the apps knowledge base.
    pre:
        request: an http request
        node_id: the id of the node that will be expanded on.
    post: node gains a question and two children nodes.
    """

    template = loader.get_template('trees/learn.html')
    node = Node.objects.filter(id=node_id)[0]

    form = LearnForm()
    form.fields['parent_id'].initial = node.id      #initialize value without running validation.
    context = RequestContext(request, {     #render the page, making this node availabe in the template

        'node': node,
        'form': form
    })
    return HttpResponse(template.render(context))

def learn_confirm(request):
    """
    confirms submission of adding to the database
    pre: request: an http request
    post: if request is valid:
        returns an http response confirming the new information was written to the database
        otherwise returns an error
    """

    #template = loader.get_template('trees/learn_confirm.html')
    #print request.POST
    try:
        parent_node = Node.objects.filter(id=request.POST['parent_id'])[0]
    except IndexError:
        #node doesn't exist!
        raise Http404("Node %s does not exist!" % (request.POST['parent_id']))

    if request.method == 'POST':
        form = LearnForm(request.POST)
        if form.is_valid():
            # is it an existing node?

            # is that node a leaf?
            if parent_node.is_leaf():
                #make the magic happen!

                #update the parent node
                parent_node.question = request.POST['question']
                parent_node.save()

                #create child node 1
                guess1 = request.POST['guess1']
                edge1 = request.POST['edge1']
                child1 = Node(guess=guess1, edge=edge1, parent_id=parent_node.id)
                child1.save()

                #create child node 2
                guess2 = request.POST['guess2']
                edge2 = request.POST['edge2']
                child2 = Node(guess=guess2, edge=edge2, parent_id=parent_node.id)
                child2.save()

                context = RequestContext(request, {
                    'parent_node': parent_node,
                    'child1': child1,
                    'child2': child2
                })

                template = loader.get_template('trees/learn_confirm.html')
                return HttpResponse(template.render(context))
            else:
                #not a leaf!
                raise Http404("Node %s is not a leaf!" % (parent_node.id))

        else:   # Form is not valid!
            #rerender the page

            context = RequestContext(request, {
                'node': parent_node,
                'form': form
            })
            messages.error(request, 'Please complete this form.')
            template = loader.get_template('trees/learn.html')
            return HttpResponse(template.render(context))

