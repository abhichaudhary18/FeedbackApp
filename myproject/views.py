from django.views.generic import TemplateView

class homepage(TemplateView):
    template_name = 'index.html'

class aboutpage(TemplateView):
    template_name= 'about.html'

class contactpage(TemplateView):
    template_name = 'contact.html'


class testpage(TemplateView):
    template_name = 'test.html'

class thankspage(TemplateView):
    template_name = 'index.html'

class settingspage(TemplateView):
    template_name = 'settings.html'

class Terms(TemplateView):
    template_name = 'terms.html'
