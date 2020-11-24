from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.core.mail import send_mail

@csrf_exempt
def index(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'CHECK-POINT-ENQUIRY'#form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']

            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            message_plus_phone = message+phone

            try:
                print("Sending Email"
                      )

                from django.core.mail import send_mail


                if message_plus_phone:
                    #message to us saying their inquiry
                    a = send_mail(subject, message_plus_phone, 'info@check-point.us',
                                  ['aiden3189@gmail.com', 'ksalette88@gmail.com'], fail_silently=True)

                    b = send_mail(subject, 'Thank you for reaching out, we will respond to your message as soon as we can.', 'info@check-point.us',
                                  [from_email], fail_silently=True )

                print("Email Sent", a, b)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success_view')

    context = { 'form': form}
    return render(request, 'content/index.html', context)

def success_view(request):
    return HttpResponse('Thank you for reaching out, we will respond to your message as soon as we can.')

@csrf_exempt
def send_email(request):

    #https://support.google.com/accounts/answer/6010255
    #
    # print("Sending Email"
    # )
    #
    #
    # from django.core.mail import send_mail
    #
    # a=send_mail('Subject', 'Message.', 'info@check-point.us', ['aiden3189@gmail.com', 'ksalette88@gmail.com'],)
    #
    # print("Email Sent", a)

    return HttpResponse('ok')

def about(request):
    context = { 'a': 0}
    return render(request, 'content/about.html', context)


def contact(request):
    context = { 'a': 0}
    return render(request, 'content/contact.html', context)