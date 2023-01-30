# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: ele
#     language: python
#     name: python3
# ---

# DataJoint U24 - Workflow Volume
#

# ### Intro
#

# This notebook will describe the steps to use Element Volume for interacting with BossDB.
# Prior to using this notebook, please refer to documentation for
# [Element installation instructions](https://datajoint.com/docs/elements/user-guide/) and refer to [BossDB resources](https://www.youtube.com/watch?v=eVNr6Pzxoh8) for information on generating an account and configuring `intern`.
#
# Importantly, you'll need an `intern` config file, which should look like this:
#
# ```cfg
#     # ~/.intern/intern.cfg
#     [Default]
#     protocol = https
#     host = api.bossdb.io
#     token = <YOUR_TOKEN>
# ```
#

# +
import datajoint as dj
import os

if os.path.basename(os.getcwd()) == "notebooks":
    os.chdir("..")
dj.conn()

# +
dj.config["custom"]["database.prefix"] = "cbroz_wfboss_"
dj.config["custom"][
    "vol_root_data_dir"
] = "/Users/cb/Documents/data/U24_SampleData/boss/"
from workflow_volume.pipeline import volume, BossDBInterface

volume.Volume.delete_quick()
# -

# `BossDBInterface` works much like `intern.array`, but with additional functionality for managing records in your Element Volume schema. We can optionally link this dataset to a session in our pipeline via a session key.
#
# Note, however, that we'll have to change our notation slightly. Whereas we can directly index into a dataset to get slices, we'll need to either provide slices as a string or a tuple.
#

# ### Testing
#

data = BossDBInterface(
    "bossdb://takemura/takemura13/image", resolution=4, session_key={}
)

# Using `intern` notion, we can look at Z slice 300, from Y voxels 200-500, and X voxels 0 to 700.
#

data[300, 200:501, 0:701]

# The same data can be downloaded and loaded into Element Volume using either of the following commands.
#
# Without a session directory provided via `get_session_directory` in `workflow_volume.paths`, we will infer an output directory based on the BossDB path from `get_vol_root_data_dir`.
#

# data.download(slice_key=(300,slice(200,501),slice(0,701)))
data.download(slice_key="[300,200:501,0:701]")

# Our volume is stored in the `Volume`

volume.Volume()

# With `Slice` corresponding to slices

volume.Volume.Slice()

# Each BossDB resolution will have a unique entry in the `Resolution` table

volume.Resolution()

# And, the `Zoom` table retain information about the X/Y windows we use.

volume.Zoom()

# Changing any of these pieces of information would download different data.

data.download(slice_key=(slice(300, 311), slice(100, 401), slice(100, 401)))


