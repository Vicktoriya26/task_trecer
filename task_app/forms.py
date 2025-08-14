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
        ("", "Всі"),
        ('todo', 'Треба зробити'),
        ('in_progress', 'Виконується'),
        ('done', 'Виконано'),
    ]

    PRIORITY = [  
        ("", "Всі"),  
        ('low', 'Низбкий'),
        ('middle', 'Середній'),
        ('high', 'Високий'),
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOISES, label='Status', required=False)
    priority = forms.ChoiceField(choices=PRIORITY, label='Priority', required=False)
    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control '})