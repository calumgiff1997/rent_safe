from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


#Adam here -- this is just so that i can test out my templates, will be deleted
def templateTest(request):
    return render(request, 'dashboard/index.html')
