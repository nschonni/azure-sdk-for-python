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


class X12DelimiterOverrides(Model):
    """The X12 delimiter override settings.

    All required parameters must be populated in order to send to Azure.

    :param protocol_version: The protocol version.
    :type protocol_version: str
    :param message_id: The message id.
    :type message_id: str
    :param data_element_separator: Required. The data element separator.
    :type data_element_separator: int
    :param component_separator: Required. The component separator.
    :type component_separator: int
    :param segment_terminator: Required. The segment terminator.
    :type segment_terminator: int
    :param segment_terminator_suffix: Required. The segment terminator suffix.
     Possible values include: 'NotSpecified', 'None', 'CR', 'LF', 'CRLF'
    :type segment_terminator_suffix: str or
     ~azure.mgmt.logic.models.SegmentTerminatorSuffix
    :param replace_character: Required. The replacement character.
    :type replace_character: int
    :param replace_separators_in_payload: Required. The value indicating
     whether to replace separators in payload.
    :type replace_separators_in_payload: bool
    :param target_namespace: The target namespace on which this delimiter
     settings has to be applied.
    :type target_namespace: str
    """

    _validation = {
        'data_element_separator': {'required': True},
        'component_separator': {'required': True},
        'segment_terminator': {'required': True},
        'segment_terminator_suffix': {'required': True},
        'replace_character': {'required': True},
        'replace_separators_in_payload': {'required': True},
    }

    _attribute_map = {
        'protocol_version': {'key': 'protocolVersion', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'data_element_separator': {'key': 'dataElementSeparator', 'type': 'int'},
        'component_separator': {'key': 'componentSeparator', 'type': 'int'},
        'segment_terminator': {'key': 'segmentTerminator', 'type': 'int'},
        'segment_terminator_suffix': {'key': 'segmentTerminatorSuffix', 'type': 'str'},
        'replace_character': {'key': 'replaceCharacter', 'type': 'int'},
        'replace_separators_in_payload': {'key': 'replaceSeparatorsInPayload', 'type': 'bool'},
        'target_namespace': {'key': 'targetNamespace', 'type': 'str'},
    }

    def __init__(self, *, data_element_separator: int, component_separator: int, segment_terminator: int, segment_terminator_suffix, replace_character: int, replace_separators_in_payload: bool, protocol_version: str=None, message_id: str=None, target_namespace: str=None, **kwargs) -> None:
        super(X12DelimiterOverrides, self).__init__(**kwargs)
        self.protocol_version = protocol_version
        self.message_id = message_id
        self.data_element_separator = data_element_separator
        self.component_separator = component_separator
        self.segment_terminator = segment_terminator
        self.segment_terminator_suffix = segment_terminator_suffix
        self.replace_character = replace_character
        self.replace_separators_in_payload = replace_separators_in_payload
        self.target_namespace = target_namespace
