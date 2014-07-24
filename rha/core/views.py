# coding: utf-8
from django.shortcuts import render


def home(request):
    context = {}

    # if request.method == 'POST':
    #     contact_form = ContactForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.send_mail()
    #         context['contact_success'] = True
    # else:
    #     contact_form = ContactForm()

    # context['contact_form'] = contact_form

    return render(request, 'index.html', context)
