from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class ExternalPolicyTest(base.BaseGbpV2Test):

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
        super(ExternalPolicyTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(ExternalPolicyTest, cls).setup_clients()
        cls.client = cls.os_primary.external_policy_client

    def test_create_external_policy(self):
        LOG.info('Create an external policy')
        body = self.client.create_external_policy(name="test")
        self.addCleanup(self.client.delete_external_policy, body['external_policy']['id'])
        self.assertEqual("test", body['external_policy']['name'])

    def test_list_external_policies(self):
        LOG.info('Create an external policy')
        body = self.client.create_external_policy(name="test")
        self.addCleanup(self.client.delete_external_policy, body['external_policy']['id'])
        LOG.info('List external_policies')
        body = self.client.list_external_policies()
        self.assertGreater(len(body['external_policies']), 0)

    def test_show_external_policy(self):
        LOG.info('Create an external policy')
        body = self.client.create_external_policy(name="test")
        self.addCleanup(self.client.delete_external_policy, body['external_policy']['id'])
        LOG.info('Fetch an external policy')
        body = self.client.show_external_policy(body['external_policy']['id'])
        self.assertEqual("test", body['external_policy']['name'])

    def test_update_external_policy(self):
        LOG.info('Create an external policy')
        body = self.client.create_external_policy(name="test")
        self.addCleanup(self.client.delete_external_policy, body['external_policy']['id'])
        LOG.info('Update an external policy')
        body = self.client.update_external_policy(body['external_policy']['id'], name="test2")
        self.assertEqual("test2", body['external_policy']['name'])
