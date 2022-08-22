from django.forms import ModelForm
from .models import Project


# take a look at Project/models.py and create a form with all input field which we had there.
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__' # that's to add all field we have in backend
        # to customize our field which comes from backend.
        fields = [
            'title',
            'description',
            'demo_link',
            'source_link',
            'tags'
        ]
