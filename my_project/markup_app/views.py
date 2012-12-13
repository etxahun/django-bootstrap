# -*- coding: utf-8 -*-

# Create your views here.

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def index(request):
    return render_to_response('markup_app/markup_base.html', {}, context_instance = RequestContext(request))


def typography(request):
    return render_to_response('markup_app/typography/headings.html', {}, context_instance = RequestContext(request))


def emphasis(request):
    return render_to_response('markup_app/typography/emphasis.html', {}, context_instance = RequestContext(request))


def blockquotes(request):
    return render_to_response('markup_app/typography/blockquotes.html', {}, context_instance = RequestContext(request))
