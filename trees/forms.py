######################################################################
##   Final Lab
##   Jacob Stoebel (stoebelj)
## CSC 326, Data Structures
## forms.py
## Purpose: Defines a useful abstraction for the form used by users to submit new data.
## Aknowledgements: (see readme.txt)

from django import forms

class LearnForm(forms.Form):
    """
    The form to accept new data from users.
    """

    #the new question
    question = forms.CharField(
        label='Please write a binary question (one with exactly two answers) that would help distinguish this tree further.',
        widget=forms.TextInput(attrs={'class': "input-md new-question-box"})
    )

    #what we can guess about this tree if edge1 is entered
    guess1 = forms.CharField(
        label='If user answers...',
        widget=forms.TextInput(attrs={'class': "input-md"})
        )

    # one possible answer to the question
    edge1 = forms.CharField(
        label='we can conclude this is a...',
        widget=forms.TextInput(attrs={'class': "input-md"})
        )
    #what we can guess about this tree if edge2 is entered
    guess2 = forms.CharField(label='If user answers...',
                widget=forms.TextInput(attrs={'class': "input-md"})
                )

    # one possible answer to the question
    edge2 = forms.CharField(label='we can conclude this is a...',
                widget=forms.TextInput(attrs={'class': "input-md"})
                )

    #the id of the parent node which the two new nodes will come from. This field will be prepopulated and hidden.
    parent_id = forms.CharField(label='parent_id (hide me)',
                    widget=forms.TextInput(attrs={'class': 'input-md hidden'})
                    )

    def is_valid(self):
        """
        validates the entry form
        pre: none
        post: returns if the form has entries for all fields.
        """
        for item in self.data:
            if not self.data[item]:
                return False        # if any fields posted are empty.

        return True     # if we make it to here it is valid
