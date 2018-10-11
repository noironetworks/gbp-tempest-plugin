from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class PolicyActionTest(base.BaseGbpV2Test):

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
        super(PolicyActionTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(PolicyActionTest, cls).setup_clients()
        cls.client = cls.os_primary.policyaction_client

    def test_create_policy_action(self):
        LOG.info('Create a policy action')
        body = self.client.create_policy_action(name="test")
        self.addCleanup(self.client.delete_policy_action, body['policy_action']['id'])
        self.assertEqual("test", body['policy_action']['name'])

    def test_list_policy_actions(self):
        LOG.info('Create a policy action')
        body = self.client.create_policy_action(name="test")
        self.addCleanup(self.client.delete_policy_action, body['policy_action']['id'])
        LOG.info('List policy actions')
        body = self.client.list_policy_actions()
        self.assertGreater(len(body['policy_actions']), 0)

    def test_show_policy_action(self):
        LOG.info('Create a policy action')
        body = self.client.create_policy_action(name="test")
        self.addCleanup(self.client.delete_policy_action, body['policy_action']['id'])
        LOG.info('Fetch policy actions')
        body = self.client.show_policy_action(body['policy_action']['id'])
        self.assertEqual("test", body['policy_action']['name'])

    def test_update_policy_action(self):
        LOG.info('Create a policy action')
        body = self.client.create_policy_action(name="test")
        self.addCleanup(self.client.delete_policy_action, body['policy_action']['id'])
        LOG.info('Update policy actions')
        body = self.client.update_policy_action(body['policy_action']['id'], name="test2")
        self.assertEqual("test2", body['policy_action']['name'])

