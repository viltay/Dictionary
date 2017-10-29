from django.shortcuts import render
from .models import Dictionary

# Create your views here.
def word(request):

    if request.method == 'POST':
        iteration_number = int(request.POST.get('iteration_number')) + 1
        if iteration_number >= 10:
            return render(request, 'source/rest.html', {} )
        return render(request, 'source/post.html', {'iteration_number': iteration_number} )
    return render(request, 'source/get.html', {} )
