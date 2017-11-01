from django.shortcuts import render
from .models import Dictionary

# Create your views here.
def word(request):

    if request.method == 'POST':
        iteration_number = int(request.POST.get('iteration_number')) + 1
        if iteration_number >= 10:
            return render(request, 'source/rest.html', {} )
        original_word = Dictionary.objects.get(id=request.POST.get('original_word'))
        next_word = Dictionary.objects.all()[int(request.POST.get('iteration_number'))]
        if original_word.translate_word == request.POST.get('translation'):
            result = True
        else:
            result = False
        return render(request, 'source/post.html', {
            'iteration_number': iteration_number,
            'previous_word': original_word,
            'result': result,
            'next_word': next_word,
        } )

    return render(request, 'source/get.html', {
        'next_word': Dictionary.objects.first()

    } )
