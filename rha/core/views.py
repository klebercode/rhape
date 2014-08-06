# coding: utf-8
from django.shortcuts import render

from forms import ContactForm, SubscribeForm
from models import (Enterprise, Contact, Team, Cost, Partner,
                    Gallery, Course, Objective, Public, Step)


def home(request):
    context = {}
    context['enterprises'] = Enterprise.objects.all()
    context['contacts'] = Contact.objects.all()
    context['teans'] = Team.objects.all()
    context['costs'] = Cost.objects.all()
    context['partners'] = Partner.objects.all()
    context['galleries'] = Gallery.objects.all()
    context['courses'] = Course.objects.all()
    context['objectivies'] = Objective.objects.all()
    context['publics'] = Public.objects.all()
    context['steps'] = Step.objects.all()

    if request.method == 'POST':
        if request.POST['action'] == 'contact':
            contact_form = ContactForm(request.POST, prefix='Contact')
            subscribe_form = SubscribeForm(prefix='Subscribe')
            if contact_form.is_valid():
                contact_form.send_mail()
                context['contact_success'] = True
        elif request.POST['action'] == 'subscribe':
            subscribe_form = SubscribeForm(request.POST,
                                           prefix='Subscribe')
            contact_form = ContactForm(prefix='Contact')
            if subscribe_form.is_valid():
                obj = subscribe_form.save()
                subscribe_form.send_mail()
                context['subscribe_success'] = True
    else:
        contact_form = ContactForm(prefix='Contact')
        subscribe_form = SubscribeForm(prefix='Subscribe')

    context['contact_form'] = contact_form
    context['subscribe_form'] = subscribe_form

    return render(request, 'index.html', context)
