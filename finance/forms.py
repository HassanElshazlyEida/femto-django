from django import forms
from .models import Goal
import datetime

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['total_amount', 'goal_date']
        widgets = {
            'goal_date': forms.DateInput(attrs={'type': 'date'})
        }
    def clean_goal_date(self):
        goal_date = self.cleaned_data['goal_date']
        current_date = datetime.date.today() + datetime.timedelta(days=30)

        if goal_date <= current_date:
            raise forms.ValidationError("Goal date must be at least one month from today.")

        return goal_date