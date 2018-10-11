from tempest import test
from tempest import config

CONF = config.CONF

class BaseGbpTest(test.BaseTestCase):
    """Base class for GBP tests."""

    credentials = ['primary']

    @classmethod
    def skip_checks(cls):
        super(BaseGbpTest, cls).skip_checks()
        print(CONF.service_available.gbp)
        if not CONF.service_available.gbp:
            skip_msg = ("%s skipped as GBP is not available"
                        % cls.__name__)
            raise cls.skipException(skip_msg)


class BaseGbpV2Test(BaseGbpTest):
    """Base class for GBP V2 API tests."""

    # Use the GBP V2 Client Manager
    #client_manager = clients.ManagerV2

    @classmethod
    def skip_checks(cls):
        super(BaseGbpV2Test, cls).skip_checks()

        if not CONF.gbp_feature_enabled.api_v2:
            skip_msg = ("%s skipped as GBP v2 API is not available"
                        % cls.__name__)
            raise cls.skipException(skip_msg)
