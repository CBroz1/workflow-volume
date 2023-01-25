from element_interface.utils import ingest_csv_to_table

from .pipeline import session


def ingest_sessions(
    session_csv_path: str = "./user_data/session/sessions.csv",
    skip_duplicates: bool = True,
    verbose: bool = True,
):
    """
    Inserts data from a sessions csv into corresponding session schema tables
    By default, uses data from workflow_session/user_data/session/
        session_csv_path (str):     relative path of session csv
        skip_duplicates (bool): Default True. See DataJoint `insert` function
        verbose (bool): Print number inserted (i.e., table length change)
    """
    csvs = [
        session_csv_path,
        session_csv_path,
        session_csv_path,
        session_csv_path,
        session_csv_path,
    ]
    tables = [
        session.Session(),
        session.SessionDirectory(),
    ]

    ingest_csv_to_table(csvs, tables, skip_duplicates=skip_duplicates, verbose=verbose)


if __name__ == "__main__":
    ingest_sessions()
