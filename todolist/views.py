from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodoList
# view decorators can be used to restrict access to certain views.Django comes with some built-in decorators eg. login_required,require_POST
from django.views.decorators.http import require_POST


# Create your views here.

def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoList()
    context = {'todo_items': todo_items,'form': form}
    return render(request, 'todolist/index.html', context)


@require_POST
def addTodoItem(request):
    print("Request POST data:", request.POST)  # Debugging: Print the POST data
    form = TodoList(request.POST)
    if form.is_valid():
        print("Form is valid")  # Debugging: Confirm form validation
        new_todo = Todolist(text=form.cleaned_data['text'])
        new_todo.save()
        print("New todo saved:", new_todo)  # Debugging: Confirm saving
    else:
        print("Form errors:", form.errors)  # Debugging: Display form errors
    return redirect('index')


def completedTodo(request,todo_id):
    todo=Todolist.objects.get(pk=todo_id)
    todo.completed=True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todolist.objects.filter(completed=True).delete()
    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')