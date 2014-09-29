# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from models import (Course, Objective, Public, Subscribe,
                    Contact)


class ContactForm(forms.Form):
    name = forms.CharField(label=u'Nome',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Nome:'}))
    phone = forms.CharField(label=u'Fone',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Fone:'}))
    email = forms.EmailField(label=u'E-mail',
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'E-mail:'}))
    subject = forms.CharField(label=u'Assunto',
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control',
                                         'placeholder': 'Assunto:'}))
    message = forms.CharField(label=u'Mensagem',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': 6,
                                         'placeholder': 'Mensagem:'}))

    def send_mail(self):
        subject = u'Contato do site (%s)' % self.cleaned_data['name']
        context = {
            'name': self.cleaned_data['name'],
            'phone': self.cleaned_data['phone'],
            'email': self.cleaned_data['email'],
            'subject': self.cleaned_data['subject'],
            'message': self.cleaned_data['message'],
        }
        email_to = 'contato@rhape.com.br'
        message = render_to_string('contact_mail.txt', context)
        message_html = render_to_string('contact_mail.html', context)
        msg = EmailMultiAlternatives(subject, message,
                                     'no-reply@rhape.com.br', [email_to])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()


class CourseModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
                                  attrs={'cols': 60, 'rows': 6}))

    class Meta:
        model = Course


class ObjectiveModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
                                  attrs={'cols': 60, 'rows': 6}))

    class Meta:
        model = Objective


class PublicModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
                                  attrs={'cols': 60, 'rows': 6}))

    class Meta:
        model = Public


class ContactModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
                              attrs={'cols': 60, 'rows': 6}))

    class Meta:
        model = Contact


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe

    def send_mail(self):
        subject = u'Inscrição do site (%s)' % self.cleaned_data['name']
        context = {
            'name': self.cleaned_data['name'],
            'mobile': self.cleaned_data['mobile'],
            'email': self.cleaned_data['email'],
        }

        email_to = 'contato@rhape.com.br'
        message = render_to_string('subscribe_mail.txt', context)
        message_html = render_to_string('subscribe_mail.html', context)
        msg = EmailMultiAlternatives(subject, message,
                                     'no-reply@rhape.com.br', [email_to])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()
