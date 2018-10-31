from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class ExternalSegmentTest(base.BaseGbpV2Test):

    credentials = ['primary', 'admin']

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
        super(ExternalSegmentTest, cls).setup_credentials()

    @classmethod
    def resource_setup(cls):
        """This section is used to create any resources or objects which are
           going to be used and shared by **all** test methods in the
           TestCase. Note then anything created in this section must also be
           destroyed in the corresponding resource_cleanup() method (which will
           be run during tearDownClass())
        """
        super(ExternalSegmentTest, cls).resource_setup()
        network_body = {'name': data_utils.rand_name(cls.__class__.__name__),'router:external': True, 'shared':True}
        cls.network = cls.admin_networks_client.create_network(**network_body)['network']
        cls.addClassResourceCleanup(cls.admin_networks_client.delete_network, cls.network['id'])
        cls.subnet = cls.admin_subnets_client.create_subnet(network_id=cls.network["id"],ip_version=4, cidr='10.64.0.0/24')['subnet'] 
        cls.addClassResourceCleanup(cls.admin_subnets_client.delete_subnet, cls.subnet['id'])

    @classmethod
    def setup_clients(cls):
        super(ExternalSegmentTest, cls).setup_clients()
        cls.client = cls.os_primary.external_segment_client
        cls.admin_networks_client = cls.os_admin.networks_client
        cls.admin_subnets_client = cls.os_admin.subnets_client

    def _create_external_segment(self, name):
        LOG.info('Create an external segment')
        body = self.client.create_external_segment(name, self.subnet['id'], cidr='10.64.0.0/24')
        external_segment = body['external_segment']
        self.addCleanup(self.client.delete_external_segment,external_segment['id'])
        return external_segment
      
    def test_create_external_segment(self):
        name = data_utils.rand_name(self.__class__.__name__)
        segment = self._create_external_segment(name)
        self.assertEqual(name, segment['name'])

    def test_list_external_segments(self):
        name = data_utils.rand_name(self.__class__.__name__)
        segment = self._create_external_segment(name)
        LOG.info('List external segments')
        body = self.client.list_external_segments()
        self.assertGreater(len(body['external_segments']), 0)

    def test_show_external_segment(self):
        name = data_utils.rand_name(self.__class__.__name__)
        segment = self._create_external_segment(name)
        LOG.info('Fetch an external segment')
        body = self.client.show_external_segment(segment['id'])
        self.assertEqual(name, body['external_segment']['name'])

    def test_update_external_segment(self):
        name = data_utils.rand_name(self.__class__.__name__)
        new_name = data_utils.rand_name(self.__class__.__name__)
        segment = self._create_external_segment(name)
        LOG.info('Update an external segment')
        body = self.client.update_external_segment(segment['id'], name=new_name)
        self.assertEqual(new_name, body['external_segment']['name'])
