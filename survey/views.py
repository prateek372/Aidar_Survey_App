from typing_extensions import TypeAlias
from django import http
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Response, Type, Question, Patient, Question_Response
from .forms import PatientResponseModelForm, QuestionModelForm, SurveyModelForm, PhysicianResponseModelForm, PatientModelForm
from django.template.defaulttags import register

# Create your views here.

# Landing Page
def landing_page(request):
  return render(request, "landing_page.html")

## Survey Views ----------------------------------

# Survey Type List View
class SurveyTypeListView(generic.ListView):
  template_name = "survey/survey_type_list.html"
  queryset = Type.objects.all()
  context_object_name = "types"


# Create/Add Survey
class SurveyCreateView(generic.CreateView):
  template_name = "survey/survey_create.html"
  form_class = SurveyModelForm

  def get_success_url(self):
      return reverse("survey:survey-type-list")


# Survey List View
def Survey_questions_list(request, pk):
  questions = Question.objects.filter(survey = pk)
  survey_name = Type.objects.get(id=pk)
  context = {
    "survey_name": survey_name,
    "questions": questions
  }
  return render(request, "survey/survey_question_list.html", context)


# Create/Add Question
class QuestionCreateView(generic.CreateView):
  template_name = "survey/question_create.html"
  form_class = QuestionModelForm

  def get_success_url(self):
      return reverse("survey:survey-type-list")
    

# Question Update/Edit
class QuestionUpdateView(generic.UpdateView):
  template_name = "survey/question_update.html"
  form_class = QuestionModelForm

  def get_success_url(self):
      return reverse("survey:survey-type-list")
    
  def get_queryset(self):
      return Question.objects.all()
      # hash={}
      # hash1.append("id": someid, "description": somedescription)
    
      # hash1.append("id": someid, "description": somedescription)
      # Question.objects.bulk_update(hash1)

# Question Delete
def QuestionDeleteView(request, pk):
  question = Question.objects.get(id=pk)
  question.delete()
  return redirect("survey:survey-type-list")


# CBV for Create/Add Patient
class PatientCreateView(generic.CreateView):
  template_name = "survey/patient_create.html"
  form_class = PatientModelForm

  def get_success_url(self):
      return reverse("survey:survey-type-list")


# Assign Survey to Patient
class PhysicianResponseCreateView(generic.CreateView):
  template_name = "survey/physician_response_create.html"
  form_class = PhysicianResponseModelForm

  def get_success_url(self):
      return reverse("survey:survey-type-list")




## Patient Views ----------------------------------

# Class Based View Patient List
# Response_Id is used to lookup assigned Survey
# Response_ID to uniquely identify Patient_ID and Survey_ID
# in cases of multiple survey to a patient

class PatientListView(generic.ListView):
  template_name = "survey/patient_list.html"
  qs_patients = Response.objects.all()
  patients = [] # list of tuples to pass as context
  
  for patient in qs_patients:
    res_id, p_id = patient.id, patient.patient
    patients.append((res_id, p_id))
  
  queryset = patients
  context_object_name = "patients"



# ------------->>>>>>>>>>>>>>

# Custom filter to return range from array length
@register.filter
def get_range(value):
    return range(len(value))


# FBV for Patient Survey-Questions List View
# Survey_ID is idetified from Response DB lookup
# Questions Populated as per Survey_ID

def Patient_questions_list(request, pk):
  # getting servey ID from the response_id
  res_record = Response.objects.get(id=pk)
  res_id = res_record.survey_id
  questions = Question.objects.filter(survey_id=res_id)
  id =[]
  question=[]

  for ques in questions:
    id.append(ques.id)
    question.append(ques.description)
  
  context = {
    'res_id': res_id,
    'question': question,
    'id': id,
    'iterateover': range(len(id))
  }
  return render(request, "survey/patient_question_list.html", context)


# Submit Survey Response
# New Unique Record is created
# Response_ID to uniquely identify Survey_ID and Patient_ID
# Question_ID to uniquely identify answers
def Patient_submit_survey(request):
  res_id = request.POST.get('res_id')
  res_obj = Response.objects.get(pk = res_id)
  res = request.POST.getlist('response')
  ques_id = request.POST.getlist('id')
  
  items = []
  for i in range(len(res)):
    res_item = res_obj
    id_item = ques_id[i]
    ans_item = res[i]
    item = Question_Response(response_id=res_item ,question_id=id_item, answer=ans_item)
    items.append(item)
  Question_Response.objects.bulk_create(items)
  return render(request, "survey/patient_submit.html")



# -------- Depricated Views (all views have been upated to Class Based Views for code Redundancy) ***********************************

# CBV for Question Details
# class QuestionListlView(generic.ListView):
#   template_name = "survey/questions_detail.html"
#   queryset = Question.objects.all()
#   context_object_name = "question"


# CBV for Question Details
# class QuestionDetailView(generic.DetailView):
#   template_name = "survey/question_detail.html"
#   queryset = Question.objects.all()
#   context_object_name = "question"





# ---------------




# CBV for Question Details
# def add_question(request):
#   form = QuestionModelForm
#   if request.method == "POST":
#     form = QuestionModelForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect("survey:survey-list")
#   context = {
#     "form" : form
#   }
#   return render(request, "survey/add_question.html", context)


# def add_survey(request):
#   form = SurveyModelForm
#   if request.method == "POST":
#     form = SurveyModelForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect("survey:survey-list")
#   context = {
#     "form" : form
#   }
#   return render(request, "survey/add_surveyType.html", context)



# def update_question(request, pk):
#   return render(request, "survey: question-update")

# def delete_question(request, pk):
#   question = Question.objects.get(id=pk)
#   question.delete()
#   return redirect("survey:question-list")


# -------------------------------------

#  FBV for Survey List

# def landing_page_view(request):
#   types = Type.objects.all()
#   context = {
#     'types' : types
#   }
#   return render(request, "survey/surveyType_list.html", context)


# -------------------------------------

# FBV for Survey List Details

# def questions_list(request, pk):
#   questions = Question.objects.filter(survey = pk)
#   survey_name = Type.objects.get(id=pk)
#   context = {
#     "survey_name": survey_name,
#     "questions": questions
#   }
#   return render(request, "survey/questions_list.html", context)