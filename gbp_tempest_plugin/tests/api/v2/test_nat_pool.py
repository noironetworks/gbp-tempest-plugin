from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class NatPoolTest(base.BaseGbpV2Test):

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
        super(NatPoolTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(NatPoolTest, cls).setup_clients()
        cls.client = cls.os_primary.nat_pool_client

    def test_create_nat_pool(self):
        LOG.info('Create a NAT pool')
        body = self.client.create_nat_pool(name="test")
        self.addCleanup(self.client.delete_nat_pool, body['nat_pool']['id'])
        self.assertEqual("test", body['nat_pool']['name'])

    def test_list_nat_pools(self):
        LOG.info('Create a NAT pool')
        body = self.client.create_nat_pool(name="test")
        self.addCleanup(self.client.delete_nat_pool, body['nat_pool']['id'])
        LOG.info('List NAT pools')
        body = self.client.list_external_policies()
        self.assertGreater(len(body['nat_pools']), 0)

    def test_show_nat_pool(self):
        LOG.info('Create a NAT pool')
        body = self.client.create_nat_pool(name="test")
        self.addCleanup(self.client.delete_nat_pool, body['nat_pool']['id'])
        LOG.info('Fetch a NAT pool')
        body = self.client.show_nat_pool(body['nat_pool']['id'])
        self.assertEqual("test", body['nat_pool']['name'])

    def test_update_nat_pool(self):
        LOG.info('Create a NAT pool')
        body = self.client.create_nat_pool(name="test")
        self.addCleanup(self.client.delete_nat_pool, body['nat_pool']['id'])
        LOG.info('Update a NAT pool')
        body = self.client.update_nat_pool(body['nat_pool']['id'], name="test2")
        self.assertEqual("test2", body['nat_pool']['name'])
