# -*- coding: utf-8 -*-

# Create your views here.

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from contact_app.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            html_content = render_to_string('contact_mail_template.html', {
                'name': cd['name'],
                'message': cd['message']
            })

            text_content = strip_tags(html_content)

            msg = EmailMultiAlternatives(
                cd['subject'],
                text_content,
                cd.get('email', 'from@example.com'),   # from -> try to get the given email, defaults to second attribute
                ['to@example.com']   # [to] -> valid email list to receive the message
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # You must provide SMTP info to allow email sending

            return HttpResponseRedirect('/correct')
    else:
        form = ContactForm()

    return render_to_response('contact_app/contact.html', {'form': form}, context_instance = RequestContext(request))

def correct(request):
    return render_to_response('contact_app/correct.html', {}, context_instance = RequestContext(request))