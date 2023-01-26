from ..models import Content
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse
import random

# 게시글 삭제
@login_required(login_url='common:login')
def content_delete(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    content.delete()

    return redirect('SCC:index')

# 게시글 만들기, 파일 업로드
@login_required(login_url = 'common:login')
def content_create(request):
    if request.method == 'POST':
        form = Content()
        file = request.FILES['file']
        form.title = file
        form.create_date = timezone.now()
        form.author = request.user
        form.file = file
        form.save()

        return redirect('SCC:index')

    return render(request, 'SCC/content_form.html')

# 파일 다운로드
def file_download(request):
    path = request.GET['path']
    file_path = os.path.join(settings.MEDIA_ROOT, path)
 
    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        message = '알 수 없는 오류가 발행하였습니다.'
        return HttpResponse("<script>alert('"+ message +"');history.back()'</script>")