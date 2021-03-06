# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AcquisitionOperation(Model):
    """AcquisitionOperation.

    :param operation_state: State of the the AcquisitionOperation for the current user
    :type operation_state: object
    :param operation_type: AcquisitionOperationType: install, request, buy, etc...
    :type operation_type: object
    :param reason: Optional reason to justify current state. Typically used with Disallow state.
    :type reason: str
    :param reasons: List of reasons indicating why the operation is not allowed.
    :type reasons: list of :class:`AcquisitionOperationDisallowReason <extension-management.v4_0.models.AcquisitionOperationDisallowReason>`
    """

    _attribute_map = {
        'operation_state': {'key': 'operationState', 'type': 'object'},
        'operation_type': {'key': 'operationType', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'str'},
        'reasons': {'key': 'reasons', 'type': '[AcquisitionOperationDisallowReason]'}
    }

    def __init__(self, operation_state=None, operation_type=None, reason=None, reasons=None):
        super(AcquisitionOperation, self).__init__()
        self.operation_state = operation_state
        self.operation_type = operation_type
        self.reason = reason
        self.reasons = reasons
