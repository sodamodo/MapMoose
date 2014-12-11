from django.shortcuts import render
from django.views import generic
from django.views.generic import FormView
# from models import Whoser,UploadFileForm
from django.shortcuts import render
from django.http import HttpResponse
from Mapski.forms import Registration
from Mapski import shapefile
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import UploadFileForm, StyleField
import json
from models import Shapefiler, User
from models import UserLeaf
from django.core.urlresolvers import reverse
from jsonify import shapeprocess
import simplejson
from json import loads
# Create your views here.


class MainView(generic.TemplateView):
    """Loads the main page."""
    template_name = 'main.html'


class DataView(generic.TemplateView):
    """Loads the main page."""
    template_name = 'data.html'

    def get_context_data(self, **kwargs):
        context = super(DataView, self).get_context_data(**kwargs)
        context['project_list'] = UserLeaf.objects.all()
        return context


class CreateMap(generic.TemplateView):
    """Loads the create map page."""
    template_name = 'create_map.html'


class UploadView(generic.FormView):
    template_name = "upload.html"
    form_class = UploadFileForm
    success_url = "/data/"

    def form_valid(self, form):
        # user = User.objects.filter(pk=self.request.user.pk)
        newdoc = Shapefiler(user=self.request.user,
                            title=form.cleaned_data['title'],
                            file=self.request.FILES['file'])
        newdoc.save()
        shapeprocess(self.request, newdoc.pk)
        return HttpResponseRedirect(reverse('data'))

# class SaveStyle(generic.FormView):
#     template_name = "style.html"
#     form_class = StyleField
#     success_url = "/data/"
#
#     def get_context_data(self, **kwargs):
#         leaf = UserLeaf.objects.get(pk=style_id)
#         attributes = leaf.attributes
#
#         context = super(SaveStyle, self).get_context_data(**kwargs)
#         context['project_list'] = UserLeaf.objects.all()
#         return context
#
#     def form_valid(self, form):
#         # user = User.objects.filter(pk=self.request.user.pk)
#         newdoc = Shapefiler(user=self.request.user,
#                             title=form.cleaned_data['title'],
#                             file=self.request.FILES['file'])
#         newdoc.save()
#         shapeprocess(self.request, newdoc.pk)
#         return HttpResponseRedirect(reverse('data'))



def base(request):
    return render(request, "base.html")


def registration(request):
    return render(request, "registration.html")


def login(request):
    return render(request, "login.html")


def map(request, map_id):
    data = UserLeaf.objects.get(pk=map_id)

    colorarray = data.fillClr.split(",")
    print(colorarray)

    attribute = data.selectedattr
    weight = data.weight
    jsonvar = data.jsonstr
    opac = data.opac
    color = data.color
    dash = data.dashArray
    fillOpacity = data.fillOpac

    return render_to_response('map.html', {'json': jsonvar, 'colors': simplejson.dumps(colorarray), 'attribute': attribute, 'weight': weight, 'opacity': opac, 'color': color, 'dash': dash, 'fillOpacity': fillOpacity})

# def map(request):
#     return render(request, "map.html")


def style(request, style_id):
    leaf = UserLeaf.objects.get(pk=style_id)
    attributes = leaf.attributes

    return render_to_response("style.html", {'attributes': attributes, 'style_id': style_id})

def save_style(request):
    print(request.POST)
    print(request.GET)
    if 'style_id' in request.GET:
        print("yes")

        style_id = request.GET['style_id']
        print(style_id)

    if 'attributes' in request.GET:
        attributes = request.GET['attributes']

    if 'fillClr' in request.GET:
        fillClr = request.GET['fillClr']

    if 'weight' in request.GET:
        weight = request.GET['weight']

    if 'color' in request.GET:
        color = request.GET['color']

    if 'dashArray' in request.GET:
        dashArray = request.GET['dashArray']

    if 'fillOpacity' in request.GET:
        fillOpacity = request.GET['fillOpacity']


    print(style_id)
    leaf = UserLeaf.objects.get(pk=style_id)
    print(leaf)
    leaf.fillClr = fillClr
    leaf.weight = weight
    leaf.dashArray = dashArray
    leaf.fillOpac = fillOpacity

    leaf.save()
    print(leaf.fillOpac)
    return HttpResponseRedirect(reverse('data'))








def data(request):
    titles = Shapefiler.objects.all().filter(user=request.user)
    return render_to_response("data.html", {'project_list': titles})