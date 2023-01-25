from ..models import Content
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ContentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 게시글 수정
@login_required(login_url = 'common:login')
def content_modify(request, content_id):
    content = get_object_or_404(Content, pk=content_id)

    if request.method == "POST":
        form = ContentForm(request.POST, instance=content)

        if form.is_valid():
            content = form.save(commit=False)
            content.author = request.user
            content.modify_date = timezone.now()
            content.save()
            return redirect('test_cloud:detail', content_id=content.id)

    else:
        form = ContentForm(instance=content)

    context = {'content': content, 'form': form}

    return render(request, 'test_cloud/content_form.html', context)

# 게시글 삭제
@login_required(login_url='common:login')
def content_delete(request, content_id):
    content = get_object_or_404(Content, pk=content_id)

    if request.user != content.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('test_cloud:detail', content_id=content.id)

    content.delete()

    return redirect('test_cloud:index')

# 게시글 만들기
@login_required(login_url = 'common:login')
def content_create(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        
        if form.is_valid():
            content = form.save(commit=False)
            content.create_date = timezone.now()
            content.author = request.user
            content.save()

            return redirect('test_cloud:index')
        
    else:
        form = ContentForm()
    
    context = {'form':form}

    return render(request, 'test_cloud/content_form.html', context)