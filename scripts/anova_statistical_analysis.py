import numpy as np
import pandas as pd
from scipy import stats


def run_roughness_anova():
    df = pd.read_csv("data/raw/surface_roughness_raw.csv")
    groups = [
        df["control"],
        df["treatment_a"],
        df["treatment_b"],
        df["treatment_c"],
        df["treatment_d"],
        df["treatment_e"],
    ]
    f_stat, p_val = stats.f_oneway(*groups)
    print(f"Roughness ANOVA: F = {f_stat:.2f}, p = {p_val:.4e}")

    # Cohen's d: Control vs Treatment E
    c = df["control"].values
    e = df["treatment_e"].values
    pooled_sd = np.sqrt(
        ((len(c) - 1) * np.var(c, ddof=1) + (len(e) - 1) * np.var(e, ddof=1))
        / (len(c) + len(e) - 2)
    )
    d = (np.mean(c) - np.mean(e)) / pooled_sd
    print(f"Cohen's d (Control vs E): {d:.2f}")


if __name__ == "__main__":
    run_roughness_anova()
