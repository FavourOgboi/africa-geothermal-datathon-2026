#!/usr/bin/env python3
"""
SPE Africa Geothermal Datathon 2026 — Team GeoLogic Analytics
Main execution script — runs the complete workflow end-to-end.

Usage:
    python main.py

This executes all three notebooks in sequence:
    01 → Geothermal Resource Assessment & Data Engineering
    02 → Integrated Energy System Design
    03 → Economic Analysis & Uncertainty
"""

import subprocess
import sys
import os
from pathlib import Path

NOTEBOOKS_DIR = Path(__file__).parent / 'notebooks'
NOTEBOOKS = [
    '01_geothermal_resource_assessment.ipynb',
    '02_integrated_energy_system_design.ipynb',
    '03_economic_and_ai_workflow.ipynb',
]


def run_notebook(notebook_path):
    """Execute a Jupyter notebook and save the output in place."""
    print(f"\n{'='*60}")
    print(f"Executing: {notebook_path.name}")
    print(f"{'='*60}")

    result = subprocess.run(
        [
            sys.executable, '-m', 'jupyter', 'nbconvert',
            '--to', 'notebook',
            '--execute',
            '--inplace',
            '--ExecutePreprocessor.timeout=300',
            str(notebook_path),
        ],
        capture_output=True,
        text=True,
        cwd=str(notebook_path.parent),
    )

    if result.returncode != 0:
        print(f"ERROR executing {notebook_path.name}:")
        print(result.stderr)
        return False

    print(f"SUCCESS: {notebook_path.name}")
    return True


def main():
    print("SPE Africa Geothermal Datathon 2026")
    print("Team GeoLogic Analytics — Full Pipeline Execution")
    print("=" * 60)

    # Verify notebooks exist
    for nb_name in NOTEBOOKS:
        nb_path = NOTEBOOKS_DIR / nb_name
        if not nb_path.exists():
            print(f"ERROR: Notebook not found: {nb_path}")
            sys.exit(1)

    # Execute in order
    success = True
    for nb_name in NOTEBOOKS:
        nb_path = NOTEBOOKS_DIR / nb_name
        if not run_notebook(nb_path):
            print(f"\nPipeline failed at: {nb_name}")
            success = False
            break

    if success:
        print(f"\n{'='*60}")
        print("PIPELINE COMPLETE — All notebooks executed successfully.")
        print("Outputs available in:")
        print("  data/processed/   — cleaned datasets")
        print("  outputs/figures/  — visualisations")
        print("  outputs/tables/   — summary tables")
        print(f"{'='*60}")
    else:
        print("\nTo run notebooks manually:")
        print("  cd notebooks/")
        print("  jupyter notebook")
        sys.exit(1)


if __name__ == '__main__':
    main()
