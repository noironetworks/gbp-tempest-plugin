from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests.api.v2 import test_external_segment

LOG = logging.getLogger(__name__)

class NATPoolTest(test_external_segment.ExternalSegmentTest):

    @classmethod
    def setup_clients(cls):
        super(NATPoolTest, cls).setup_clients()
        cls.nat_client = cls.os_primary.nat_pool_client

    def _create_nat_pool(self, name):
        LOG.info('Create an External Segment')
        segment = self._create_external_segment(data_utils.rand_name(self.__class__.__name__))
        LOG.info('Create a NAT pool')
        nat_pool = self.nat_client.create_nat_pool(name, segment['id'], '10.64.0.0/24')['nat_pool']
        self.addCleanup(self.nat_client.delete_nat_pool,nat_pool['id'])
        return nat_pool

    def test_create_nat_pool(self):
        name = data_utils.rand_name(self.__class__.__name__)
        nat_pool = self._create_nat_pool(name)
        self.assertEqual(name, nat_pool['name'])

    def test_list_nat_pools(self):
        name = data_utils.rand_name(self.__class__.__name__)
        self._create_nat_pool(name)
        LOG.info('List NAT pools')
        body = self.nat_client.list_nat_pools()
        self.assertGreater(len(body['nat_pools']), 0)

    def test_show_nat_pool(self):
        name = data_utils.rand_name(self.__class__.__name__)
        nat_pool = self._create_nat_pool(name)
        LOG.info('Fetch a NAT pool')
        body = self.nat_client.show_nat_pool(nat_pool['id'])
        self.assertEqual(name, body['nat_pool']['name'])

    def test_update_nat_pool(self):
        name = data_utils.rand_name(self.__class__.__name__)
        new_name = data_utils.rand_name(self.__class__.__name__)
        nat_pool = self._create_nat_pool(name)
        LOG.info('Update a NAT pool')
        body = self.nat_client.update_nat_pool(nat_pool['id'], name=new_name)
        self.assertEqual(new_name, body['nat_pool']['name'])
