from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Appointment, Diet, Bloodsugar, Weight, Exercise
from .forms import AppointmentForm,DietForm,BloodsugarForm,WeightForm,ExerciseForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView,CreateView
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

class homeview(View):
    def get(self,request,*args,**kwargs):
        appointment_list = Appointment.objects.filter(user=request.user.pk).filter(appointmenttime__gt=datetime.now()).order_by('appointmenttime')
        bloodsugar_list = Bloodsugar.objects.filter(user=request.user.pk).order_by('-measuretime')
        weight_list = Weight.objects.filter(user=request.user.pk).order_by('-measuretime')

        time_threshold = datetime.now() + timedelta(days=7)
        print(datetime.now(),time_threshold)
        close_appoint_list = appointment_list.filter(appointmenttime__lt=time_threshold).filter(appointmenttime__gt=datetime.now())

        context = {
            'appointment_list': appointment_list,
            'bloodsugar_list': bloodsugar_list,
            'weight_list': weight_list,
            'close_appoint_list':close_appoint_list,

        }

        return render(request,"homepage.html",context)




def diabetes_education(request):
    links = [
        {"name": "American Diabetes Association", "url": "http://www.diabetes.org"},
        {"name": "Centers for Disease Control and Prevention", "url": "http://www.cdc.gov/diabetes"},
        {"name": "National Institute of Diabetes and Digestive and Kidney Diseases", "url": "http://www.niddk.nih.gov"},
        {"name": "Mayo Clinic", "url": "http://www.mayoclinic.org/diseases-conditions/diabetes"},
        {"name": "Diabetes Self-Management", "url": "http://www.diabetesselfmanagement.com"},
        {"name": "Diabetes Forecast", "url": "http://www.diabetesforecast.org"},
        {"name": "Juvenile Diabetes Research Foundation", "url": "http://www.jdrf.org"},
        {"name": "The Diabetic Life", "url": "http://www.thediabeticlife.com"},
        {"name": "Diabetes Daily", "url": "http://www.diabetesdaily.com"},
        {"name": "Diabetic Connect", "url": "http://www.diabeticconnect.com"},
    ]
    context = {"links": links}
    return render(request, "education.html", context)


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointmentlist.html'
    paginate_by = 10

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user).order_by('appointmenttime')


class AppointmentAddView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment.html'
    success_url = reverse_lazy('appointments_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AppointmentAddView, self).form_valid(form)

class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = 'appointment.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('appointments_list') # redirect to the list view after successful update

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('appointments_list') # redirect to the list view after successful deletion


class BloodsugarListView(ListView):
    model = Bloodsugar
    template_name = 'bloodsugarlist.html'
    paginate_by = 10

    def get_queryset(self):
        return Bloodsugar.objects.filter(user=self.request.user).order_by('-measuretime')

class BloodsugarAddView(CreateView):
    model = Bloodsugar
    form_class = BloodsugarForm
    template_name = 'bloodsugar.html'
    success_url = reverse_lazy('bloodsugar_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BloodsugarAddView, self).form_valid(form)

class BloodsugarUpdateView(UpdateView):
    model = Bloodsugar
    template_name = 'bloodsugar.html'
    fields = ['bloodsugarmeasure', 'measuretime']
    def get_success_url(self):
        return reverse_lazy('bloodsugar_list')

class BloodsugarDeleteView(DeleteView):
    model = Bloodsugar
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('bloodsugar_list') # redirect to the list view after successful deletion


class DietListView(ListView):
    model = Diet
    template_name = 'dietlist.html'
    paginate_by = 10
    def get_queryset(self):
        return Diet.objects.filter(user=self.request.user).order_by('-recordtime')

class DietAddView(CreateView):
    model = Diet
    form_class = DietForm
    template_name = 'diet.html'
    success_url = reverse_lazy('diet_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DietAddView, self).form_valid(form)

class DietUpdateView(UpdateView):
    model = Diet
    template_name = 'diet.html'
    fields = ['food','quantity','recordtime']
    success_url = reverse_lazy('diet_list') # redirect to the list view after successful update

class DietDeleteView(DeleteView):
    model = Diet
    template_name = 'diet_confirm_delete.html'
    success_url = reverse_lazy('diet_list') # redirect to the list view after successful deletion


######  Weight Starts from Here, Unit: Pound ######

class WeightListView(ListView):
    model = Weight
    template_name = 'weightlist.html'
    paginate_by = 10

    def get_queryset(self):
        return Weight.objects.filter(user=self.request.user).order_by('-measuretime')


class WeightAddView(CreateView):
    model = Weight
    form_class = WeightForm
    template_name = 'weight.html'
    success_url = reverse_lazy('weight_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WeightAddView, self).form_valid(form)


class WeightUpdateView(UpdateView):
    model = Weight
    template_name = 'weight.html'
    fields = ['weight', 'measuretime']
    def get_success_url(self):
        return reverse_lazy('weight_list')

class WeightDeleteView(DeleteView):
    model = Weight
    template_name = 'weight_confirm_delete.html'
    success_url = reverse_lazy('weight_list') # redirect to the list view after successful deletion


######  Weight Ends Here ######

class ExerciseAddView(CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'exercise.html'
    success_url = reverse_lazy('exercise_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExerciseAddView,self).form_valid(form)

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exerciselist.html'
    paginate_by = 10

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user).order_by('-exercisedate')

class ExerciseUpdateView(UpdateView):
    model = Exercise
    template_name = 'exercise.html'
    fields = ['exercise','currentweight','hour']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['exercise'].label = 'Exercise Name'
        form.fields['currentweight'].label = 'Current Weight (Kg)'
        return form

    success_url = reverse_lazy('exercise_list') # redirect to the list view after successful update

class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'exercise_confirm_delete.html'
    success_url = reverse_lazy('exercise_list')
