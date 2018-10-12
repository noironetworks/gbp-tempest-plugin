from tempest.lib.common.utils import data_utils
from six.moves import http_client
from tempest.lib.common import rest_client
from oslo_serialization import jsonutils as json

from gbp_tempest_plugin.services.gbp.v2.json import base

class PolicyClassifierClient(base.GbpClientV2Base):
    """API V2 Tempest REST client for GBP Policy Classifier API"""

    resource = "/grouppolicy/policy_classifiers"

    def create_policy_classifier(self, name, **kwargs):
        """Create a Policy Classifier"""
        post_body = {'policy_classifier': {'name': name }}
        if kwargs.get('protocol'):
            post_body['protocol'] = kwargs.get('protocol')
        if kwargs.get('description'):
            post_body['description'] = kwargs.get('description')
        post_body = json.dumps(post_body)
        resp, body = self.post(self.get_uri(self.resource), post_body)
        body = json.loads(body)
        self.expected_success(http_client.CREATED, resp.status)
        return rest_client.ResponseBody(resp, body)

    def list_policy_classifiers(self):
        """List policy actions"""
        resp, body = self.get(self.get_uri(self.resource))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def delete_policy_classifier(self, id):
        """Delete policy action"""
        resp, body = self.delete(self.get_uri(self.resource, id))
        self.expected_success(http_client.NO_CONTENT, resp.status)
        return rest_client.ResponseBody(resp, body)

    def show_policy_classifier(self, id):
        """Show policy action"""
        resp, body = self.get(self.get_uri(self.resource, id))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def update_policy_classifier(self, id, **kwargs):
        """Update existing policy action"""
        resp, body = self.put(self.get_uri(self.resource, id), json.dumps({'policy_classifier':kwargs}))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

