from oslo_log import log as logging
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc
from tempest.lib.common.utils import data_utils

from gbp_tempest_plugin.tests import base

LOG = logging.getLogger(__name__)

class PolicyClassifierTest(base.BaseGbpV2Test):

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
        super(PolicyClassifierTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(PolicyClassifierTest, cls).setup_clients()
        cls.client = cls.os_primary.policy_classifier_client

    def test_create_policy_classifier(self):
        LOG.info('Create a policy classifier')
        body = self.client.create_policy_classifier(name="test")
        self.addCleanup(self.client.delete_policy_classifier, body['policy_classifier']['id'])
        self.assertEqual("test", body['policy_classifier']['name'])

    def test_list_policy_classifier(self):
        LOG.info('Create a policy classifier')
        body = self.client.create_policy_classifier(name="test")
        self.addCleanup(self.client.delete_policy_classifier, body['policy_classifier']['id'])
        LOG.info('List policy classifier')
        body = self.client.list_policy_classifiers()
        self.assertGreater(len(body['policy_classifiers']), 0)

    def test_show_policy_classifier(self):
        LOG.info('Create a policy classifier')
        body = self.client.create_policy_classifier(name="test")
        self.addCleanup(self.client.delete_policy_classifier, body['policy_classifier']['id'])
        LOG.info('Fetch policy classifier')
        body = self.client.show_policy_classifier(body['policy_classifier']['id'])
        self.assertEqual("test", body['policy_classifier']['name'])

    def test_update_policy_classifier(self):
        LOG.info('Create a policy classifier')
        body = self.client.create_policy_classifier(name="test")
        self.addCleanup(self.client.delete_policy_classifier, body['policy_classifier']['id'])
        LOG.info('Update policy classifier')
        body = self.client.update_policy_classifier(body['policy_classifier']['id'], name="test2")
        self.assertEqual("test2", body['policy_classifier']['name'])

