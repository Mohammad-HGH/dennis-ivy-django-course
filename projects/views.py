
from django.shortcuts import render


# Create your views here.

projectList = [
    {
        "id": "1",
        "title": "Ecommerce Website",
        "description": "Fully functional ecommerce website",
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "This is a personal website",
    },
    {
        "id": "3",
        "title": "Social network",
        "description": "Awesome open source social media",
    },
]


def projects(request):
    pages = projectList
    return render(request, "projects/projects.html", {"pages": pages})


def project(request, pk):
    projectObj = None
    for i in projectList:
        if i["id"] == pk:
            projectObj = i

    return render(request, "projects/single-project.html", {"project": projectObj})
