# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template

from django.shortcuts import render_to_response

from AppSearch.forms import SearchForm

from AppSearch.API.iTunes import search_by_term


def search_page(request):
    form = SearchForm()
    show_results = False
    apps = None
    if 'query' in request.GET:
        show_results = True
        query = request.GET['query'].strip()
        if query:
            apps = search_by_term(query)
            form = SearchForm({'query':query,
                               'apps': apps})
    variables = RequestContext(request, {'form': form,
                                         'show_results':show_results,
                                         'apps': apps})
    
    if request.GET.has_key('ajax'):
        return render_to_response('apps_list.html', variables)
    else:
        return render_to_response('search.html', variables)