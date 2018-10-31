from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class ServiceChainSpecTest(base.BaseGbpV2Test):

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
        super(ServiceChainSpecTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(ServiceChainSpecTest, cls).setup_clients()
        cls.client = cls.os_primary.service_chain_spec_client

    def test_create_service_chain_spec(self):
        LOG.info('Create a Service Chain Spec')
        body = self.client.create_service_chain_spec(name="test")
        self.addCleanup(self.client.delete_service_chain_spec, body['service_chain_spec']['id'])
        self.assertEqual("test", body['service_chain_spec']['name'])

    def test_list_service_chain_specs(self):
        LOG.info('Create a Service Chain Spec')
        body = self.client.create_service_chain_spec(name="test")
        self.addCleanup(self.client.delete_service_chain_spec, body['service_chain_spec']['id'])
        LOG.info('List Service Chain Specs')
        body = self.client.list_service_chain_specs()
        self.assertGreater(len(body['service_chain_specs']), 0)

    def test_show_service_chain_spec(self):
        LOG.info('Create a Service Chain Spec')
        body = self.client.create_service_chain_spec(name="test")
        self.addCleanup(self.client.delete_service_chain_spec, body['service_chain_spec']['id'])
        LOG.info('Fetch Service Chain Specs')
        body = self.client.show_service_chain_spec(body['service_chain_spec']['id'])
        self.assertEqual("test", body['service_chain_spec']['name'])

    def test_update_service_chain_spec(self):
        LOG.info('Create a Service Chain Spec')
        body = self.client.create_service_chain_spec(name="test")
        self.addCleanup(self.client.delete_service_chain_spec, body['service_chain_spec']['id'])
        LOG.info('Update Service Chain Specs')
        body = self.client.update_service_chain_spec(body['service_chain_spec']['id'], name="test2")
        self.assertEqual("test2", body['service_chain_spec']['name'])

