from django.shortcuts import render, get_object_or_404
from .models import Password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
import pdb

# аналог passw_list
class PasswListView(ListView):
    queryset = Password.objects.all()
    context_object_name = 'passws'
    template_name = 'pass/htmls/list.html'

    def get(self, request):
        page = self.request.GET.get('page', 1)
        per_page = self.request.GET.get('per_page', 1)
        paginator = Paginator(self.queryset, per_page)
        try:
            passws = paginator.page(page)
        except EmptyPage:
            # If page is out of range deliver last page of results
            passws = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'passws': passws})



def passw_list(request):
    passws = Password.objects.all()

    page = request.GET.get('page') or 1
    per_page = request.GET.get('per_page') or 1
    paginator = Paginator(passws, per_page)
    try:
        passws = paginator.page(page)
    except EmptyPage:
        # If page is out of range deliver last page of results
        passws = paginator.page(paginator.num_pages)

    return render(request, 'pass/htmls/list.html', {'page': page,'passws': passws})


def passw_detail(request, id):
    passw = get_object_or_404(Password, id=id)
    return render(request,'pass/htmls/detail.html', {'passw': passw})


