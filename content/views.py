from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):

    if request.method == 'POST':

        #https://support.google.com/accounts/answer/6010255
        from django.conf import settings

        from django.core.mail import send_mail

        print("Sending Email"
              )

        from django.core.mail import send_mail

        a = send_mail('Subject', 'Prod Message.', 'info@check-point.us', ['aiden3189@gmail.com', 'ksalette88@gmail.com'], )

        print("Email Sent", a)



    context = { 'a': 0}
    return render(request, 'content/index.html', context)



@csrf_exempt
def send_email(request):

    #https://support.google.com/accounts/answer/6010255

    print("Sending Email"
    )


    from django.core.mail import send_mail

    a=send_mail('Subject', 'Message.', 'info@check-point.us', ['aiden3189@gmail.com', 'ksalette88@gmail.com'],)

    print("Email Sent", a)

    return HttpResponse('ok')

def about(request):
    context = { 'a': 0}
    return render(request, 'content/about.html', context)


def contact(request):
    context = { 'a': 0}
    return render(request, 'content/contact.html', context)