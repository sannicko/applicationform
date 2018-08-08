from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse

from jsignature.utils import draw_signature

from django.template import Context
from django.template.loader import get_template
from io import BytesIO
import cStringIO as StringIO
from xhtml2pdf import pisa
from cgi import escape
from django.core.files.base import ContentFile

from django.core.mail import EmailMessage

from django.db.models import Q
from .forms import *
from .models import *
# from .decorators import redirect_to_home

from account.views import *
from django.views.generic import View, TemplateView,FormView
from datetime import datetime
import os


def form_submit(request):
    print '>>>In form submit function <<<'
    form = UserForm(data=request.POST,files=request.FILES or None)
    if form.is_valid():
        print '>>>cleaned data is : ',form.cleaned_data
        print 'ceiling mechanic value is : ',form.cleaned_data['ceiling_mechanic']
        print 'framing_mechanic value is : ',form.cleaned_data['framing_mechanic']
        print 'drywall_hanger value is : ',form.cleaned_data['drywall_hanger']
        print '>>>brick layer value is : ',form.cleaned_data['masonry_bricklayer']
        print '>>>martial status is : ',form.cleaned_data['Martial_status']
        print 'state is : ',form.cleaned_data['state']
        print 'date of birth is : ',form.cleaned_data['is_osha10']
        print 'uploaded resume copy is : ',form.cleaned_data['is_osha30']
        fm = form.save(commit=False)
        sig = form.cleaned_data['user_signature']
        if sig:
            sig_file = draw_signature(sig)
            image_io = BytesIO()
            sig_file.save(image_io, format='PNG', quality=80)
            fm.signature = ContentFile(image_io.getvalue(), str(request.user.id)+'_signature.png')
        fm.save()
        id = fm.id
        print '>>>after saving the form/user <<<'
        return generate(request, id)
    else:
        print '>>>in else part <<<'
        print form.errors
        print form.cleaned_data['agreement_signed_date']
    return render(request, 'employee/form.html')
    return render(request, 'employee/form.html')


class UserHome(TemplateView):
    def get(self, request, *args, **kwargs):
        employeeForm = UserForm(request.POST or None)
        date = datetime.today().strftime('%Y-%m-%d')
        # print '>>>logged in user is : ',self.request.user.email
        return render(request, 'employee/form.html', {'employeeForm':employeeForm, 'date':date})



class UserProfile(TemplateView):
    template_name='profile.html'
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('userId', None)
        print '>>>now id is : ',user_id
        getUser = Friend.objects.get(id=user_id)
        print '>>usr is : ',getUser
        return render(request, 'profile.html', {'userObject':getUser})


def render_to_pdf(path, dict, request):
    template = get_template(path)
    html = template.render(dict)
    file_name = 'media/temp_pdf/' + str(dict['id']) + "form.pdf"
    response = open(file_name, 'wb')
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response, link_callback=fetch_resuources)
    if not pdf.err:
        response.close()
        """
        email = EmailMessage(
            'Subject here', 'Here is the message.', 'from@me.com', ['email@to.com'])
        email.attach_file(file_name)
        email.send()
        """
        return render(request, 'employee/success.html', locals())
    else:
        return HttpResponse("Error Rendering PDF", status=400)

def fetch_resuources(url, rel):
    path = os.path.join(settings.MEDIA_ROOT, url.replace(settings.MEDIA_URL, ""))
    return path

def generate(request, id):
    user = ApplicationForm.objects.get(id=id)
    return render_to_pdf('pdf_form.html', {'pagesize': 'A4', 'mylist': user, 'id':id}, request)