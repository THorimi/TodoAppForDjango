from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
import datetime
from datetime import date


from django.contrib.auth.models import User


from .models import TodoModel
from .forms import TodoModelForm
from django.urls import reverse_lazy

today = datetime.datetime.today().date()

# Create your views here.
# indexページ
@login_required
def index_view(request):
    object_list = TodoModel.objects.filter(user__id=request.user.id, complete=False)
    for item in object_list:
        item.remaining_days = (item.duedate - date.today()).days
    return render(request, 'todo/index.html', {'object_list': object_list, 'title': "TOPページ"})

# 完了済みページ
@login_required
def complete_view(request):
    object_list = TodoModel.objects.filter(user__id=request.user.id, complete=True)
    return render(request, 'todo/complete.html', {'object_list': object_list, 'title': "完了済みタスク一覧"})

# ToDoの作成機能    
@login_required
def create_todo(request):
    if request.method == 'POST':
        form = TodoModelForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user_id = request.user.id  # ログインユーザーのIDを取得して設定
            todo.save()
            return redirect('index')
    else:
        form = TodoModelForm()
    return render(request, 'todo/create.html', {'form': form})

# ToDoの削除機能
class TodoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'todo/delete.html'
    model = TodoModel
    success_url = reverse_lazy('index')

    def get_object(self, queryset= None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "タスクの削除"
        return context

# ToDoの編集機能
class TodoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'todo/update.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate')
    success_url = reverse_lazy('index')

    def get_object(self, queryset= None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "タスクの編集"
        return context

# タスク完了状態をトグルする
@login_required
def complete_task(request, pk):
    task = get_object_or_404(TodoModel, pk=pk)
    task.complete = not task.complete
    task.save()
    if task.complete:
        return redirect('index')
    else:
        return redirect('complete')