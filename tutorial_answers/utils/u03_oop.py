import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


def label_clusters(
    vals: pd.Series, eps: float = 0.001, min_samples: int = 10
) -> np.ndarray:
    """For determining the nominal values of data in a series containing one or more
    nominal values with some noise.

    Parameters
    ----------
    vals : pd.Series
        A series of data containing one or more nominal values with some noise.
    eps : float, optional
        Passed to `sklearn.cluster.DBSCAN()`. The maximum distance between two samples
        for one to be considered as in the neighborhood of the other, by default 0.001.
    min_samples : int, optional
        Passed to `sklearn.cluster.DBSCAN()`. The number of samples in a neighborhood
        for a point to be considered as a core point, by default 10.

    Returns
    -------
    np.ndarray
        An array of the same size as `vals` which contains the cluster labels for each
        element in `vals`. Noisy samples are given the label -1. A `vals` series
        containing, for example, one nominal temperature with noise should return an
        array with only one cluster label of -1.

    """
    reshaped_vals = vals.values.reshape(-1, 1)
    scaler = StandardScaler()
    reshaped_normalized_vals = scaler.fit_transform(reshaped_vals)
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    cluster_labels = dbscan.fit_predict(reshaped_normalized_vals)
    return cluster_labels


def unique_values(
    x: pd.Series, eps: float = 0.001, min_samples: int = 10
) -> list[float]:
    """Given a series of data containing one or more nominal values with some noise,
    returns a list of the nominal values.

    Parameters
    ----------
    x : pd.Series
        A series of data containing one or more nominal values with some noise.
    eps : float, optional
        Passed to `sklearn.cluster.DBSCAN()`. The maximum distance between two samples
        for one to be considered as in the neighborhood of the other, by default 0.001.
    min_samples : int, optional
        Passed to `sklearn.cluster.DBSCAN()`. The number of samples in a neighborhood
        for a point to be considered as a core point, by default 10.

    Returns
    -------
    list[float]
        The nominal values in `x` with the noise removed.
    """
    cluster_labels = label_clusters(x, eps=eps, min_samples=min_samples)
    unique_values = []
    for i in np.unique(cluster_labels):
        # average the values in each cluster
        unique_val = np.mean(x[cluster_labels == i])
        unique_val = round(unique_val, 1)
        unique_values.append(unique_val)
    return unique_values


def find_outlier_indices(x: pd.Series, threshold: float = 3) -> list[int]:
    """Finds the indices of outliers in a series of data.

    Parameters
    ----------
    x : pd.Series
        A series of data.
    threshold : float, optional
        The number of standard deviations from the mean to consider a value an outlier,
        by default 3.

    Returns
    -------
    list[int]
        The indices of the outliers in `x`.
    """
    z_scores = (x - x.mean()) / x.std()
    outliers = z_scores.abs() > threshold
    return list(outliers[outliers].index)


def find_temp_turnaround_point(df: pd.DataFrame) -> int:
    """Finds the index of the temperature turnaround point in a dataframe of
    a ZFCFC experiment which includes a column "Temperature (K)". Can handle two cases
    in which a single dataframe contains first a ZFC experiment, then a FC experiment.
    Case 1: ZFC temperature monotonically increases, then FC temperature monotonically
    decreases. Case 2: ZFC temperature monotonically increases, the temperature is
    reset to a lower value, then FC temperature monotonically increases.

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe of a ZFCFC experiment which includes a column "Temperature (K)".

    Returns
    -------
    int
        The index of the temperature turnaround point.

    """
    outlier_indices = find_outlier_indices(df["Temperature (K)"].diff())
    if len(outlier_indices) == 0:
        # zfc temp increases, fc temp decreases
        zero_point = abs(df["Temperature (K)"].iloc[20:-20].diff()).idxmin()
        return zero_point
    else:
        # zfc temp increases, reset temp, fc temp increases
        return outlier_indices[0]
