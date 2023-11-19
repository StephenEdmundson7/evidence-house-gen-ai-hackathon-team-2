import streamlit as st
# import networkx as nx
# import plotly.graph_objects as go
#import re

import os

import claude

product="Electric car"

os.environ["CLAUDE_API_KEY"] = "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"

assistant = claude.Assistant()

# Call assistant to get BOM
response = assistant.ask(
    f"Please provide the full bill of materials, including all sub-components, raw materials, and processing steps required to produce {product}. Present this as a dictionary of lists, with each key representing a top-level component or material, and the list containing its inputs/sub-components.")

print(response)

#
#
# def get_bom(product):
#     # Create Claude AI assistant
#     assistant = claude.Assistant()
#
#     # Call assistant to get BOM
#     response = assistant.ask(
#         f"Please provide the full bill of materials, including all sub-components, raw materials, and processing steps required to produce {product}. Present this as a dictionary of lists, with each key representing a top-level component or material, and the list containing its inputs/sub-components.")
#
#     # Extract BOM dictionary from Claude's response
#     bom_dict = extract_bom(response)
#
#     return bom_dict
#
#

#
# def extract_bom(claude_response):
#     bom_dict = {}
#
#     # Split response into lines
#     lines = claude_response.split('\n')
#
#     # Regex to match BOM component headers
#     comp_regex = r'^- (?P<component>\w+)$'
#
#     # Regex to match sub-component indent lines
#     sub_regex = r'^  - (?P<subcomponent>\w+)$'
#
#     current_component = None
#
#     for line in lines:
#         comp_match = re.match(comp_regex, line)
#         if comp_match:
#             # Found new component
#             current_component = comp_match.group('component')
#             bom_dict[current_component] = []
#             continue
#
#         sub_match = re.match(sub_regex, line)
#         if sub_match:
#             # Found sub-component under current component
#             subcomponent = sub_match.group('subcomponent')
#             bom_dict[current_component].append(subcomponent)
#
#     return bom_dict
#
#
# st.title('Bill of Materials Visualizer')
#
# product = st.text_input('Enter a product name:')
#
# if product:
#     # Call Claude AI to get BOM data
#     bom_data = get_bom(product)
#
#     # Create graph from BOM data
#     G = nx.from_dict_of_lists(bom_data)
#
#     # Draw graph with Plotly
#     fig = go.Figure(
#         data=[go.Sankey(
#             node=dict(
#                 pad=15,
#                 thickness=20,
#                 line=dict(color="black", width=0.5),
#                 label=list(G.nodes()),
#             ),
#             link=dict(
#                 source=list(G.edges())[:][0],
#                 target=list(G.edges())[:][1],
#                 value=[1] * len(list(G.edges()))
#             ))])
#
#     st.plotly_chart(fig)
#
# else:
#     st.write('Enter a product name to view its bill of materials')