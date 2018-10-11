from tempest import clients
from tempest import config
from tempest.lib import auth

from gbp_tempest_plugin.services.gbp.v2.json.policyaction_client import PolicyActionClient

CONF = config.CONF

class ManagerV2(clients.Manager):

    def __init__(self, credentials=None):
        super(ManagerV2, self).__init__(credentials)
        self._init_clients(self._get_params())

    def _init_clients(self, params):
        self.policyaction_client  = PolicyActionClient(**params)

    def _get_params(self):
        params = dict(self.default_params)
        params.update({
            'auth_provider': self.auth_provider,
            'service': CONF.network.catalog_type,
            'region': CONF.identity.region,
            'endpoint_type': CONF.network.endpoint_type,
        })
        return params

