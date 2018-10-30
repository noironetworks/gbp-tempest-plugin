from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class L2PolicyTest(base.BaseGbpV2Test):

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
        super(L2PolicyTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(L2PolicyTest, cls).setup_clients()
        cls.client = cls.os_primary.l2_policy_client
        cls.l3_policy_client = cls.os_primary.l3_policy_client

    def _create_l2_policy(self, name):
        LOG.info('Create a L3 policy')
        l3_policy = self.l3_policy_client.create_l3_policy("test_l3_policy")
        self.addCleanup(self.l3_policy_client.delete_l3_policy, l3_policy['l3_policy']['id'])

        LOG.info('Create a L2 policy')
        body = self.client.create_l2_policy(name, l3_policy_id=l3_policy['l3_policy']['id'])
        self.addCleanup(self.client.delete_l2_policy, body['l2_policy']['id'])
        return body

    def test_create_l2_policy(self):
        LOG.info('Create a L2 policy')
        body = self._create_l2_policy("test")
        self.assertEqual("test", body['policy_action']['name'])

    def test_list_l2_policies(self):
        LOG.info('Create a L2 policy')
        body = self._create_l2_policy("test")
        LOG.info('List L2 policies')
        body = self.client.list_policy_actions()
        self.assertGreater(len(body['l2_policies']), 0)

    def test_show_l2_policy(self):
        LOG.info('Create a L2 policy')
        body = self._create_l2_policy("test")
        LOG.info('Fetch L2 policy')
        body = self.client.show_policy_action(body['l2_policy']['id'])
        self.assertEqual("test", body['l2_policy']['name'])

    def test_update_l2_policy(self):
        LOG.info('Create a L2 policy')
        body = self._create_l2_policy("test")
        LOG.info('Update L2 policy')
        body = self.client.update_policy_action(body['l2_policy']['id'], name="test2")
        self.assertEqual("test2", body['l2_policy']['name'])
