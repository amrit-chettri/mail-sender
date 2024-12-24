from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    subject = "hait"
    message = "k xa "
    recipient_list = ['test@gmail.com']  
    
    try:
        send_mail(subject, message, 'sender@gmail.com', recipient_list)
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending email: {str(e)}")
