from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class PolicyRuleTest(base.BaseGbpV2Test):

    @classmethod
    def setup_credentials(cls):
        """This section is used to do any manual credential allocation and also
           in the case of dynamic credentials to override the default network
           resource creation/auto allocation
        """
        # This call is used to tell the credential allocator to not create any
        # network resources for this test case. It also enables selective
        # creation of other neutron resources. NOTE: it must go before the
        # super call
        cls.set_network_resources()
        super(PolicyRuleTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(PolicyRuleTest, cls).setup_clients()
        cls.client = cls.os_primary.policy_rule_client
        cls.classifier_client = cls.os_primary.poicy_classifier_client
        cls.action_client = cls.os_primary.policy_action_client

    def _create_policy_rule(self, name):
        LOG.info('Create a policy classifier')
        classifier = self.classifier_client.create_policy_classifier("test_classifier")
        self.addCleanup(self.classifier_client.delete_policy_classifier, classifier['policy_classifier']['id'])

        LOG.info('Create a policy action')
        action = self.action_client(name="test_rule")
        self.addCleanup(self.action_client.delete_policy_action, action['policy_action']['id'])

        LOG.info('Create a policy rule')
        body = self.client.create_policy_rule(name, classifier="test_classifier", action ="test_rule")
        self.addCleanup(self.client.delete_policy_rule, body['policy_rule']['id'])
        return body

    def test_create_policy_rule(self):
        body = self._create_policy_rule(name="test") 
        self.assertEqual("test", body['policy_rule']['name'])

    def test_list_policy_rule(self):
        self._create_policy_rule(name="test") 
        LOG.info('List policy rule')
        body = self.client.list_policy_rules()
        self.assertGreater(len(body['policy_rules']), 0)

    def test_show_policy_rule(self):
        body = self._create_policy_rule(name="test")
        LOG.info('Fetch policy rule')
        body = self.client.show_policy_rule(body['policy_rule']['id'])
        self.assertEqual("test", body['policy_rule']['name'])

    def test_update_policy_rule(self):
        body = self._create_policy_rule(name="test")
        LOG.info('Update policy rule')
        body = self.client.update_policy_rule(body['policy_rule']['id'], name="test2")
        self.assertEqual("test2", body['policy_rule']['name'])

