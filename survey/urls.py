from django.urls import path
from django.urls.resolvers import URLPattern
from .views import( SurveyTypeListView, Survey_questions_list, QuestionUpdateView, 
QuestionDeleteView, QuestionCreateView, SurveyCreateView, PhysicianResponseCreateView, 
PatientCreateView, PatientListView, Patient_questions_list, Patient_submit_survey)

# app_name to use INCLUDE and redirect paths to following app
app_name = "survey"

urlpatterns = [
    path('', SurveyTypeListView.as_view(), name='survey-type-list'),
    path('<int:pk>/', Survey_questions_list, name='survey-question-list'),
    path('create-survey/', SurveyCreateView.as_view(), name='survey-create'),
    path('create-question/', QuestionCreateView.as_view(), name='question-create'),
    path('edit/<int:pk>/', QuestionUpdateView.as_view(), name='question-update'),
    path('delete/<int:pk>/', QuestionDeleteView, name='question-delete'),
    path('add-patient/', PatientCreateView.as_view(), name='patient-create'),
    path('list-patient/', PatientListView.as_view(), name='patient-list'),
    path('assign-survey/', PhysicianResponseCreateView.as_view(), name='physician-response-create'),
    path('patient-survey/<int:pk>/', Patient_questions_list, name='patient-response'),
    path('submit/', Patient_submit_survey, name='patient-response-submit'),
    

    
    # Depricated Paths for Depricated Views

    # path('add_survey/', add_survey, name='survey-add'),
    # path('<int:pk>/', QuestionListlView.as_view(), name='question-list'),
    # path('add_question/', add_question, name='question-add'),
    # path('delete_question/<int:pk>', delete_question, name='question-delete'),
    # path('<int:pk>/update_question', update_question, name='question-update'),
]