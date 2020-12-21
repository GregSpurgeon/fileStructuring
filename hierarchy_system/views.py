from django.shortcuts import render
from hierarchy_system.models import Folder
# Create your views here.


def tree_view(request):
    return render(request, 'folders.html', {'folders': Folder.objects.all()})
