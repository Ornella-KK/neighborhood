from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone

# Create your tests here.
class NeighborhoodTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='nella')
        self.user.save()
        self.hood = Neighborhood(name='Ornella',location='Kigali',description="my hood",photo='photo.url',user=self.user)
        self.hood.create_neighborhood()


    def tearDown(self):
        Neighborhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood,Neighborhood))

    def test_create_neighborhood(self):
        self.hood.create_neighborhood()
        hoods = Neighborhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_neighborhood(self):
        self.hood.create_neighborhood()
        self.hood.delete_neighborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood) == 0)

class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.hood = Neighborhood(name='ornella')
        self.hood.save()
        self.user = User(username='nella')
        self.user.save()
        self.profile = Profile(photo='me',bio='bio',email="abc@xyz.com",user=self.user,neighborhood=self.hood)
        self.profile.save_profile()


    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

class BusinessTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='nella')
        self.user.save()
        self.hood = Neighborhood(name='ornella')
        self.hood.save()
        self.business = Business(name='Restaurant-Bar',propreiter=self.user,neighborhood=self.hood,email='ourbusiness@gmail.com')
        self.business.create_business()


    def tearDown(self):
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_create_business(self):
        self.business.create_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_neighborhood(self):
        self.business.create_business()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)

class AlertTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='nella')
        self.user.save()
        self.hood = Neighborhood(name='ornella')
        self.hood.save()
        self.alert = Alert(alert='New in the hood',posted_by=self.user,neighborhood=self.hood)
        self.alert.save_alert()

    def tearDown(self):
        Alert.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.alert,Alert))

    def test_create_business(self):
        self.alert.save_alert()
        alert = Alert.objects.all()
        self.assertTrue(len(alert) > 0)

    def test_delete_neighborhood(self):
        self.alert.save_alert()
        self.alert.delete_alert()
        alert = Alert.objects.all()
        self.assertTrue(len(alert) == 0)
