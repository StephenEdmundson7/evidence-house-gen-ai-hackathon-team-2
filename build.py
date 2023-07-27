# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3.9
#     language: python
#     name: py39
# ---

# %% [markdown]
# # Build app

# %%
# instance = !echo $JUPYTERHUB_SERVICE_PREFIX
"https://data.cma.gov.uk" + instance[0] + "proxy/" + "8080/"

# %%
# !streamlit run app.py --server.port 8080
