import os

class KeyVaultSampleConfig(object):

    def _init_(self):
        self.subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID', '11111111-1111-1111-1111-111111111111')
        self.client_id = os.getenv('AZURE_CLIENT_ID', '22222222-2222-2222-2222-222222222222')
        self.client_oid = os.getenv('AZURE_CLIENT_OID', '33333333-3333-3333-3333-333333333333')
        self.tenant_id = os.getenv('AZURE_TENANT_ID', '44444444-4444-4444-4444-444444444444')
        self.client_secret = os.getenv('AZURE_CLIENT_SECRET', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz=')
        self.location = os.getenv('AZURE_LOCATION', 'westus')
        self.group_name = os.getenv('AZURE_RESOURCE_GROUP', 'azure-key-vault-samples')
