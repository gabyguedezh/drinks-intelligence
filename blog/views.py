from django.shortcuts import redirect, render
from django.views import generic

from .models import BlogPost


####################################################################################
#       Define class based view for Articles page, both POST and GET requests      #
####################################################################################

class BlogPostView(generic.DetailView):
    template_name = 'blog/blog.html'

    def get(self, request):
        posts = BlogPost.objects.all()
        return render(request, self.template_name, {'posts': posts})