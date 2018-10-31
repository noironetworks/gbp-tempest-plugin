from tempest.lib.common.utils import data_utils
from six.moves import http_client
from tempest.lib.common import rest_client
from oslo_serialization import jsonutils as json

from gbp_tempest_plugin.services.gbp.v2.json import base

class NetworkServicePolicyClient(base.GbpClientV2Base):
    """API V2 Tempest REST client for GBP Network Service Policy API"""

    resource = "/grouppolicy/network_service_policies"

    def create_network_service_policy(self, name, **kwargs):
        """Create a Network Service Policy"""
        post_body = {'network_service_policy': {'name': name}}
        if kwargs.get('description'):
            post_body['description'] = kwargs.get('description')
        post_body = json.dumps(post_body)
        resp, body = self.post(self.get_uri(self.resource), post_body)
        body = json.loads(body)
        self.expected_success(http_client.CREATED, resp.status)
        return rest_client.ResponseBody(resp, body)

    def list_network_service_policies(self):
        """List Network Service Policies"""
        resp, body = self.get(self.get_uri(self.resource))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def delete_network_service_policy(self, id):
        """Delete a Network Service Policy"""
        resp, body = self.delete(self.get_uri(self.resource, id))
        self.expected_success(http_client.NO_CONTENT, resp.status)
        return rest_client.ResponseBody(resp, body)

    def show_network_service_policy(self, id):
        """Show a Network Service Policy"""
        resp, body = self.get(self.get_uri(self.resource, id))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def update_network_service_policy(self, id, **kwargs):
        """Update a existing Network Service Policy"""
        resp, body = self.put(self.get_uri(self.resource, id), json.dumps({'network_service_policy':kwargs}))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)
