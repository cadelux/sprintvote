from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # Giriş yapılmadan bu sayfa açılamaz
from .models import Topic, Vote
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # kullanıcıyı otomatik giriş yaptır
            return redirect('/')  # anasayfaya gönder
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Basit oy formu
class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['choice']
        widgets = {
            'choice': forms.RadioSelect(choices=[(True, 'Evet'), (False, 'Hayır')])
        }

# Tüm konuların listesi (giriş yaptıktan sonra)
@login_required
def home(request):
    topics = Topic.objects.all()
    return render(request, 'home.html', {'topics': topics})

# Seçilen konuya gidip oy kullanma ve sonucu görme
@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    user_vote = Vote.objects.filter(topic=topic, user=request.user).first()

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            Vote.objects.update_or_create(
                topic=topic,
                user=request.user,
                defaults={'choice': form.cleaned_data['choice']}
            )
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = VoteForm(instance=user_vote)

    yes_count = Vote.objects.filter(topic=topic, choice=True).count()
    no_count = Vote.objects.filter(topic=topic, choice=False).count()
    all_votes = Vote.objects.filter(topic=topic).select_related('user')
    # Konuya ait tüm oyları çek
    return render(request, 'topic_detail.html', {
        'topic': topic,
        'form': form,
        'yes_count': yes_count,
        'no_count': no_count,
        'user_vote': user_vote,
        'all_votes': all_votes,
    })
  

