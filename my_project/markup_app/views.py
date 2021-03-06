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


def code(request):
    return render_to_response('markup_app/code.html', {}, context_instance = RequestContext(request))


def headings(request):
    return render_to_response('markup_app/typography/headings.html', {}, context_instance = RequestContext(request))


def emphasis(request):
    return render_to_response('markup_app/typography/emphasis.html', {}, context_instance = RequestContext(request))


def blockquotes(request):
    return render_to_response('markup_app/typography/blockquotes.html', {}, context_instance = RequestContext(request))


def lists(request):
    return render_to_response('markup_app/typography/lists.html', {}, context_instance = RequestContext(request))


def buttons(request):
    return render_to_response('markup_app/buttons.html', {}, context_instance = RequestContext(request))


def tables(request):
    return render_to_response('markup_app/tables.html', {}, context_instance = RequestContext(request))


def forms(request):
    return render_to_response('markup_app/forms.html', {}, context_instance = RequestContext(request))
