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


class X12FramingSettings(Model):
    """The X12 agreement framing settings.

    All required parameters must be populated in order to send to Azure.

    :param data_element_separator: Required. The data element separator.
    :type data_element_separator: int
    :param component_separator: Required. The component separator.
    :type component_separator: int
    :param replace_separators_in_payload: Required. The value indicating
     whether to replace separators in payload.
    :type replace_separators_in_payload: bool
    :param replace_character: Required. The replacement character.
    :type replace_character: int
    :param segment_terminator: Required. The segment terminator.
    :type segment_terminator: int
    :param character_set: Required. The X12 character set. Possible values
     include: 'NotSpecified', 'Basic', 'Extended', 'UTF8'
    :type character_set: str or ~azure.mgmt.logic.models.X12CharacterSet
    :param segment_terminator_suffix: Required. The segment terminator suffix.
     Possible values include: 'NotSpecified', 'None', 'CR', 'LF', 'CRLF'
    :type segment_terminator_suffix: str or
     ~azure.mgmt.logic.models.SegmentTerminatorSuffix
    """

    _validation = {
        'data_element_separator': {'required': True},
        'component_separator': {'required': True},
        'replace_separators_in_payload': {'required': True},
        'replace_character': {'required': True},
        'segment_terminator': {'required': True},
        'character_set': {'required': True},
        'segment_terminator_suffix': {'required': True},
    }

    _attribute_map = {
        'data_element_separator': {'key': 'dataElementSeparator', 'type': 'int'},
        'component_separator': {'key': 'componentSeparator', 'type': 'int'},
        'replace_separators_in_payload': {'key': 'replaceSeparatorsInPayload', 'type': 'bool'},
        'replace_character': {'key': 'replaceCharacter', 'type': 'int'},
        'segment_terminator': {'key': 'segmentTerminator', 'type': 'int'},
        'character_set': {'key': 'characterSet', 'type': 'str'},
        'segment_terminator_suffix': {'key': 'segmentTerminatorSuffix', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(X12FramingSettings, self).__init__(**kwargs)
        self.data_element_separator = kwargs.get('data_element_separator', None)
        self.component_separator = kwargs.get('component_separator', None)
        self.replace_separators_in_payload = kwargs.get('replace_separators_in_payload', None)
        self.replace_character = kwargs.get('replace_character', None)
        self.segment_terminator = kwargs.get('segment_terminator', None)
        self.character_set = kwargs.get('character_set', None)
        self.segment_terminator_suffix = kwargs.get('segment_terminator_suffix', None)
