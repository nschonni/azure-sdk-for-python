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

from msrest.serialization import Model


class TrackingEvent(Model):
    """TrackingEvent.

    All required parameters must be populated in order to send to Azure.

    :param event_level: Required. Possible values include: 'LogAlways',
     'Critical', 'Error', 'Warning', 'Informational', 'Verbose'
    :type event_level: str or ~azure.mgmt.logic.models.EventLevel
    :param event_time: Required.
    :type event_time: datetime
    :param record_type: Required. Possible values include: 'NotSpecified',
     'Custom', 'AS2Message', 'AS2MDN', 'X12Interchange', 'X12FunctionalGroup',
     'X12TransactionSet', 'X12InterchangeAcknowledgment',
     'X12FunctionalGroupAcknowledgment', 'X12TransactionSetAcknowledgment',
     'EdifactInterchange', 'EdifactFunctionalGroup', 'EdifactTransactionSet',
     'EdifactInterchangeAcknowledgment',
     'EdifactFunctionalGroupAcknowledgment',
     'EdifactTransactionSetAcknowledgment'
    :type record_type: str or ~azure.mgmt.logic.models.TrackingRecordType
    :param error:
    :type error: ~azure.mgmt.logic.models.TrackingEventErrorInfo
    """

    _validation = {
        'event_level': {'required': True},
        'event_time': {'required': True},
        'record_type': {'required': True},
    }

    _attribute_map = {
        'event_level': {'key': 'eventLevel', 'type': 'str'},
        'event_time': {'key': 'eventTime', 'type': 'iso-8601'},
        'record_type': {'key': 'recordType', 'type': 'str'},
        'error': {'key': 'error', 'type': 'TrackingEventErrorInfo'},
    }

    def __init__(self, **kwargs):
        super(TrackingEvent, self).__init__(**kwargs)
        self.event_level = kwargs.get('event_level', None)
        self.event_time = kwargs.get('event_time', None)
        self.record_type = kwargs.get('record_type', None)
        self.error = kwargs.get('error', None)
