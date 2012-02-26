from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label=u'Enter a keyword to Search for', widget=forms.TextInput(attrs={'size':32}))
    