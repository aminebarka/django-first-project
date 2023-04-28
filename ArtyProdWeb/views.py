from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from django.views import index 
from .models import Project, Service, TeamMember
from .forms import ContactForm

def home(request):
     return render(request, 'index.html')


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'artyprod/portfolio/list.html'


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'artyprod/portfolio/detail.html'


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'artyprod/services/list.html'


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'artyprod/services/detail.html'


class TeamMemberListView(ListView):
    model = TeamMember
    context_object_name = 'team_members'
    template_name = 'artyprod/team/list.html'


class TeamMemberDetailView(DetailView):
    model = TeamMember
    context_object_name = 'team_member'
    template_name = 'artyprod/team/detail.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = [settings.CONTACT_EMAIL]
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return render(request, 'artyprod/contact/thanks.html')
    else:
        form = ContactForm()

    return render(request, 'artyprod/contact/contact.html', {'form': form})
