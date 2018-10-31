from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class PolicyTargetTest(base.BaseGbpV2Test):

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
        super(PolicyTargetTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(PolicyTargetTest, cls).setup_clients()
        cls.client = cls.os_primary.policy_target_client
        cls.policy_target_group_client = cls.os_primary.policy_target_group_client

    def _create_policy_target(self, name):
        LOG.info('Create an policy target group')
        policy_target_group = self.policy_target_group_client.create_policy_target_group(name="test")
        self.addCleanup(self.policy_target_group_client.delete_policy_target_group, policy_target_group['policy_target_group']['id'])
        LOG.info('Create a policy target')
        body = self.client.create_policy_target(name, policy_target_group['policy_target_group']['id'])
        self.addCleanup(self.client.delete_policy_target, body['policy_target']['id'])
        return body

    def test_create_policy_target(self):
        body = self._create_policy_target("test")
        self.assertEqual("test", body['policy_target']['name'])

    def test_list_policy_target(self):
        body = self._create_policy_target("test")
        LOG.info('List Application policy groups')
        body = self.client.list_policy_targets()
        self.assertGreater(len(body['policy_targets']), 0)

    def test_show_policy_target(self):
        body = self._create_policy_target("test")
        LOG.info('Fetch a policy target group')
        body = self.client.show_policy_target(body['policy_target']['id'])
        self.assertEqual("test", body['policy_target']['name'])

    def test_update_policy_target(self):
        body = self._create_policy_target("test")
        LOG.info('Update a policy target')
        body = self.client.update_policy_target(body['policy_target']['id'], name="test2")
        self.assertEqual("test2", body['policy_target']['name'])

