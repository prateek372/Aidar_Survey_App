from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import Question, Type, Patient, Response, Question_Response



# Form to Create/Edit Survey_Types DB
class SurveyModelForm(forms.ModelForm):
  class Meta:
    model = Type
    fields =(
      'name',
      'description'
    )


# Form to Create/Edit Question DB
class QuestionModelForm(forms.ModelForm):
  class Meta:
    model = Question
    fields =(
      'description',
      'survey'
    )

# Form to Create/Edit Patient DB
class PatientModelForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = (
      'name',
    )

# Form to Assign Survey to Patients
# Available only to Physicians
class PhysicianResponseModelForm(forms.ModelForm):
  class Meta:
    model = Response
    fields = (
      'survey',
      'patient'
    )
  

# Form to Edit Survey Responses
# Available only to Patients
class PatientResponseModelForm(forms.ModelForm):
  class Meta:
    model = Question_Response
    fields = (
      'answer',
    )