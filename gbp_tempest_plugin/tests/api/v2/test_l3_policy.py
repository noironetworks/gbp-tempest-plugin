from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class L3PolicyTest(base.BaseGbpV2Test):

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
        super(L3PolicyTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(L3PolicyTest, cls).setup_clients()
        cls.client = cls.os_primary.l3_policy_client

    def test_create_l3_policy(self):
        LOG.info('Create a L3 policy')
        body = self.client.create_l3_policy(name="test")
        self.addCleanup(self.client.delete_l3_policy, body['l3_policy']['id'])
        self.assertEqual("test", body['l3_policy']['name'])

    def test_list_l3_policies(self):
        LOG.info('Create a L3 policy')
        body = self.client.create_l3_policy(name="test")
        self.addCleanup(self.client.delete_l3_policy, body['l3_policy']['id'])
        LOG.info('List L3 policies')
        body = self.client.list_l3_policies()
        self.assertGreater(len(body['l3_policies']), 0)

    def test_show_l3_policy(self):
        LOG.info('Create a L3 policy')
        body = self.client.create_l3_policy(name="test")
        self.addCleanup(self.client.delete_l3_policy, body['l3_policy']['id'])
        LOG.info('Fetch L3 policy')
        body = self.client.show_l3_policy(body['l3_policy']['id'])
        self.assertEqual("test", body['l3_policy']['name'])

    def test_update_l3_policy(self):
        LOG.info('Create a L3 policy')
        body = self.client.create_l3_policy(name="test")
        self.addCleanup(self.client.delete_l3_policy, body['l3_policy']['id'])
        LOG.info('Update L3 policy')
        body = self.client.update_l3_policy(body['l3_policy']['id'], name="test2")
        self.assertEqual("test2", body['l3_policy']['name'])
