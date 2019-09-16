from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Artical
from django.core.paginator import Paginator
def hello_world(request):
    return HttpResponse("Hello World")

def boyang(request):
    return HttpResponse("boyang is Handsome")

def artical_content(request):
    artical = Artical.objects.all()[0]
    title = artical.title
    brief_content = artical.brief_content
    content = artical.content
    artical_id = artical.article_id
    publish_date = artical.publish_date
    return_str = 'title: %s, brief_content: %s, content: %s, artical_id: %s, ' \
                 'publish_date: %s' %(title, brief_content,
                                      content, artical_id, publish_date)
    return HttpResponse(return_str)



def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print('page param: ', page)
    all_artical = Artical.objects.all()
    paginator = Paginator(all_artical, 3)
    print('page num: ', paginator.num_pages)
    page_artical_list = paginator.page(page)
    page_num = paginator.num_pages
    top5_artical_list = Artical.objects.order_by('-publish_date')[:5]
    if page_artical_list.has_next():
        next_page = page+1
    else:
        next_page = page
    if page_artical_list.has_previous():
        previous_page = page-1
    else:
        previous_page = page

    return render(request, 'blog/index.html',
                  {
                  'artical_list': page_artical_list,
                  'page_num':range(1, page_num+1),
                  'curr_page':page,
                  'next_page':next_page,
                  'previous_page':previous_page,
                  'top5_artical_list':top5_artical_list,
                  })

def get_detail_page(request, artical_id):
    all_artical = Artical.objects.all()
    curr_artical = None
    previous_index = 0
    next_index = 0
    previous_artical = None
    next_artical = None
    for index, artical in enumerate(all_artical):
        if index == 0:
            previous_index = 0
            next_index = index+1
        elif index == len(all_artical)-1:
            previous_index = index-1
            next_index = index
        else:
            previous_index = index-1
            next_index = index+1
        if artical.article_id == artical_id:
            curr_artical = artical
            previous_artical = all_artical[previous_index]
            next_artical = all_artical[next_index]
            break

    section_list = curr_artical.content.split('\n')
    return render(request, 'blog/detail.html',
                  {
                  'curr_artical': curr_artical,
                  'section_list': section_list,
                  'previous_artical': previous_artical,
                  'next_artical':next_artical,
                  })



def test(request):
    return HttpResponse("Test")
