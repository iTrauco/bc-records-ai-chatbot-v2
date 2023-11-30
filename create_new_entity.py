#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from google.cloud import dialogflowcx_v3


def create_entity_type():
    # Create a client
    client = dialogflowcx_v3.EntityTypesClient()

    # Initialize request argument(s)
    entity_type = dialogflowcx_v3.EntityType()
    entity_type.display_name = "test3"
    entity_type.kind = "KIND_MAP"

    request = dialogflowcx_v3.CreateEntityTypeRequest(
        parent="projects/bot1-404120/locations/global/agents/4a2fde83-decc-4656-8995-1cbc2e3eeab4",
        entity_type=entity_type,
    )

    # Make the request
    response = client.create_entity_type(request=request)

    # Handle the response
    print(response)

create_entity_type()
