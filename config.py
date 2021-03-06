import os

# Replace with given bearer token or add given bearer token to environment variables as such
bearer_token = os.environ.get('BEARER_TOKEN')
header = {'Authorization': 'Bearer ' + bearer_token}

# If using another zendesk subdomain change the API url here, this may go down after this subdomains trial expires
api = 'https://zccsupport.zendesk.com/api/v2/'
