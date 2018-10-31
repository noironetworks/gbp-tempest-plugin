from tempest.lib.common.utils import data_utils
from six.moves import http_client
from tempest.lib.common import rest_client
from oslo_serialization import jsonutils as json

from gbp_tempest_plugin.services.gbp.v2.json import base

class ExternalSegmentClient(base.GbpClientV2Base):
    """API V2 Tempest REST client for GBP External Segment API"""

    resource = "/grouppolicy/external_segments"

    def create_external_segment(self, name, **kwargs):
        """Create an External Segment"""
        post_body = {'external_segment': {'name': name}}
        if kwargs.get('description'):
            post_body['description'] = kwargs.get('description')
        post_body = json.dumps(post_body)
        resp, body = self.post(self.get_uri(self.resource), post_body)
        body = json.loads(body)
        self.expected_success(http_client.CREATED, resp.status)
        return rest_client.ResponseBody(resp, body)

    def list_external_segments(self):
        """List External Segments"""
        resp, body = self.get(self.get_uri(self.resource))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def delete_external_segment(self, id):
        """Delete an External Segment"""
        resp, body = self.delete(self.get_uri(self.resource, id))
        self.expected_success(http_client.NO_CONTENT, resp.status)
        return rest_client.ResponseBody(resp, body)

    def show_external_segment(self, id):
        """Show an External Segment"""
        resp, body = self.get(self.get_uri(self.resource, id))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)

    def update_external_segment(self, id, **kwargs):
        """Update an existing External Segment"""
        resp, body = self.put(self.get_uri(self.resource, id), json.dumps({'external_segment':kwargs}))
        body = json.loads(body)
        self.expected_success(http_client.OK, resp.status)
        return rest_client.ResponseBody(resp, body)
