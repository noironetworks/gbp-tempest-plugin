from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class ServicechainSpecTest(base.BaseGbpV2Test):

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
        super(ServicechainSpecTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(ServicechainSpecTest, cls).setup_clients()
        cls.client = cls.os_primary.servicechain_spec_client

    def test_create_servicechain_spec(self):
        LOG.info('Create a Servicechain Spec')
        body = self.client.create_servicechain_spec(name="test")
        self.addCleanup(self.client.delete_servicechain_spec, body['servicechain_spec']['id'])
        self.assertEqual("test", body['servicechain_spec']['name'])

    def test_list_servicechain_specs(self):
        LOG.info('Create a Servicechain Spec')
        body = self.client.create_servicechain_spec(name="test")
        self.addCleanup(self.client.delete_servicechain_spec, body['servicechain_spec']['id'])
        LOG.info('List Servicechain Specs')
        body = self.client.list_servicechain_specs()
        self.assertGreater(len(body['servicechain_specs']), 0)

    def test_show_servicechain_spec(self):
        LOG.info('Create a Servicechain Spec')
        body = self.client.create_servicechain_spec(name="test")
        self.addCleanup(self.client.delete_servicechain_spec, body['servicechain_spec']['id'])
        LOG.info('Fetch Servicechain Specs')
        body = self.client.show_servicechain_spec(body['servicechain_spec']['id'])
        self.assertEqual("test", body['servicechain_spec']['name'])

    def test_update_servicechain_spec(self):
        LOG.info('Create a Servicechain Spec')
        body = self.client.create_servicechain_spec(name="test")
        self.addCleanup(self.client.delete_servicechain_spec, body['servicechain_spec']['id'])
        LOG.info('Update Servicechain Specs')
        body = self.client.update_servicechain_spec(body['servicechain_spec']['id'], name="test2")
        self.assertEqual("test2", body['servicechain_spec']['name'])

