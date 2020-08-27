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

from enum import Enum


class DeploymentMode(str, Enum):

    incremental = "Incremental"
    complete = "Complete"


class OnErrorDeploymentType(str, Enum):

    last_successful = "LastSuccessful"
    specific_deployment = "SpecificDeployment"


class WhatIfResultFormat(str, Enum):

    resource_id_only = "ResourceIdOnly"
    full_resource_payloads = "FullResourcePayloads"


class AliasPathTokenType(str, Enum):

    not_specified = "NotSpecified"  #: The token type is not specified.
    any = "Any"  #: The token type can be anything.
    string = "String"  #: The token type is string.
    object_enum = "Object"  #: The token type is object.
    array = "Array"  #: The token type is array.
    integer = "Integer"  #: The token type is integer.
    number = "Number"  #: The token type is number.
    boolean = "Boolean"  #: The token type is boolean.


class AliasPathAttributes(str, Enum):

    none = "None"  #: The token that the alias path is referring to has no attributes.
    modifiable = "Modifiable"  #: The token that the alias path is referring to is modifiable by policies with 'modify' effect.


class AliasPatternType(str, Enum):

    not_specified = "NotSpecified"  #: NotSpecified is not allowed.
    extract = "Extract"  #: Extract is the only allowed value.


class AliasType(str, Enum):

    not_specified = "NotSpecified"  #: Alias type is unknown (same as not providing alias type).
    plain_text = "PlainText"  #: Alias value is not secret.
    mask = "Mask"  #: Alias value is secret.


class ProvisioningState(str, Enum):

    not_specified = "NotSpecified"
    accepted = "Accepted"
    running = "Running"
    ready = "Ready"
    creating = "Creating"
    created = "Created"
    deleting = "Deleting"
    deleted = "Deleted"
    canceled = "Canceled"
    failed = "Failed"
    succeeded = "Succeeded"
    updating = "Updating"


class ResourceIdentityType(str, Enum):

    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"
    system_assigned_user_assigned = "SystemAssigned, UserAssigned"
    none = "None"


class ProvisioningOperation(str, Enum):

    not_specified = "NotSpecified"  #: The provisioning operation is not specified.
    create = "Create"  #: The provisioning operation is create.
    delete = "Delete"  #: The provisioning operation is delete.
    waiting = "Waiting"  #: The provisioning operation is waiting.
    azure_async_operation_waiting = "AzureAsyncOperationWaiting"  #: The provisioning operation is waiting Azure async operation.
    resource_cache_waiting = "ResourceCacheWaiting"  #: The provisioning operation is waiting for resource cache.
    action = "Action"  #: The provisioning operation is action.
    read = "Read"  #: The provisioning operation is read.
    evaluate_deployment_output = "EvaluateDeploymentOutput"  #: The provisioning operation is evaluate output.
    deployment_cleanup = "DeploymentCleanup"  #: The provisioning operation is cleanup. This operation is part of the 'complete' mode deployment.


class PropertyChangeType(str, Enum):

    create = "Create"  #: The property does not exist in the current state but is present in the desired state. The property will be created when the deployment is executed.
    delete = "Delete"  #: The property exists in the current state and is missing from the desired state. It will be deleted when the deployment is executed.
    modify = "Modify"  #: The property exists in both current and desired state and is different. The value of the property will change when the deployment is executed.
    array = "Array"  #: The property is an array and contains nested changes.


class ChangeType(str, Enum):

    create = "Create"  #: The resource does not exist in the current state but is present in the desired state. The resource will be created when the deployment is executed.
    delete = "Delete"  #: The resource exists in the current state and is missing from the desired state. The resource will be deleted when the deployment is executed.
    ignore = "Ignore"  #: The resource exists in the current state and is missing from the desired state. The resource will not be deployed or modified when the deployment is executed.
    deploy = "Deploy"  #: The resource exists in the current state and the desired state and will be redeployed when the deployment is executed. The properties of the resource may or may not change.
    no_change = "NoChange"  #: The resource exists in the current state and the desired state and will be redeployed when the deployment is executed. The properties of the resource will not change.
    modify = "Modify"  #: The resource exists in the current state and the desired state and will be redeployed when the deployment is executed. The properties of the resource will change.


class TagsPatchOperation(str, Enum):

    replace = "Replace"  #: The 'replace' option replaces the entire set of existing tags with a new set.
    merge = "Merge"  #: The 'merge' option allows adding tags with new names and updating the values of tags with existing names.
    delete = "Delete"  #: The 'delete' option allows selectively deleting tags based on given names or name/value pairs.
