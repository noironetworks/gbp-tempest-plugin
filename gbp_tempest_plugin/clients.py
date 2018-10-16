from tempest import clients
from tempest import config
from tempest.lib import auth

from gbp_tempest_plugin.services.gbp.v2.json.policy_action_client import PolicyActionClient
from gbp_tempest_plugin.services.gbp.v2.json.policy_classifier_client import PolicyClassifierClient
from gbp_tempest_plugin.services.gbp.v2.json.policy_rule_client import PolicyRuleClient
from gbp_tempest_plugin.services.gbp.v2.json.policy_rule_set_client import PolicyRuleSetClient

CONF = config.CONF

class ManagerV2(clients.Manager):

    def __init__(self, credentials=None):
        super(ManagerV2, self).__init__(credentials)
        self._init_clients(self._get_params())

    def _init_clients(self, params):
        self.policy_action_client  = PolicyActionClient(**params)
        self.policy_classifier_client = PolicyClassifierClient(**params)
        self.policy_rule_client = PolicyRuleClient(**params)
        self.policy_rule_set_client = PolicyRuleSetClient(**params)

    def _get_params(self):
        params = dict(self.default_params)
        params.update({
            'auth_provider': self.auth_provider,
            'service': CONF.network.catalog_type,
            'region': CONF.identity.region,
            'endpoint_type': CONF.network.endpoint_type,
        })
        return params

