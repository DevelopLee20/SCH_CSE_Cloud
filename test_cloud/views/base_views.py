from ..models import Content
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def index_filter(request):
    content_list = Content.objects.order_by('-create_date')
    page = request.GET.get('page', '1')

    # 검색 필터링
    kw = request.GET.get('kw','') # 검색어
    if kw:
        content_list = content_list.filter(
            Q(title__icontains=kw) |
            Q(summary__icontains=kw) |
            Q(author__username__icontains=kw)
        ).distinct()
    paginator = Paginator(content_list, 10)
    page_obj = paginator.get_page(page)
    context = {'content_list':page_obj, 'page':page, 'kw':kw}

    return context

# 메인 화면
@login_required(login_url = 'common:login')
def index(request):
    page_obj, page, kw = index_filter(request)
    context = index_filter(request)
    return render(request, 'test_cloud/content_list.html', context)

# 게시글 클릭시 화면
@login_required(login_url = 'common:login')
def detail(request, content_id):
    content = get_object_or_404(Content, pk=content_id)

    if request.user != content.author:
        messages.error(request, '권한이 없습니다.') # 작동하지 않음
        page_obj, page, kw = index_filter(request)
        context = index_filter(request)
        context['error_check'] = 1

        return render(request, 'test_cloud/content_list.html', context)

    context = {'content':content}

    return render(request, 'test_cloud/content_detail.html', context)