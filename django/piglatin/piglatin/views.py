from django.http import HttpResponse
from django.shortcuts import render # to render html

def home(request):
  return render(request, 'home.html')

def translate(request):
  original_text = request.GET['original_text'].lower()

  translation = ''
  for word in original_text.split():
    if word[0] in ['a', 'e', 'i', 'o', 'u']:
      # vowel
      translation += word 
      translation += 'way '
    else:
      # consonant
      suffix = word[0] + 'ay '
      translation += word[1:]
      translation += suffix


  return render(request, 'translate.html', {
    'original': original_text,
    'translation': translation
  })

def about(request):
  return render(request, 'about.html')
