from django.db import models
from django.contrib.auth.models import User  # Django’nun hazır kullanıcı modeli

# Oylamaya sunulacak konu başlıkları
class Topic(models.Model):
    title = models.CharField(max_length=200)  # Konunun kısa başlığı

    def __str__(self):
        return self.title

# Kullanıcının verdiği oy
class Vote(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # Hangi konuya
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # Hangi kullanıcı oy vermiş
    choice = models.BooleanField()  # True = Evet, False = Hayır

    class Meta:
        unique_together = ('topic', 'user')  # Her kullanıcı bir konuda sadece 1 oy verebilir
