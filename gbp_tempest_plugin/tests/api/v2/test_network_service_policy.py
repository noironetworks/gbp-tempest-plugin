from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class NetworkServicePolicyTest(base.BaseGbpV2Test):

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
        super(NetworkServicePolicyTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(NetworkServicePolicyTest, cls).setup_clients()
        cls.client = cls.os_primary.network_service_policy_client

    def test_create_network_service_policy(self):
        LOG.info('Create a network service policy')
        body = self.client.create_network_service_policy(name="test")
        self.addCleanup(self.client.delete_network_service_policy, body['network_service_policy']['id'])
        self.assertEqual("test", body['network_service_policy']['name'])

    def test_list_network_service_policies(self):
        LOG.info('Create a network service policy')
        body = self.client.create_network_service_policy(name="test")
        self.addCleanup(self.client.delete_network_service_policy, body['network_service_policy']['id'])
        LOG.info('List network service policies')
        body = self.client.list_network_service_policies()
        self.assertGreater(len(body['network_service_policies']), 0)

    def test_show_network_service_policy(self):
        LOG.info('Create a network service policy')
        body = self.client.create_network_service_policy(name="test")
        self.addCleanup(self.client.delete_network_service_policy, body['network_service_policy']['id'])
        LOG.info('Fetch a network service policy')
        body = self.client.show_network_service_policy(body['network_service_policy']['id'])
        self.assertEqual("test", body['network_service_policy']['name'])

    def test_update_network_service_policy(self):
        LOG.info('Create a network service policy')
        body = self.client.create_network_service_policy(name="test")
        self.addCleanup(self.client.delete_network_service_policy, body['network_service_policy']['id'])
        LOG.info('Update a network service policy')
        body = self.client.update_network_service_policy(body['network_service_policy']['id'], name="test2")
        self.assertEqual("test2", body['network_service_policy']['name'])
