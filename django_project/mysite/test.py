from django.test import TestCase


class Animal:
    
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        

    
    def speak(self):
        return 'The {} says "{}"'.format(self.name, self.sound)
     


class TestCase(TestCase):
    def setUp(self):
        self.animal1 = Animal(name="lion", sound="roar")
        self.animal2 = Animal(name="cat", sound="meow")
        self.animal3 = Animal(name="Lula", sound="Picanha")
       

    def test_animals_can_speak(self):
        self.assertEqual(self.animal1.speak(),'The lion says "roar"')
        self.assertEqual(self.animal2.speak(),'The cat says "meow"')
        self.assertEqual(self.animal3.speak(),'The Lula says "Fake"')
        