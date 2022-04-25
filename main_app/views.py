from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Movie, Comment



class MovieListView(ListView):
    model = Movie
    paginate_by = 100  # if pagination is desired
    template_name = 'movi_templates/index.html'

    def get_context_data(self, **kwargs):
        statusRA = Movie.objects.filter(status='RA')
        statusMW = Movie.objects.filter(status='MW')
        statusTR = Movie.objects.filter(status='TR')
        contexts = {
            'statusRA': statusRA,
            'statusMW': statusMW,
            'statusTR': statusTR,

        }
        return contexts


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movi_templates/movie-details.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse('detail_list', kwargs={
                'pk': post.pk,
            }))
            # return render(request,'movie_detail.html')