from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse('''
  <h1>
    Navigat to:
  </h1>
  <ul>
    <li>
      <a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-0/" target="_blank">www.codewithharry.com</a>:-  Python-Django tutorials (Hindi)
    </li>
    <br>
    <li>
      <a href="http://127.0.0.1:8000/app1/analyzingtext/" target="_blank">Text Analyzer</a>:- My mini project using Python, Django, HTML 
    </li>
  </ul>              
                      ''')


def analyzingtext(request):
  return render(request,"analyzingtext.html")
  

def analyzedtext(request):
  text=request.POST.get('textarea','Default') 

  removepunc=request.POST.get('removepunc','off') 
  removespace=request.POST.get('removespace','off') 
  removeextraspace=request.POST.get('removeextraspace','off')  
  removeline=request.POST.get('removeline','off') 
  removedigit=request.POST.get('removedigit','off')  
  removealpha=request.POST.get('removealpha','off')  
  uppercase=request.POST.get('upper','off') 
  lowercase=request.POST.get('lower','off')  
  countchar=request.POST.get('countchar','off')

  newtext=''
  purpose = []

  if removepunc=='on':
    purpose.append('Remove punctuations')
    text=removepunctuation(text,newtext)

  if removespace=='on':
    purpose.append('Remove spaces')
    text=removespaces(text,newtext)

  if removeextraspace=='on':
    purpose.append('Remove extra spaces')
    text=removeextraspaces(text)

  if removeline=='on':
    purpose.append('Remove new lines')
    text=removenewlines(text,newtext)

  if removedigit=='on':
    purpose.append('Remove digits')
    text=removedigits(text,newtext)

  if removealpha=='on':
    purpose.append('Remove alphabets')
    text=removealphabets(text,newtext)

  if uppercase=='on':
    purpose.append('Convert to uppercase')
    text=text.upper()

  if lowercase=='on':
    purpose.append('Convert to lowercase')
    text=text.lower()

  if countchar=='on':
    purpose.append('Count no. of characters')
    text=countchars(text)

  if removepunc == removespace == removeextraspace == removeline == removedigit == removealpha == uppercase == lowercase == countchar == 'off':
    purpose=['No utility selected']
    if text == '':
      text='No text entered for analysis'
    text=text

  if text == '':
    text='No text entered for analysis'


  d={ "inputpurpose":purpose, "inputtext":text}
  return render(request,"analyzedtext.html", context=d)


def removepunctuation(text,newtext):
  for ch in text:
    if ch not in '.,;:!-?(})[]{@#$%^*+=|\/~`""': 
        newtext += ch
  return newtext

def removespaces(text,newtext):
  for ch in text:
    if ch != ' ': 
        newtext += ch
  return newtext
  
def removeextraspaces(text):
  return ' '.join(text.split())

def removenewlines(text,newtext):
  for ch in text:
    if ch != '\n' and ch !='\r': 
        newtext += ch
  return newtext

def removedigits(text,newtext):
  for ch in text:
    if ch not in '01234567890': 
        newtext += ch
  return newtext

def removealphabets(text,newtext):
  li = [chr(val) for val in range(65,91)]+[chr(val) for val in range(97,123)]
  for ch in text: 
    if ch not in li: 
        newtext += ch
  return newtext

def countchars(text):
  count=0
  for ch in text:
    if ch != '\n' and ch !='\r': 
        count += 1
  return count
