# This program contains a set of functions to interract with providers API
# Hosted at: (PythonAnyhwere CHECK IF HOSTING LOCATION CHANGED)
# Author: Oksana Abrosimova


from urllib import response

import requests
import json

#UPDATE URL later
# url = "https://yourname.pythonanywhere.com/providers"
providers_url = "http://127.0.0.1:5000/providers"
services_url = "http://127.0.0.1:5000/services"

# PROVIDERS

def get_providers():
    response = requests.get(providers_url)
    if response.ok:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}

def provider_by_id(provider_id):
    url_id = providers_url+ "/" + str(provider_id)
    response = requests.get(url_id)
    if response.ok:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}
    

def create_provider(new_provider):
    response = requests.post(providers_url, json=new_provider)
    if response.ok:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}

def update_provider(provider_id, provider_diff):
    update_url = providers_url + "/" +str(provider_id)
    response = requests.put(update_url, json=provider_diff)
    if response.ok:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}

def delete_provider(provider_id):
    delete_url = providers_url + "/" + str(provider_id)
    response = requests.delete(delete_url)
    if response.ok:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}

# SERVICES

def get_services():
    response = requests.get(services_url)
    if response.ok:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}

def create_service(new_service):
    response = requests.post(services_url, json=new_service)
    if response.ok:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}

def update_service(service_id, service_diff):
    update_url = services_url + "/" +str(service_id)
    response = requests.put(update_url, json=service_diff)
    if response.ok:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}

def delete_service(service_id):
    delete_url = services_url + "/" + str(service_id)
    response = requests.delete(delete_url)
    if response.ok:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}

# TEST
if __name__ == "__main__":
    print(get_providers())
    #print(provider_by_id(--id--))
    
    # TEST new provider
    new_provider = {
        'name': "Scott Glennon",
        'email': "sglenn@gmail.com",
        'phone': "0871234567",
        'price_per_hour': 70,
        'service_id': 1
    }

    # TEST UPDATE 
    #print(create_provider(new_provider))
    # provider_diff = {
    #    'price_per_hour': 80
    #}
    #print(update_provider(id, provider_diff))
    #print(delete_provider(id))
    
    # TEST new service
    # new_service = {
    #    'name': 'Plumbing'
    #}