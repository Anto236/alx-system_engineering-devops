import requests

# Datadog API endpoint for getting the list of hosts
url = 'https://api.datadoghq.com/api/v1/hosts'

# Your Datadog API key and application key
api_key = '51c71a24a8558816a707cccb18e7994f'
app_key = '6e2092e340dd1d4bea61ddceca1478d229f232dd'

# Parameters for the API request
params = {
    'api_key': api_key,
    'application_key': app_key
}

# Send the API request
response = requests.get(url, params=params)

# Parse the JSON response
response_json = response.json()

# Check if the host is in the list of hosts
host_name = '102807-web-01'
hosts = response_json.get('hosts', [])
if any(host.get('name') == host_name for host in hosts):
    print(f"The host {host_name} is present in Datadog.")
else:
    print(f"The host {host_name} is NOT present in Datadog.")
