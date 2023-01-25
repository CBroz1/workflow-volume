import datajoint as dj
from element_animal import subject
from element_animal.subject import Subject
from element_lab import lab
from element_session import session
from element_session.session_with_datetime import Session, SessionDirectory
from element_volume import volume

if "custom" not in dj.config:
    dj.config["custom"] = {}

db_prefix = dj.config["custom"].get("database.prefix", "")

__all__ = ["lab", "subject", "session", "Subject", "Session", "SessionDirectory"]

# Activate "lab", "subject", "session" schemas ---------------------------

lab.activate(db_prefix + "lab")

subject.activate(db_prefix + "subject", linking_module=__name__)

Experimenter = lab.User
session.activate(db_prefix + "session", linking_module=__name__)

volume.activate(db_prefix + "volume", linking_module=__name__)
