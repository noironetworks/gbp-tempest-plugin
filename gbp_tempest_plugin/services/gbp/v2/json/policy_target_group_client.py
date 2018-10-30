from tempest.lib.common.utils import data_utils
from six.moves import http_client
from tempest.lib.common import rest_client
from oslo_serialization import jsonutils as json

from gbp_tempest_plugin.services.gbp.v2.json import base

class PolicyTargetGroupClient(base.GbpClientV2Base):
    """API V2 Tempest REST client for GBP Policy Target Group API"""

    resource = "/grouppolicy/policy_target_groups"

    def create_policy_target_group(self, name, **kwargs):
        """Create a Policy Target Group"""
        post_body = {'policy_target_group': {'name': name}}
        if kwargs.get('description'):
            post_body['description'] = kwargs.get('description')
        post_body = json.dumps(post_body)
        resp, body = self.post(self.get_uri(self.resource), post_body)
        body = json.loads(body)
        self.expected_success(http_client.CREATED, resp.status)
        return rest_client.ResponseBody(resp, body)

    def list_policy_target_groups(self):
        """List Policy Target Groups"""
        resp, body = self.get(self.get_uri(self.resource))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def delete_policy_target_group(self, id):
        """Delete a Policy Target Group"""
        resp, body = self.delete(self.get_uri(self.resource, id))
        self.expected_success(http_client.NO_CONTENT, resp.status)
        return rest_client.ResponseBody(resp, body)

    def show_policy_target_group(self, id):
        """Show a Policy Target Group"""
        resp, body = self.get(self.get_uri(self.resource, id))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def update_policy_target_group(self, id, **kwargs):
        """Update a existing Policy Target Group"""
        resp, body = self.put(self.get_uri(self.resource, id), json.dumps({'policy_target_group':kwargs}))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)
