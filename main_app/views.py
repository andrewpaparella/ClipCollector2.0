from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Clip
from .forms import CommentForm

class ClipCreate(CreateView):
  model = Clip
  fields = '__all__'

class ClipUpdate(UpdateView):
  model = Clip
  fields = ['description']

class ClipDelete(DeleteView):
  model = Clip
  success_url = '/clips/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def clips_index(request):
  clips = Clip.objects.all()
  return render(request, 'clips/index.html', { 'clips': clips })

def clips_detail(request, clip_id):
  clip = Clip.objects.get(id=clip_id)
#   toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
#   # instantiate FeedingForm to be rendered in the template
  comment_form = CommentForm()
  return render(request, 'clips/detail.html', {
#     # pass the cat and feeding_form as context
    'clip': clip, 
    'comment_form': comment_form,
#     'toys' : toys_cat_doesnt_have
  })

def add_comment(request, clip_id):
	# create the ModelForm using the data in request.POST
  form = CommentForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the clip_id assigned
    new_comment = form.save(commit=False)
    new_comment.clip_id = clip_id
    new_comment.save()
  return redirect('detail', clip_id=clip_id)

# class ToyList(ListView):
#   model = Toy

# class ToyDetail(DetailView):
#   model = Toy

# class ToyCreate(CreateView):
#   model = Toy
#   fields = '__all__'

# class ToyUpdate(UpdateView):
#   model = Toy
#   fields = ['name', 'color']

# class ToyDelete(DeleteView):
#   model = Toy
#   success_url = '/toys/'

# def assoc_toy(request, cat_id, toy_id):
#   Cat.objects.get(id=cat_id).toys.add(toy_id)
#   return redirect('detail', cat_id=cat_id)