from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from supabase import create_client, Client

url = "https://zsvuwwnqsfbbojhygbpo.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpzdnV3d25xc2ZiYm9qaHlnYnBvIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzQ2Njk0NTcsImV4cCI6MTk5MDI0NTQ1N30.6P50k058UQdd91I7gLcPbA1Qa6JeMAUXr5KBozJzZyY"
supabase: Client = create_client(url, key)



def GetCardData(username):
    response = supabase.table('cards').select("*").eq('username','tushar').execute()
    response = response.data[0]
    print(response['first_name'])
    return response
def index(request):
    card = GetCardData('tushar')
    context = {'card': card}
    return render(request, 'BizzyCardApp/index.html', context)

def login(request):
    return render(request,'BizzyCardApp/login.html')