from django.test import TestCase
from .models import Profile,NeighbourHood,Business
from django.contrib.auth.models import User
# Create your tests here.


class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='kabagemark',first_name='mark',last_name='kabage',email='kabagemark@gmail.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
    
    def test_data(self):
        self.assertTrue(self.user.username,"kabagemarl")
        self.assertTrue(self.user.first_name,"mark")
        self.assertTrue(self.user.last_name,'kabage')
        self.assertTrue(self.user.email,'kabagemark@gmail.com')
    
    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)
    
    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)


class ProfileTest(TestCase):
    def setUp(self):
        self.new_profile=Profile(name ="mark",bio='i love technology',location="Mombasa",profile_photo="https://www.google.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    
    def test_data(self):
        self.assertTrue(self.new_profile.bio,"i love technology")
        self.assertTrue(self.new_profile.name,"mark")
        self.assertTrue(self.new_profile.location,"Mombasa")
        self.assertTrue(self.new_profile.profile_photo,"https://www.google.com")

    def test_save(self):
        self.new_profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    
    def test_delete(self):
        profile = Profile.objects.filter(id=1)
        profile.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)

    
    def test_edit_profile(self):
        self.new_profile.save()
        self.update_profile = Profile.objects.filter(bio='i love technology').update(bio = 'i love technology')
        self.updated_profile = Profile.objects.get(bio='i love technology')
        self.assertTrue(self.updated_profile.bio,'i love technology')





class NeighbourHoodTest(TestCase):
    def setUp(self):
        self.user=User(username='kabagemark',first_name='mark',last_name='kabage',email='kabagemark@gmail.com')
        self.user.save()
        self.new_NeighbourHood=NeighbourHood( Occupants_count="6",name='Umoja',location='Mombasa')
        self.new_NeighbourHood = NeighbourHood( Occupants_count="6",name='Umoja',location='Mombasa')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_NeighbourHood,NeighbourHood))
    
    def test_data(self):
        self.assertTrue(self.new_NeighbourHood.location,'Mombasa')
        
    def test_save(self):
        self.new_NeighbourHood.save()
        Hood = NeighbourHood.objects.all()
        self.assertTrue(len(Hood)>0)
    
    def test_delete(self):
        Hood = NeighbourHood.objects.filter(id=1)
        Hood.delete()
        Hood = NeighbourHood.objects.all()
        self.assertTrue(len(Hood)==0)

    def test_update_post(self):
        self.new_NeighbourHood.save()
        self.update_NeighbourHood = NeighbourHood.objects.filter(name='Umoja').update(name='barnabas')
        self.updated_NeighbourHood = NeighbourHood.objects.get(name='barnabas')
        self.assertTrue(self.updated_NeighbourHood.name,'barnabas')