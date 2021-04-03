#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get(
        "QnAKnowledgebaseId", "febe3ecf-89d1-4f49-b408-d23bab02d35b")
    QNA_ENDPOINT_KEY = os.environ.get(
        "QnAEndpointKey", "d4b21ea1-c1c6-4dfb-87a8-c9746bb6f74e")
    QNA_ENDPOINT_HOST = os.environ.get(
        "QnAEndpointHostName", "https://echobotsampleproject.azurewebsites.net/qnamaker")
