from django.shortcuts import render, get_object_or_404

from .models import Entry, Client, Project


def entries(request):
    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
    })

def projects(request):
    project_list = Project.objects.all()
    return render(request, 'projects.html', {
        'project_list': project_list,
    })

def clients(request):
    client_list = Client.objects.all()
    return render(request, 'clients.html', {
        'client_list': client_list,
    })

def client_summary(request, id):
    client = get_object_or_404(Client, pk=id)

    # This could also be done in the template with {{ client.project_set }}
    projects_list = Project.objects.filter(client=client)

    return render(request, 'client_summary.html', {
        'client': client,
        'projects_list': projects_list,
    })
