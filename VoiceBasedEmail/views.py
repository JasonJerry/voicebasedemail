from django.shortcuts import render, redirect
from oauth2client.contrib.django_util import decorators
from django.http import HttpResponse
from .services import *
from googleapiclient.discovery import build
from django.contrib import messages
    
@decorators.oauth_enabled
def inbox(request):
    service = build(serviceName='gmail', version='v1',
            http=request.oauth.http)
    maillist=ListMessagesMatchingQuery(service, 'me')
    number=0
    while number < maillist.__len__() :
        current_message=GetMimeMessage(service,"me",maillist[number]['id'])
        number=number+1

    context = {"page_title": "Inbox", "current_message": current_message,}
    return render(request, "inbox.html", context)

@decorators.oauth_enabled
def compose(request):
    if request.method == 'POST':
        if request.POST['to'] is None:
            messages.error(request, u'To Email required.')
            context = {"page_title": "Inbox"}
            return render(request, "inbox.html", context)
        if request.POST['subject'] is None:
            messages.error(request, u'Subject required.')
            context = {"page_title": "Inbox"}
            return render(request, "inbox.html", context)
        if request.POST['body'] is None:
            messages.error(request, u'Body required.')
            context = {"page_title": "Inbox"}
            return render(request, "inbox.html", context)
        created_message=CreateMessage('me', request.POST['to'], request.POST['subject'], request.POST['body'])
        service = build(serviceName='gmail', version='v1',
                http=request.oauth.http)
        sent_message=SendMessage(service, 'me', created_message)
        messages.success(request, u'Email sent.')
        context = {"page_title": "Inbox"}
        return render(request, "compose.html", context)
    context = {"page_title": "Compose"}
    return render(request, "compose.html", context)

@decorators.oauth_enabled
def read(request):
    context = {"page_title": "Read"}
    return render(request, "read.html", context)

@decorators.oauth_enabled
def index(request):
    if request.oauth.has_credentials():
        return render(request, "index.html")
    else:
        return HttpResponse('Here is an OAuth Authorize link:<a href="{}">Authorize</a>'.format(request.oauth.get_authorize_redirect()))
