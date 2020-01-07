import sys
from key_vault_sample_base import KeyVaultSampleBase, keyvaultsample, get_name, run_all_samples
from azure.common.credentials import ServicePrincipalCredentials
from azure.keyvault import KeyVaultClient, KeyVaultAuthentication, KeyVaultId

class TestAuth(KeyVaultSampleBase):
    
    def sp_auth(self):
        vault = self.create_vault()
        credentials = ServicePrincipalCredentials(  client_id = self.config.client_id,
                                                    secret = self.config.client_secret,
                                                    tenant = self.config.tenant_id)

        client = KeyVaultClient(credentials)

        #set secret
        secret_bundle = client.set_secret(vault.properties.vault_uri, 'auth-sample-secret', 'successfully authenticated')
        print(secret_bundle)

        #get secret
        secret_bundle = client.get_secret(vault.properties.vault_uri, 'auth-sample-secret', secret_version = KeyVaultId.version_none)
        print(secret_bundle)


