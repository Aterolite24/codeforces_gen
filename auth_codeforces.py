import hashlib
import time
import random
import requests

def fetch_authenticated_data(method, params, api_key, secret):
    base_url = "https://codeforces.com/api/"
    rand = ''.join(random.choices('0123456789abcdef', k=6))  # Random 6 chars
    current_time = int(time.time())
    
    params["apiKey"] = api_key
    params["time"] = current_time
    
    # Construct the signature string
    sorted_params = "&".join(f"{key}={params[key]}" for key in sorted(params))
    sig_base = f"{rand}/{method}?{sorted_params}#{secret}"
    api_sig = rand + hashlib.sha512(sig_base.encode('utf-8')).hexdigest()
    
    # Add apiSig to parameters
    params["apiSig"] = api_sig
    
    # Make the request
    url = base_url + method
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to connect to Codeforces API:", response.status_code)
        return None

# Example usage
api_key = ""
secret = ""
method = "problemset.problems"
params = {"tags": "implementation"}

response = fetch_authenticated_data(method, params, api_key, secret)
if response:
    print(response)
