# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import PolicyClientConfiguration



class PolicyClient(MultiApiClientMixin, SDKClient):
    """To manage and control access to your resources, you can define customized policies and assign them at a scope.

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: PolicyClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2019-09-01'
    _PROFILE_TAG = "azure.mgmt.resource.policy.PolicyClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = PolicyClientConfiguration(credentials, subscription_id, base_url)
        super(PolicyClient, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-10-01-preview: :mod:`v2015_10_01_preview.models<azure.mgmt.resource.policy.v2015_10_01_preview.models>`
           * 2016-04-01: :mod:`v2016_04_01.models<azure.mgmt.resource.policy.v2016_04_01.models>`
           * 2016-12-01: :mod:`v2016_12_01.models<azure.mgmt.resource.policy.v2016_12_01.models>`
           * 2017-06-01-preview: :mod:`v2017_06_01_preview.models<azure.mgmt.resource.policy.v2017_06_01_preview.models>`
           * 2018-03-01: :mod:`v2018_03_01.models<azure.mgmt.resource.policy.v2018_03_01.models>`
           * 2018-05-01: :mod:`v2018_05_01.models<azure.mgmt.resource.policy.v2018_05_01.models>`
           * 2019-01-01: :mod:`v2019_01_01.models<azure.mgmt.resource.policy.v2019_01_01.models>`
           * 2019-06-01: :mod:`v2019_06_01.models<azure.mgmt.resource.policy.v2019_06_01.models>`
           * 2019-09-01: :mod:`v2019_09_01.models<azure.mgmt.resource.policy.v2019_09_01.models>`
        """
        if api_version == '2015-10-01-preview':
            from .v2015_10_01_preview import models
            return models
        elif api_version == '2016-04-01':
            from .v2016_04_01 import models
            return models
        elif api_version == '2016-12-01':
            from .v2016_12_01 import models
            return models
        elif api_version == '2017-06-01-preview':
            from .v2017_06_01_preview import models
            return models
        elif api_version == '2018-03-01':
            from .v2018_03_01 import models
            return models
        elif api_version == '2018-05-01':
            from .v2018_05_01 import models
            return models
        elif api_version == '2019-01-01':
            from .v2019_01_01 import models
            return models
        elif api_version == '2019-06-01':
            from .v2019_06_01 import models
            return models
        elif api_version == '2019-09-01':
            from .v2019_09_01 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def policy_assignments(self):
        """Instance depends on the API version:

           * 2015-10-01-preview: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2015_10_01_preview.operations.PolicyAssignmentsOperations>`
           * 2016-04-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2016_04_01.operations.PolicyAssignmentsOperations>`
           * 2016-12-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2016_12_01.operations.PolicyAssignmentsOperations>`
           * 2017-06-01-preview: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2017_06_01_preview.operations.PolicyAssignmentsOperations>`
           * 2018-03-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2018_03_01.operations.PolicyAssignmentsOperations>`
           * 2018-05-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2018_05_01.operations.PolicyAssignmentsOperations>`
           * 2019-01-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2019_01_01.operations.PolicyAssignmentsOperations>`
           * 2019-06-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2019_06_01.operations.PolicyAssignmentsOperations>`
           * 2019-09-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2019_09_01.operations.PolicyAssignmentsOperations>`
        """
        api_version = self._get_api_version('policy_assignments')
        if api_version == '2015-10-01-preview':
            from .v2015_10_01_preview.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2016-04-01':
            from .v2016_04_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2016-12-01':
            from .v2016_12_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2017-06-01-preview':
            from .v2017_06_01_preview.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2018-03-01':
            from .v2018_03_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2019-01-01':
            from .v2019_01_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2019-06-01':
            from .v2019_06_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import PolicyAssignmentsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_definitions(self):
        """Instance depends on the API version:

           * 2015-10-01-preview: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2015_10_01_preview.operations.PolicyDefinitionsOperations>`
           * 2016-04-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2016_04_01.operations.PolicyDefinitionsOperations>`
           * 2016-12-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2016_12_01.operations.PolicyDefinitionsOperations>`
           * 2017-06-01-preview: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2017_06_01_preview.operations.PolicyDefinitionsOperations>`
           * 2018-03-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2018_03_01.operations.PolicyDefinitionsOperations>`
           * 2018-05-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2018_05_01.operations.PolicyDefinitionsOperations>`
           * 2019-01-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2019_01_01.operations.PolicyDefinitionsOperations>`
           * 2019-06-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2019_06_01.operations.PolicyDefinitionsOperations>`
           * 2019-09-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2019_09_01.operations.PolicyDefinitionsOperations>`
        """
        api_version = self._get_api_version('policy_definitions')
        if api_version == '2015-10-01-preview':
            from .v2015_10_01_preview.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2016-04-01':
            from .v2016_04_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2016-12-01':
            from .v2016_12_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2017-06-01-preview':
            from .v2017_06_01_preview.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2018-03-01':
            from .v2018_03_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2019-01-01':
            from .v2019_01_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2019-06-01':
            from .v2019_06_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import PolicyDefinitionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_set_definitions(self):
        """Instance depends on the API version:

           * 2017-06-01-preview: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2017_06_01_preview.operations.PolicySetDefinitionsOperations>`
           * 2018-03-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2018_03_01.operations.PolicySetDefinitionsOperations>`
           * 2018-05-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2018_05_01.operations.PolicySetDefinitionsOperations>`
           * 2019-01-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2019_01_01.operations.PolicySetDefinitionsOperations>`
           * 2019-06-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2019_06_01.operations.PolicySetDefinitionsOperations>`
           * 2019-09-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2019_09_01.operations.PolicySetDefinitionsOperations>`
        """
        api_version = self._get_api_version('policy_set_definitions')
        if api_version == '2017-06-01-preview':
            from .v2017_06_01_preview.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2018-03-01':
            from .v2018_03_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2019-01-01':
            from .v2019_01_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2019-06-01':
            from .v2019_06_01.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import PolicySetDefinitionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
