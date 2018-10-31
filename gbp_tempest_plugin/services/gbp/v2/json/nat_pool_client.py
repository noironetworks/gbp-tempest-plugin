from tempest.lib.common.utils import data_utils
from six.moves import http_client
from tempest.lib.common import rest_client
from oslo_serialization import jsonutils as json

from gbp_tempest_plugin.services.gbp.v2.json import base

class NATPoolClient(base.GbpClientV2Base):
    """API V2 Tempest REST client for GBP NAT Pool API"""

    resource = "/grouppolicy/nat_pools"

    def create_nat_pool(self, name, external_segment_id, ip_pool, **kwargs):
        """Create a NAT Pool"""
        post_body = {'nat_pool': {'name': name, 'external_segment_id': external_segment_id, 'ip_pool': ip_pool}}
        if kwargs.get('description'):
            post_body['nat_pool']['description'] = kwargs.get('description')
        post_body = json.dumps(post_body)
        resp, body = self.post(self.get_uri(self.resource), post_body)
        body = json.loads(body)
        self.expected_success(http_client.CREATED, resp.status)
        return rest_client.ResponseBody(resp, body)

    def list_nat_pools(self):
        """List NAT Pools"""
        resp, body = self.get(self.get_uri(self.resource))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def delete_nat_pool(self, id):
        """Delete a NAT Pool"""
        resp, body = self.delete(self.get_uri(self.resource, id))
        self.expected_success(http_client.NO_CONTENT, resp.status)
        return rest_client.ResponseBody(resp, body)

    def show_nat_pool(self, id):
        """Show a NAT Pool"""
        resp, body = self.get(self.get_uri(self.resource, id))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def update_nat_pool(self, id, **kwargs):
        """Update an existing External Policy"""
        resp, body = self.put(self.get_uri(self.resource, id), json.dumps({'nat_pool':kwargs}))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)
