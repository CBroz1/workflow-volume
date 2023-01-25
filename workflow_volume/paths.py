from typing import List, Union

import datajoint as dj


def get_session_directory(session_key: dict) -> str:
    """Return relative path from SessionDirectory table given key

    Args:
        session_key (dict): Key uniquely identifying a session

    Returns:
        path (str): Relative path of session directory
    """
    from .pipeline import session

    session_dir = (session.SessionDirectory & session_key).fetch1("session_dir")
    return session_dir


def get_vol_root_data_dir() -> Union[str, List[str]]:
    """Return root directory for ephys from 'vol_root_data_dir' in dj.config

    Returns:
        path (any): List of path(s) if available or None
    """
    return dj.config.get("custom", {}).get("vol_root_data_dir", None)
