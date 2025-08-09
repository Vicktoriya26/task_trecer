from django import forms
from .models import Task 

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'proirity', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class TaskFilterForm(forms.Form):
    STATUS_CHOISES = [
        ("To Do", "To Do"),
        ("In Progression", "In progression"),
        ("Done", "Done")
    ]

    PRIORITY = [    
        ("low",'low'),
        ("med", "Medium"),
        ('high', 'High'),
        ('2high', 'PIZDA HIGH')
    ]
    status = forms.ChoiceField(choices=STATUS_CHOISES, label='Status', required=False)
    priority = forms.ChoiceField(choices=PRIORITY, label='Priority', required=False)
    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control '})