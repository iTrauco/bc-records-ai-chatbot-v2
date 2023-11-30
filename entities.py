#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from google.cloud import dialogflowcx_v3


def list_entity_types():
    # Create a client
    client = dialogflowcx_v3.EntityTypesClient()

    # Initialize request argument(s)
    request = dialogflowcx_v3.ListEntityTypesRequest(
        parent="projects/bot1-404120/locations/global/agents/4a2fde83-decc-4656-8995-1cbc2e3eeab4",
    )

    # Make the request
    page_result = client.list_entity_types(request=request)

    # Handle the response
    for response in page_result:
        print(response)

list_entity_types()
