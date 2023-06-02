import datetime
import string
import factory
#pip install django-factory
#pip install factory-boy
from factory import fuzzy
from faker import Faker
from django.db.models import Max

from diabetes import models
from factory.django import DjangoModelFactory
from factory import LazyAttribute

fake = Faker()



class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User
        django_get_or_create = ('username', 'email')

    username = factory.Sequence(lambda n: f'user{n}')
    email = LazyAttribute(lambda obj: f"{obj.username}@{fake.domain_name()}")




class bloodsugarFactory(DjangoModelFactory):
    class Meta:
        model = models.Bloodsugar

    user = factory.SubFactory(UserFactory)
    measuretime = fuzzy.FuzzyDate(datetime.date(2018, 1, 1))
    bloodsugarmeasure = fuzzy.FuzzyInteger(40, 400)



class appointmentFactory(DjangoModelFactory):
    class Meta:
        model = models.Appointment

    user = factory.SubFactory(UserFactory)
    appointmenttime = fuzzy.FuzzyDate(datetime.date(2018, 1, 1))
    hospital = factory.Faker('word')
    provider = factory.Faker('last_name')


class dietFactory(DjangoModelFactory):
    class Meta:
        model = models.Diet

    user = factory.SubFactory(UserFactory)
    quantity = fuzzy.FuzzyInteger(0, 100)
    food =fuzzy.FuzzyChoice(models.Food.name, getter=lambda c: c[0])

