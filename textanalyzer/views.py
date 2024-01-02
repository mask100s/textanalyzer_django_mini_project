from django.shortcuts import render
from django.http import HttpResponse



#----------------------single selection---------------------------#

# def home(request):
#   return HttpResponse('''
#   <h1>
#     Navigat to:
#   </h1>
#   <ul>
#     <li>
#       <a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-0/" target="_blank">www.codewithharry.com</a>:-  Python django tutorials hindi
#     </li>
#     <li>
#       <a href="http://127.0.0.1:8000/analyzingtext/" target="_blank">analyzingtext</a>
#     </li>
#   </ul>              
#                       ''')

# def analyzingtext(request):
#   return render(request,"analyzingtext.html")
  

# def analyzedtext(request):
#   text=request.GET.get('textarea','default') 
#   removepunc=request.GET.get('removepunc') 
#   removespace=request.GET.get('removespace')  
#   removeline=request.GET.get('removeline')  
#   uppercase=request.GET.get('upper') 
#   lowercase=request.GET.get('lower')  
#   countchar=request.GET.get('countchar')

#   newtext=''
#   purpose = ''

#   if removepunc=='on':
#     purpose='Remove punctuation'
#     newtext=removepunctuation(text,newtext)
#   elif removespace=='on':
#     purpose='Remove spaces'
#     newtext=removespaces(text,newtext)
#   elif removeline=='on':
#     purpose='Remove new lines'
#     newtext=removenewlines(text,newtext)
#   elif uppercase=='on':
#     purpose='Convert to uppercase'
#     newtext=text.upper()
#   elif lowercase=='on':
#     purpose='Convert to lowercase'
#     newtext=text.lower()
#   elif countchar=='on':
#     purpose='count no. of characters'
#     newtext=countchars(text)
#   else:
#     purpose='None'
#     newtext=text

#   d={"inputpurpose":purpose, "inputtext":newtext}
#   return render(request,"analyzedtext.html", context=d)


# def removepunctuation(text,newtext):
#   for ch in text:
#     if ch not in '.,;:!-?()""': 
#         newtext += ch
#   return newtext

# def removespaces(text,newtext):
#   for ch in text:
#     if ch != ' ': 
#         newtext += ch
#   return newtext

# def removenewlines(text,newtext):
#   for ch in text:
#     if ch != '\n': 
#         newtext += ch
#   return newtext

# def countchars(text):
#   count=0
#   for ch in text:
#     if ch != '\n': 
#         count += 1
#   return count






#------------------multipule selection-----------------------#

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
      <a href="http://127.0.0.1:8000/analyzingtext/" target="_blank">Text Analyzer</a>:- My mini project using Python, Django, HTML 
    </li>
  </ul>              
                      ''')

def analyzingtext(request):
  return render(request,"analyzingtext.html")
  

def analyzedtext(request):
  text=request.GET.get('textarea') 
  print(text)

  removepunc=request.GET.get('removepunc') 
  removespace=request.GET.get('removespace')  
  removeline=request.GET.get('removeline')  
  uppercase=request.GET.get('upper') 
  lowercase=request.GET.get('lower')  
  countchar=request.GET.get('countchar')

  newtext=''
  purpose = []

  if removepunc=='on':
    purpose.append('Remove punctuations')
    text=removepunctuation(text,newtext)
  if removespace=='on':
    purpose.append('Remove spaces')
    text=removespaces(text,newtext)
  if removeline=='on':
    purpose.append('Remove new lines')
    text=removenewlines(text,newtext)
  if uppercase=='on':
    purpose.append('Convert to uppercase')
    text=text.upper()
  if lowercase=='on':
    purpose.append('Convert to lowercase')
    text=text.lower()
  if countchar=='on':
    purpose.append('Count no. of characters')
    text=countchars(text)
  if removepunc == removespace == removeline == uppercase == lowercase == countchar == 'off':
    purpose=['None']
    text=text


  d={ "inputpurpose":purpose, "inputtext":text}
  return render(request,"analyzedtext.html", context=d)


def removepunctuation(text,newtext):
  for ch in text:
    if ch not in '.,;:!-?()""': 
        newtext += ch
  return newtext

def removespaces(text,newtext):
  for ch in text:
    if ch != ' ': 
        newtext += ch
  return newtext

def removenewlines(text,newtext):
  for ch in text:
    if ch != '\n': 
        newtext += ch
  return newtext

def countchars(text):
  count=0
  for ch in text:
    if ch != '\n': 
        count += 1
  return count
