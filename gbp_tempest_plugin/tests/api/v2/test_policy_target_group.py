from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class PolicyTargetGroupTest(base.BaseGbpV2Test):

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
        super(PolicyTargetGroupTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(PolicyTargetGroupTest, cls).setup_clients()
        cls.client = cls.os_primary.policy_target_group_client

    def test_create_policy_target_group(self):
        LOG.info('Create a policy target group')
        body = self.client.create_policy_target_group(name="test")
        self.addCleanup(self.client.delete_policy_target_group, body['policy_target_group']['id'])
        self.assertEqual("test", body['policy_target_group']['name'])

    def test_list_policy_target_groups(self):
        LOG.info('Create a policy target group')
        body = self.client.create_policy_target_group(name="test")
        self.addCleanup(self.client.delete_policy_target_group, body['policy_target_group']['id'])
        LOG.info('List policy target groups')
        body = self.client.list_policy_target_groups()
        self.assertGreater(len(body['policy_target_groups']), 0)

    def test_show_policy_target_group(self):
        LOG.info('Create a policy target group')
        body = self.client.create_policy_target_group(name="test")
        self.addCleanup(self.client.delete_policy_target_group, body['policy_target_group']['id'])
        LOG.info('Fetch a policy target group')
        body = self.client.show_policy_target_group(body['policy_target_group']['id'])
        self.assertEqual("test", body['policy_target_group']['name'])

    def test_update_policy_target_group(self):
        LOG.info('Create a policy target group')
        body = self.client.create_policy_target_group(name="test")
        self.addCleanup(self.client.delete_policy_target_group, body['policy_target_group']['id'])
        LOG.info('Update a policy target group')
        body = self.client.update_policy_target_group(body['policy_target_group']['id'], name="test2")
        self.assertEqual("test2", body['policy_target_group']['name'])
