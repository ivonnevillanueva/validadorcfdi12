#from cfdi.models import Cfdi
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def validador(request):
    return  render(request,'validador.html', {'validador':validador})
