from tempest.lib.common.utils import data_utils
from six.moves import http_client
from tempest.lib.common import rest_client
from oslo_serialization import jsonutils as json

from gbp_tempest_plugin.services.gbp.v2.json import base

class ServicechainSpecClient(base.GbpClientV2Base):
    """API V2 Tempest REST client for GBP Servicechain Spec API"""

    resource = "/grouppolicy/servicechain_specs"

    def create_servicechain_spec(self, name, **kwargs):
        """Create a Servicechain Spec"""
        post_body = {'servicechain_spec': {'name': name}}
        if kwargs.get('description'):
            post_body['servicechain_spec']['description'] = kwargs.get('description')
        post_body = json.dumps(post_body)
        resp, body = self.post(self.get_uri(self.resource), post_body)
        body = json.loads(body)
        self.expected_success(http_client.CREATED, resp.status)
        return rest_client.ResponseBody(resp, body)

    def list_servicechain_specs(self):
        """List Servicechain Specs"""
        resp, body = self.get(self.get_uri(self.resource))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def delete_servicechain_spec(self, id):
        """Delete a Servicechain Spec"""
        resp, body = self.delete(self.get_uri(self.resource, id))
        self.expected_success(http_client.NO_CONTENT, resp.status)
        return rest_client.ResponseBody(resp, body)

    def show_servicechain_spec(self, id):
        """Show a Servicechain Spec"""
        resp, body = self.get(self.get_uri(self.resource, id))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def update_servicechain_spec(self, id, **kwargs):
        """Update an existing External Policy"""
        resp, body = self.put(self.get_uri(self.resource, id), json.dumps({'servicechain_spec':kwargs}))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)
