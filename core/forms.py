from django import forms
from .models import Degree,Course,Document,PlanningExam

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'documenttype', 'course', 'document']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DocumentForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['course'].queryset = Course.objects.filter(user=user)