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

from .response import Response


class ImageKnowledge(Response):
    """ImageKnowledge.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource. To use the URL,
     append query parameters as appropriate and include the
     Ocp-Apim-Subscription-Key header.
    :vartype read_link: str
    :ivar web_search_url: The URL to Bing's search result for this item.
    :vartype web_search_url: str
    :ivar tags: A list of visual search tags.
    :vartype tags:
     list[~azure.cognitiveservices.search.visualsearch.models.ImageTag]
    :ivar image: Image object containing metadata about the requested image.
    :vartype image:
     ~azure.cognitiveservices.search.visualsearch.models.ImageObject
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'tags': {'readonly': True},
        'image': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[ImageTag]'},
        'image': {'key': 'image', 'type': 'ImageObject'},
    }

    def __init__(self, **kwargs):
        super(ImageKnowledge, self).__init__(**kwargs)
        self.tags = None
        self.image = None
        self._type = 'ImageKnowledge'
