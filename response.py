#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from google.cloud import dialogflowcx_v3beta1


def list_agents():
    # Create a client
    client = dialogflowcx_v3beta1.AgentsClient()

    # Initialize request argument(s)
    request = dialogflowcx_v3beta1.ListAgentsRequest(
        parent="projects/bot1-404120/locations/global",
    )

    # Make the request
    page_result = client.list_agents(request=request)

    # Handle the response
    for response in page_result:
        print(response)

# [END dialogflow_v3beta1_generated_Agents_ListAgents_sync]

list_agents()
