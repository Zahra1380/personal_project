from django.shortcuts import render
from about_app.models import About, library, Experience, Education, Contact_me, Recieve_massage

def home(request):
   detail = About.objects.all().last()
   m =detail.ability.split("_")
   lib = library.objects.all()
   ex = Experience.objects.all()[::-1]
   ed = Education.objects.all()[::-1]
   con = Contact_me.objects.all().last()
   if request.method == 'POST':
      n = request.POST.get('name')
      e = request.POST.get('email')
      mm = request.POST.get('message')
      Recieve_massage.objects.create(name= n, email=e, massage= mm)

   return render(request, 'index.html', {'detail': detail, 'ability': m, 'lib': lib, 'ex': ex, 'ed': ed, 'con': con})
