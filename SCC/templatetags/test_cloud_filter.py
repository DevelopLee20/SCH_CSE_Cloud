from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

# 게시글 작성에 마크다운 적용 가능하게 변경
@register.filter()
def mark(value):
    extensions = ["nl2br","fenced_code"]

    return mark_safe(markdown.markdown(value, extensions=extensions))