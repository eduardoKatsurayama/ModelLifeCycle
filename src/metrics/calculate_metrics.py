import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, roc_auc_score, f1_score
import mlflow
from optbinning.scorecard import plot_ks


def ks_score(y_test, target_col='y', proba_col='predict_proba'):
    df = y_test.sort_values(proba_col).copy()
    df = df.reset_index()

    df['cumulative_n_population'] = df.index + 1
    df['cumulative_n_good'] = df[target_col].cumsum()
    df['cumulative_n_bad'] = (
        df['cumulative_n_population'] - df[target_col].cumsum()
    )
    df['cumulative_perc_population'] = df['cumulative_n_population'] / (
        df.shape[0]
    )
    df['cumulative_perc_good'] = df['cumulative_n_good'] / df[target_col].sum()
    df['cumulative_perc_bad'] = df['cumulative_n_bad'] / (
        df.shape[0] - df[target_col].sum()
    )
    ks_score = max(df['cumulative_perc_bad'] - df['cumulative_perc_good'])

    return ks_score


def run_metrics(y_test, y_score, y_pred, y_proba):
    metrics = {
        'ks': ks_score(
            pd.DataFrame({'y': np.array(y_test), 'predict_proba': y_proba})
        ),
        'roc_auc': roc_auc_score(y_test, y_proba),
        'f1_score': f1_score(y_test, y_pred),
        'gini': 2 * roc_auc_score(y_test, y_proba) - 1,
        'r2': r2_score(y_test, y_proba)
    }
    mlflow.log_metrics(metrics)

    plot_ks(y_test, y_score, savefig=True, fname='ks.png')
    mlflow.log_artifact('ks.png')
