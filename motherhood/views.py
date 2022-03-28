from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import pro_skills, Location, Nanny
from .forms import ContactForm, FilterNannies
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
    nannies = Nanny.objects.all()[:4]

    return render(request,'index.html',{"nannies":nannies})

def about(request):

    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name':form.cleaned_data['first_name'],
                'last_name':form.cleaned_data['last_name'],
                'email_address':form.cleaned_data['email_address'],
                'message':form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("inquiry_received")
    form = ContactForm()

    return render(request,'contact.html',{'form':form})

def nannies(request):
    nannies = Nanny.objects.all()

    return render(request,'nannies.html',{"nannies":nannies})

def profile(request):

    return render(request,'profile.html')



def pricing(request):
    nannies = Nanny.objects.all()

    return render(request,'pricing.html',{"nannies":nannies})

def services(request):

    return render(request,'services.html')

def testimonial(request):

    return render(request,'testimonial.html')

def inquiry_received(request):

    return render(request,'inquiry_received.html')

def book_nanny(request, nanny_id):
    nanny = Nanny.objects.get(id=nanny_id)

    try:
        nanny = Nanny.objects.get(id=nanny_id)
    except:
        raise ObjectDoesNotExist()

    return render(request,"book_nanny.html",{"nanny":nanny})

def search_results(request):

    if 'nanny' in request.GET and request.GET["nanny"] and 'skill' in request.GET and request.GET["skill"]:
        search_term = request.GET.get("nanny")
        skill_search = request.GET.get("skill")
        filtered_nannies = Nanny.filter_nannies(search_term, skill_search).distinct()
        message=f"{search_term} and {skill_search}"

        print(filtered_nannies)

        return render(request,'filtered_nannies.html',{"message":message,"filtered_nannies":filtered_nannies})

    else:
        message = "You haven't searched for any term"
        return render(request,'filtered_nannies.html',{"message":message})
