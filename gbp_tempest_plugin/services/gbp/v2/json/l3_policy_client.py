from tempest.lib.common.utils import data_utils
from six.moves import http_client
from tempest.lib.common import rest_client
from oslo_serialization import jsonutils as json

from gbp_tempest_plugin.services.gbp.v2.json import base

class L3PolicyClient(base.GbpClientV2Base):
    """API V2 Tempest REST client for GBP L2 Policy API"""

    resource = "/grouppolicy/l3_policies"

    def create_l3_policy(self, name, **kwargs):
        """Create a L3 policy"""
        post_body = {'l3_policy': {'name': name }}
        if kwargs.get('description'):
            post_body['description'] = kwargs.get('description')
        post_body = json.dumps(post_body)
        resp, body = self.post(self.get_uri(self.resource), post_body)
        body = json.loads(body)
        self.expected_success(http_client.CREATED, resp.status)
        return rest_client.ResponseBody(resp, body)

    def list_l3_policies(self):
        """List L3 policies"""
        resp, body = self.get(self.get_uri(self.resource))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def delete_l3_policy(self, id):
        """Delete L3 policy"""
        resp, body = self.delete(self.get_uri(self.resource, id))
        self.expected_success(http_client.NO_CONTENT, resp.status)
        return rest_client.ResponseBody(resp, body)

    def show_l3_policy(self, id):
        """Show L3 policy"""
        resp, body = self.get(self.get_uri(self.resource, id))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def update_l3_policy(self, id, **kwargs):
        """Update existing L3 policy"""
        resp, body = self.put(self.get_uri(self.resource, id), json.dumps({'l3_policy':kwargs}))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)