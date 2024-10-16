from os import environ

from supabase import create_client

SUPABASE_URL = environ.get('SUPABASE_URL')
SUPABASE_KEY = environ.get('SUPABASE_KEY')
SUPABASE_SERVICE_ROLE_KEY = environ.get('SUPABASE_SERVICE_ROLE_KEY')
supabase = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY)
supabase_admin = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_SERVICE_ROLE_KEY)


def get_clients():
    try:
        response = (
            supabase.table('profiles')
            .select('*, accounts(balance)')
            .eq('profiles.type', 'client')
            .execute()
        )
        if response and response.data:
            print(response.data)
            return response.data
    except Exception as e:
        print(f'Error fetching clients: {e}')
