from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# Model for Syrvey Types (Each survey Type will have a list of questions)
class Type(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  description = models.CharField(max_length=200)

  def __str__(self):
      return self.name

# Model for Syrvey Questions --> Foreign Key = Type_ID
class Question(models.Model):
  id = models.AutoField(primary_key=True)
  description = models.CharField(max_length=200)
  survey = models.ForeignKey('Type', on_delete=models.CASCADE)

  def __str__(self):
      # return  self.description
      return '{}_{}'.format(self.id, self.description)

# Model for Patient Details
class Patient(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)

  def __str__(self):
      return self.name

# Model for Store Responses
# FK --> Survey Type_ID
# # FK --> Patient_ID
class Response(models.Model):
  id = models.AutoField(primary_key=True)
  survey = models.ForeignKey('Type', on_delete=models.CASCADE)
  patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
  
  def __str__(self):
      # return str(self.survey)
      return '{}_{}_{}'.format(self.id, self.survey, self.patient)


class Question_Response(models.Model):
  id = models.AutoField(primary_key=True)
  question_id = models.CharField(max_length=100)
  response_id = models.ForeignKey('Response', on_delete=models.CASCADE)
  answer = models.CharField(max_length=200)

  def __str__(self):
      return self.answer