import csv
from pathlib import Path
import pandas as pd


def get_header(file_path: str | Path) -> list[list[str]]:
    header: list[list[str]] = []
    with Path(file_path).open() as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            header.append(row)
            if row[0] == "[Data]":
                break
    return header


def get_data(file_path: str | Path) -> pd.DataFrame:
    file_path = Path(file_path)
    skip_rows = len(get_header(file_path))
    df = pd.read_csv(file_path, sep="\t", skiprows=skip_rows)
    # for unknown reasons, some .dat files parse incorrectly with sep="\t"
    # the incorrectly parsed df has only one column
    if df.shape[1] == 1:
        df = pd.read_csv(file_path, skiprows=skip_rows)
    return df


def measurement_type(df: pd.DataFrame) -> str:
    meas_type = ""
    if df["Moment (emu)"].notna().all():
        meas_type = "VSM"
    elif df["DC Moment Free Ctr (emu)"].notna().all():
        meas_type = "DC"
    return meas_type


def simplify_magnetic_df(df: pd.DataFrame) -> pd.DataFrame:
    new_df = pd.DataFrame()
    new_df["time"] = df["Time Stamp (sec)"] - df["Time Stamp (sec)"].min()
    new_df["temp"] = df["Temperature (K)"]
    new_df["field"] = df["Magnetic Field (Oe)"]
    meas_type = measurement_type(df)
    if meas_type == "VSM":
        new_df["moment"] = df["Moment (emu)"]
        new_df["moment_err"] = df["M. Std. Err. (emu)"]
    elif meas_type == "DC":
        new_df["moment"] = df["DC Moment Free Ctr (emu)"]
        new_df["moment_err"] = df["DC Moment Err Free Ctr (emu)"]
    return new_df


def magnetic_df(file_path: str | Path) -> pd.DataFrame:
    df = get_data(file_path)
    return simplify_magnetic_df(df)
