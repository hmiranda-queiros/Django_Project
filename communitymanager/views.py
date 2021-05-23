from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import *
from .forms import *


@login_required
def communautes(request):
    communities = Communaute.objects.all()
    abonnement = Communaute.objects.filter(abonnes=request.user)
    return render(request, 'communitymanager/voir_communautes.html', locals())


@login_required
def abonnement(request, action, com_id):
    com = get_object_or_404(Communaute, pk=com_id)

    if action == "abo":
        com.abonnes.add(request.user)
        com.save()
    elif action == "desabo":
        com.abonnes.remove(request.user)
        com.save()

    return redirect('communautes')


@login_required
def communaute(request, com_id):
    com = get_object_or_404(Communaute, pk=com_id)
    posts = Post.objects.filter(communaute=com_id)
    user = request.user
    return render(request, 'communitymanager/voir_posts.html', locals())


@login_required
def post(request, post_id):
    form = CommentaireForm(request.POST or None)

    if form.is_valid():
        contenu = form.cleaned_data['contenu']
        return redirect(reverse('commentaire', kwargs={"post_id": post_id, "contenu": contenu}))

    post = get_object_or_404(Post, pk=post_id)
    coments = Commentaire.objects.filter(post=post_id).order_by('date_creation')
    return render(request, 'communitymanager/voir_commentaires.html', locals())


@login_required
def commentaire(request, post_id, contenu):
    coment = Commentaire()
    coment.auteur = request.user
    coment.contenu = contenu
    post = get_object_or_404(Post, pk=post_id)
    coment.post = post
    coment.save()
    return redirect('post', post_id=post_id)


@login_required
def nouveau_post(request):
    form = PostForm(request.POST or None, auteur_id=request.user.id)
    form.fields['auteur'].widget = forms.HiddenInput()
    if form.is_valid():
        post = form.save()
        return redirect('post', post_id=post.id)

    return render(request, 'communitymanager/nouveau_post.html', locals())


@login_required
def modif_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, auteur_id=request.user.id, instance=post)
    form.fields['auteur'].widget = forms.HiddenInput()
    if form.is_valid():
        form.save()
        return redirect('post', post_id=post_id)

    return render(request, 'communitymanager/nouveau_post.html', locals())


@login_required
def news_feed(request):
    communautes = request.user.communautes.all()
    posts = Post.objects.all().order_by('-date_creation').filter(communaute__in=communautes)
    return render(request, 'communitymanager/news_feed.html', locals())

@login_required
def nouvelle_communaute(request):
    form = CommunauteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('communautes')

    return render(request, 'communitymanager/nouvelle_communaute.html', locals())


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})