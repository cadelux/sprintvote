from django.contrib import admin
from .models import Topic, Vote

admin.site.register(Topic)
admin.site.register(Vote)
# Bu sayede admin panelinde Topic ve Vote bölümleri görünür yapıyorum.

