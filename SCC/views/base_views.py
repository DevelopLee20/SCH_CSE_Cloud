from ..models import Content
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# 메인 화면
@login_required(login_url = 'common:login')
def index(request):
    content_list = Content.objects.order_by('-create_date')
    page = request.GET.get('page', '1')
    content_list = content_list.filter(Q(author__username__icontains = request.user)).distinct()
    paginator = Paginator(content_list, 10)
    page_obj = paginator.get_page(page)
    context = {'content_list':page_obj, 'page':page, 'kw':request.user}

    return render(request, 'SCC/content_list.html', context)