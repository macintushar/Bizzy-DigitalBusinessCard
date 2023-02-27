from supabase import create_client, Client

url = "https://zsvuwwnqsfbbojhygbpo.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpzdnV3d25xc2ZiYm9qaHlnYnBvIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzQ2Njk0NTcsImV4cCI6MTk5MDI0NTQ1N30.6P50k058UQdd91I7gLcPbA1Qa6JeMAUXr5KBozJzZyY"
supabase: Client = create_client(url, key)


class SupabaseFunctions:
    def GetCardData(username):
        response = supabase.table('cards').select("*").eq('username','tushar').execute()
        return response



