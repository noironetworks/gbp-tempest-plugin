from oslo_serialization import jsonutils as json
from six.moves import http_client
from tempest import exceptions
from tempest.lib.common import rest_client
from tempest.lib import exceptions as lib_exc

class GbpClientV2Base(rest_client.RestClient):
    """Base API V2 Tempest REST client for GBP API"""

    uri_prefix = "v2.0"

    def get_uri(self, resource_name, uuid=None, params=None):
        """Get URI for a specific resource or object.
        :param resource_name: The name of the REST resource, e.g., 'zones'.
        :param uuid: The unique identifier of an object in UUID format.
        :param params: A Python dict that represents the query paramaters to
                       include in the request URI.
        :returns: Relative URI for the resource or object.
        """
        uri_pattern = '{pref}/{res}{uuid}{params}'

        uuid = '/%s' % uuid if uuid else ''
        params = '?%s' % urllib.urlencode(params) if params else ''

        return uri_pattern.format(pref=self.uri_prefix,
                                  res=resource_name,
                                  uuid=uuid,
                                  params=params)

