import datajoint as dj
from element_animal import subject
from element_animal.subject import Subject
from element_lab import lab
from element_lab.lab import Lab, Project, Protocol, Source, User
from element_session import session
from element_session.session_with_datetime import Session, SessionDirectory
from element_volume import volume
from element_volume.readers.bossdb import BossDBInterface

from .paths import get_session_directory, get_vol_root_data_dir

if "custom" not in dj.config:
    dj.config["custom"] = {}

db_prefix = dj.config["custom"].get("database.prefix", "")

__all__ = [
    "lab",
    "subject",
    "session",
    "Lab",
    "Source",
    "Subject",
    "Project",
    "Protocol",
    "User",
    "Session",
    "SessionDirectory",
    "BossDBInterface",
    "get_session_directory",
    "get_vol_root_data_dir",
]

# Activate "lab", "subject", "session" schemas ---------------------------

lab.activate(db_prefix + "lab")

subject.activate(db_prefix + "subject", linking_module=__name__)

Experimenter = lab.User
session.activate(db_prefix + "session", linking_module=__name__)

volume.activate(db_prefix + "volume", linking_module=__name__)
