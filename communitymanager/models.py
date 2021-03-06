from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Communaute(models.Model):
    nom = models.CharField(max_length=200)
    abonnes = models.ManyToManyField(User, related_name="communautes")
    description = models.TextField()
    managers = models.ManyToManyField(User, related_name="communautes_managed")
    open = models.BooleanField(default=True)
    suspended = models.IntegerField(default=0)
    banned = models.ManyToManyField(User, blank=True, related_name="communautes_banned")


    class Meta:
        verbose_name = "Communaute"

    def __str__(self):
        return self.nom


class Priorite(models.Model):
    label = models.CharField(max_length=200)
    degre = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Priorite"

    def __str__(self):
        return self.label



class Post(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    communaute = models.ForeignKey('Communaute', on_delete=models.CASCADE)
    priorite = models.ForeignKey('Priorite', on_delete=models.CASCADE)
    evenementiel = models.BooleanField()
    date_evenement = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)
    avertissement = models.BooleanField(default=False)
    lecteurs =models.ManyToManyField(User, related_name="posts")
    lu = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='post_like')

    def number_of_likes(self):
        return self.likes.count()


    class Meta:
        verbose_name = "Post"

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)


    class Meta:
        verbose_name = "Commentaire"

    def __str__(self):
        return self.contenu

