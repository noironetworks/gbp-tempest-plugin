from tempest.lib.common.utils import data_utils
from six.moves import http_client
from tempest.lib.common import rest_client
from oslo_serialization import jsonutils as json

from gbp_tempest_plugin.services.gbp.v2.json import base

class PolicyActionClient(base.GbpClientV2Base):
    """API V2 Tempest REST client for GBP Policy Action API"""

    resource = "/grouppolicy/policy_actions"

    def create_policy_action(self, name, **kwargs):
        """Create a Policy action"""
        post_body = {'policy_action': {'name': name }}
        if kwargs.get('action_type'):
            post_body['action_type'] = kwargs.get('action_type')
        if kwargs.get('description'):
            post_body['description'] = kwargs.get('description')
        post_body = json.dumps(post_body)
        resp, body = self.post(self.get_uri(self.resource), post_body)
        body = json.loads(body)
        self.expected_success(http_client.CREATED, resp.status)
        return rest_client.ResponseBody(resp, body)

    def list_policy_actions(self):
        """List policy actions"""
        resp, body = self.get(self.get_uri(self.resource))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def delete_policy_action(self, id):
        """Delete policy action"""
        resp, body = self.delete(self.get_uri(self.resource, id))
        self.expected_success(http_client.NO_CONTENT, resp.status)
        return rest_client.ResponseBody(resp, body)

    def show_policy_action(self, id):
        """Show policy action"""
        resp, body = self.get(self.get_uri(self.resource, id))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def update_policy_action(self, id, **kwargs):
        """Update existing policy action"""
        resp, body = self.put(self.get_uri(self.resource, id), json.dumps({'policy_action':kwargs}))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)
 

