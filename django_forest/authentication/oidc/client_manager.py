from urllib.parse import urljoin

from oic.oic import Client
from oic.oic.message import ProviderConfigurationResponse

from django_forest.authentication.oidc.configuration_retriever import retrieve
from django_forest.authentication.oidc.dynamic_client_registrator import register


class OidcClientManager:
    client = None

    @classmethod
    def get_client_for_callback_url(cls, callback_url):
        # TODO use cache here, by client_id/callback_url
        if cls.client:
            return cls.client

        configuration = retrieve()
        client_credentials = register(
            {
                'token_endpoint_auth_method': 'none',
                'redirect_uris': [callback_url],
                'registration_endpoint': configuration['registration_endpoint']
            })
        client_data = {
            'client_id': client_credentials['client_id'],
            'issuer': configuration['issuer']
        }

        op_info = ProviderConfigurationResponse(
            client_id=client_data['client_id'],
            redirect_uri=callback_url,
            issuer=client_data['issuer'],
            authorization_endpoint=urljoin(client_data['issuer'], 'oidc/auth'),
            token_endpoint=urljoin(client_data['issuer'], 'oidc/token'),
            jwks_uri=urljoin(client_data['issuer'], 'oidc/jwks')
        )

        cls.client = Client(client_data['client_id'], verify_ssl=False)
        cls.client.handle_provider_config(op_info, op_info['issuer'])

        return cls.client