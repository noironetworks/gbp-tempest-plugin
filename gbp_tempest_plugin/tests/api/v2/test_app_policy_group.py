from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class AppPolicyGroupTest(base.BaseGbpV2Test):

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
        super(AppPolicyGroupTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(AppPolicyGroupTest, cls).setup_clients()
        cls.client = cls.os_primary.app_policy_group_client

    def test_create_app_policy_group(self):
        LOG.info('Create an Application policy group')
        body = self.client.create_app_policy_group(name="test")
        self.addCleanup(self.client.delete_app_policy_group, body['application_policy_group']['id'])
        self.assertEqual("test", body['application_policy_group']['name'])

    def test_list_app_policy_groups(self):
        LOG.info('Create an Application policy group')
        body = self.client.create_app_policy_group(name="test")
        self.addCleanup(self.client.delete_app_policy_group, body['application_policy_group']['id'])
        LOG.info('List Application policy groups')
        body = self.client.list_app_policy_groups()
        self.assertGreater(len(body['application_policy_groups']), 0)

    def test_show_app_policy_group(self):
        LOG.info('Create an Application policy group')
        body = self.client.create_app_policy_group(name="test")
        self.addCleanup(self.client.delete_app_policy_group, body['application_policy_group']['id'])
        LOG.info('Fetch an Application policy group')
        body = self.client.show_app_policy_group(body['application_policy_group']['id'])
        self.assertEqual("test", body['application_policy_group']['name'])

    def test_update_app_policy_group(self):
        LOG.info('Create an Application policy group')
        body = self.client.create_app_policy_group(name="test")
        self.addCleanup(self.client.delete_app_policy_group, body['application_policy_group']['id'])
        LOG.info('Update an Application policy group')
        body = self.client.update_app_policy_group(body['application_policy_group']['id'], name="test2")
        self.assertEqual("test2", body['application_policy_group']['name'])
