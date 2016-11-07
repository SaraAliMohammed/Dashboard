from builtins import print
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from .models import Server,Mac,Rac
import json
from django.core import serializers
from django.http import HttpResponse
from django import forms

def dataCenterView(request):
    context={}
    context['servers']=Server.objects.all()
    context['macs']=Mac.objects.all()
    context['type']=type(Server.objects.name) is str
    return render_to_response('dataCenter.html',context)



def servers_view(request):
    serverData = {}
    serverData['servers'] = serializers.serialize("json", Server.objects.all())
    serverData['macs'] = serializers.serialize("json",Mac.objects.all())

    '''test = [{
        "name": "win",
        "Type": "A",
        "RAM": "test",
        "Core": "3",
        "Storage": "200.00",
    }];'''

    servers=[]
    for server in Server.objects.all():
        obj={"name":server.name,"Type":server.Type,"RAM":server.RAM,"Core":server.Core,"Storage":server.Storage}
        servers.append(obj)
    serverData['test']=servers
    '''serverData['s'] ="s"'''
    data = json.dumps(serverData)

    return HttpResponse(data, content_type='application/json')



from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db import IntegrityError

class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['name','Type','RAM','Core','Storage','RackNum']


def ServerListView(request, template_name='ServerList.html'):
    servers = Server.objects.all()
    data = {}
    data['object_list'] = servers
    '''form = RacServers(request.POST or None)
        if form.is_valid():
            data['RackNum'] = form.cleaned_data.get('RackNum')'''
    return render(request, template_name, data)

def ServerCreateView(request, template_name='ServerForm.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

def ServerUpdateView(request, pk, template_name='ServerForm.html'):
    server = get_object_or_404(Server, pk=pk)
    form = ServerForm(request.POST or None, instance=server)

    if request.method == 'POST' and request.is_ajax:
        if form.is_valid():
            serverName = form.cleaned_data.get('name')
            try:
                Server.objects.filter(name=pk).update(name=serverName)
                Mac.objects.filter(ServerID=pk).update(ServerID=serverName)
                form.save()
                msg = 'server edited successfully'
            # if try to write name aleady exists
            except IntegrityError:
                form.save(commit=False)
                msg='This name is already exists'
            return HttpResponse(msg)
        else:
            msg = 'error'

        return HttpResponse(msg)

    else:
        if form.is_valid():
            serverName = form.cleaned_data.get('name')
            try:
                Server.objects.filter(name=pk).update(name=serverName)
                Mac.objects.filter(ServerID=pk).update(ServerID=serverName)
                form.save()

            #if try to write name aleady exists
            except IntegrityError:
                form.save(commit=False)

            return redirect('server_list')
        return render(request, template_name, {'form':form})

'''def ServerDeleteView(request, pk, template_name='ServerConfirmDelete.html'):
    server = get_object_or_404(Server, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':server})'''

def ServerDeleteView(request, pk):
    server = get_object_or_404(Server, pk=pk)
    msg = 'not deleted'
    if request.method=='POST':
        server.delete()
        msg = 'deleted successfully'
    return HttpResponse(msg)



#------------------Mac----------------------------------
class MacForm(ModelForm):
    class Meta:
        model = Mac
        fields = ['ServerID','MacNum']

def MacListView(request, template_name='MacList.html'):
    macs = Mac.objects.all()
    data={}
    data['object_list'] = macs
    return render(request,template_name, data )

def AddMacToServerView(request, template_name='ServerForm.html'):
    form = MacForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mac_list')
    return render(request, template_name, {'form':form})

def UpdateMacView(request,pk,template_name='ServerForm.html'):
    mac = get_object_or_404(Mac,pk=pk)
    form = MacForm(request.POST or None, instance=mac)
    if form.is_valid():
        macNum = form.cleaned_data.get('MacNum')
        Mac.objects.filter(pk=pk).update(MacNum=macNum)
        form.save()
        return redirect('mac_list')
    return render(request, template_name, {'form' : form})

def ShowServerMacsView(request, pk, template_name='MacList.html'):
    serverMacs = Mac.objects.filter(ServerID=pk).all()
    return render(request, template_name, {'object_list':serverMacs})

def ShowRacServersView(request, template_name='RacServers.html'):
    rac1Servers = Server.objects.filter(RackNum=1)
    rac2Servers = Server.objects.filter(RackNum=2)
    rac3Servers = Server.objects.filter(RackNum=3)
    rac4Servers = Server.objects.filter(RackNum=4)
    rac5Servers = Server.objects.filter(RackNum=5)
    rac6Servers = Server.objects.filter(RackNum=6)

    context = {
        'rac1Servers' : rac1Servers,
        'rac2Servers' :rac2Servers,
        'rac3Servers': rac3Servers,
        'rac4Servers': rac4Servers,
        'rac5Servers': rac5Servers,
        'rac6Servers': rac6Servers,
    }
    return render(request, template_name, context)

#----------------- index ------------------------------
def oldIndexView(request):
    racsObjects=Rac.objects.all()
    racsNumbers=[]
    racServers = []
    MacNumbers=Mac.objects.all()
    for rac in racsObjects:
        racServers.append(Server.objects.filter(RackNum=rac.RackNum))
        racsNumbers.append(rac.RackNum)

    racsNumbers.sort()

    context = {
        'RacsNum': racsNumbers,
        'racs':racServers,
        'MacNumbers':MacNumbers
    }
    return render(request, 'oldIndex.html',context)

def indexView(request):
    racsObjects=Rac.objects.all()
    racsNumbers=[]
    racServers = []
    MacNumbers=Mac.objects.all()
    for rac in racsObjects:
        racServers.append(Server.objects.filter(RackNum=rac.RackNum))
        racsNumbers.append(rac.RackNum)

    racsNumbers.sort()

    Servers = Server.objects.all()
    serversCount = len(Servers)
    editServerForm=ServerForm(request.POST or None)
    context = {
        'RacsNum' : racsNumbers,
        'racs' : racServers,
        'MacNumbers' : MacNumbers,
        'serversCount' : serversCount,
        'Servers' : Servers,
        'editServerForm':editServerForm
    }
    return render(request, 'index.html',context)

from django.template.loader import render_to_string

def test(request, template_name='ServerForm.html'):
    html=''
    test='f'
    if (request.is_ajax()):
        id=request.POST.get('id')
        server = get_object_or_404(Server, pk=id)
        form = ServerForm(request.POST or None, instance=server)
        if form.is_valid():
            serverName = form.cleaned_data.get('name')
            try:
                Server.objects.filter(name=id).update(name=serverName)
                Mac.objects.filter(ServerID=id).update(ServerID=serverName)
                form.save()
            # if try to write name aleady exists
            except IntegrityError:
                form.save(commit=False)
            return redirect('server_list')
        html = render_to_string(template_name, {'id':id,'server':server,'form':form,'test':test})
    else:
        html = render_to_string('ServerList.html', {'id':id})
    return HttpResponse(html)




