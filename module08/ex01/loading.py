import sys
import importlib


REQUIRED = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computations",
    "matplotlib": "Visualization",
    "requests": "Network access",
}


def check_dependencies() -> dict:
    """Check which packages are available and return their versions."""
    status = {}
    for pkg, desc in REQUIRED.items():
        try:
            mod = importlib.import_module(pkg)
            version = getattr(mod, "__version__", "unknown")
            status[pkg] = {"ok": True, "version": version, "desc": desc}
        except ImportError:
            status[pkg] = {"ok": False, "version": None, "desc": desc}
    return status


def show_status(status: dict) -> bool:
    """Display dependency status. Returns True if all OK."""
    all_ok = True
    for pkg, info in status.items():
        if info["ok"]:
            print(f"  [OK] {pkg} ({info['version']}) - {info['desc']} ready")
        else:
            print(f"  [MISSING] {pkg} - {info['desc']} NOT available")
            all_ok = False
    return all_ok


def run_analysis():
    """Run the Matrix data analysis using the loaded packages."""
    import pandas as pd
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    np.random.seed(42)
    n = 1000
    print(f"Processing {n} data points...")

    data = pd.DataFrame({
        "timestamp": pd.date_range("2026-01-01", periods=n, freq="h"),
        "signal": np.random.randn(n).cumsum(),
        "anomaly": np.random.choice([0, 1], size=n, p=[0.95, 0.05]),
    })

    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data["timestamp"], data["signal"], linewidth=0.8)
    anomalies = data[data["anomaly"] == 1]
    ax.scatter(anomalies["timestamp"], anomalies["signal"],
               color="red", s=15, label="Anomaly")
    ax.set_title("Matrix Signal Analysis")
    ax.set_xlabel("Time")
    ax.set_ylabel("Signal Strength")
    ax.legend()
    fig.tight_layout()
    fig.savefig("matrix_analysis.png")
    plt.close(fig)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    status = check_dependencies()
    all_ok = show_status(status)

    if not all_ok:
        print("\nSome dependencies are missing!")
        print("Install with pip:")
        print("  pip install -r requirements.txt")
        print("Or with Poetry:")
        print("  poetry install")
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
