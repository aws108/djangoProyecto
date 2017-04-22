from django.shortcuts import render

from .models import Categoria


def index(request):
	#Quiero mostrar los ultimos 5 productos por fecha de publicacion
	ultima_publicacion = Categoria.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('ecologic/index.html')
	#output = ', '.join([p.nombre for q in ultima_publicacion])
	context = {'ultima_publicacion': ultima_publicacion}
	return render(request, 'ecologic/index.html', context)




    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    


"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))"""