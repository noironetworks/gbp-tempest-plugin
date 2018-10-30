from tempest.lib.common.utils import data_utils
from six.moves import http_client
from tempest.lib.common import rest_client
from oslo_serialization import jsonutils as json

from gbp_tempest_plugin.services.gbp.v2.json import base

class AppPolicyGroupClient(base.GbpClientV2Base):
    """API V2 Tempest REST client for GBP Application Policy Group API"""

    resource = "/grouppolicy/application_policy_groups"

    def create_app_policy_group(self, name, **kwargs):
        """Create an Application policy group"""
        post_body = {'application_policy_group': {'name': name}}
        if kwargs.get('description'):
            post_body['description'] = kwargs.get('description')
        post_body = json.dumps(post_body)
        resp, body = self.post(self.get_uri(self.resource), post_body)
        body = json.loads(body)
        self.expected_success(http_client.CREATED, resp.status)
        return rest_client.ResponseBody(resp, body)

    def list_app_policy_groups(self):
        """List Application policy groups"""
        resp, body = self.get(self.get_uri(self.resource))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def delete_app_policy_group(self, id):
        """Delete an Application policy group"""
        resp, body = self.delete(self.get_uri(self.resource, id))
        self.expected_success(http_client.NO_CONTENT, resp.status)
        return rest_client.ResponseBody(resp, body)

    def show_app_policy_group(self, id):
        """Show an Application policy group"""
        resp, body = self.get(self.get_uri(self.resource, id))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def update_app_policy_group(self, id, **kwargs):
        """Update existing an Application policy group"""
        resp, body = self.put(self.get_uri(self.resource, id), json.dumps({'application_policy_group':kwargs}))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)
