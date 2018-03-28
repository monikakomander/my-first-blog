from django.db import models
from django.utils import timezone

class Post(models.Model): # ta linijka definiuje nasz model (jest on obiektem, czyli object)
    # class to specjalne słowo kluczowe, które sygnalizuje, że tworzymy obiekt.
    # Post to nazwa naszego modelu. Możemy nadać mu inną nazwę (bez polskich liter, znaków specjalnych i spacji). Zawsze zaczynaj nazwę modelu wielką literą.
    # models.Model oznacza, że nasz obiekt Post jest modelem Django. W ten sposób Django wie, że powinien go przechowywać w bazie danych.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # models.ForeignKey - odnośnik do innego modelu
    title = models.CharField(max_length=200) # models.CharField - tekst z ograniczoną liczbą znaków
    text = models.TextField() # models.TextField -  dłuższe teksty bez ograniczeń w ilości znaków
    created_date = models.DateTimeField( #models.DateTimeField - data i godzina
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self): # metoda publikująca wpis na blogu (publish). Wyraz def oznacza, że mamy do czynienia z funkcją/metodą, a publish to nazwa metody.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title # otrzymamy tekst (string) zawierający tytuł wpisu