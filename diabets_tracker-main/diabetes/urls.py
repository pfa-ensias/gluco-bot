from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include

from diabetes.views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path("diabetes_education/", diabetes_education, name="diabetes_education"),

# Appointment
    path('appointlist/', AppointmentListView.as_view(),name='appointments_list'),
    path('appointadd/', AppointmentAddView.as_view(), name='appoint_add'),
    path('appointupdate/<int:pk>', AppointmentUpdateView.as_view(), name='appoint_update'),
    path('appointdelete/<int:pk>', AppointmentDeleteView.as_view(), name='appoint_delete'),
# Bloodsugar
    path('bloodsugarlist/', BloodsugarListView.as_view(), name='bloodsugar_list'),
    path('bloodsugaradd/', BloodsugarAddView.as_view(), name='bloodsugar_add'),
    path('bloodsugarupdate/<int:pk>', BloodsugarUpdateView.as_view(), name='bloodsugar_update'),
    path('bloodsugardelete/<int:pk>', BloodsugarDeleteView.as_view(), name='bloodsugar_delete'),
# Diet
    path('dietlist/', DietListView.as_view(), name='diet_list'),
    path('dietadd/', DietAddView.as_view(), name='diet_add'),
    path('dietupdate/<int:pk>', DietUpdateView.as_view(), name='diet_update'),
    path('dietdelete/<int:pk>', DietDeleteView.as_view(), name='diet_delete'),

#weight
    path('weightlist/', WeightListView.as_view(), name='weight_list'),
    path('weightadd/', WeightAddView.as_view(), name='weight_add'),
    path('weightupdate/<int:pk>', WeightUpdateView.as_view(), name='weight_update'),
    path('weightdelete/<int:pk>', WeightDeleteView.as_view(), name='weight_delete'),



# Exercise
    path('exerciseadd/', ExerciseAddView.as_view(), name='exercise_add'),
    path('exerciselist/', ExerciseListView.as_view(), name='exercise_list'),
    path('exerciseupdate/<int:pk>', ExerciseUpdateView.as_view(), name='exercise_update'),
    path('exercisedelete/<int:pk>', ExerciseDeleteView.as_view(), name='exercise_delete'),

]
