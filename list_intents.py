#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from google.cloud import dialogflowcx_v3


def list_intents():
    # Create a client
    client = dialogflowcx_v3.IntentsClient()

    # Initialize request argument(s)
    request = dialogflowcx_v3.ListIntentsRequest(
        parent="projects/bot1-404120/locations/global/agents/79c5a35e-32a9-403b-ad36-d24f4f7d5d67",
    )

    # Make the request
    page_result = client.list_intents(request=request)

    # Handle the response
    for response in page_result:
        print(response)
list_intents()
