from todo.models import *
from django.shortcuts import *
from django.template import *


# Create your views here.

def list(request):
	todo_list = ToDo.objects.all()
	return render_to_response ('todo/list.html' , {'todolist' : todo_list })


# def createTodo(request):
# 	return render_to_response('todo/createTodo.html' , {'action' : 'AddTodo' , 'button' : 'Add'})

# def AddTodo(request):
# 	Title = request.POST ('Title')
# 	Description = request.POST ('Description')
# 	Duration = request.POST('Duration')
# 	Venue = request . POST ('Venue')

# 	todo = ToDo (

# 			Title = Title
# 			Description = Description
# 			Duration = Duration
# 			Venue = Venue

# 		)

# 	todo.save()
# 	return render_to_response('request', { message = 'item added!'})
