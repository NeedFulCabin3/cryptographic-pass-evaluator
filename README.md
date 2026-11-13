# cryptographic-pass-evaluator

> Probabilistic Assessment of Passphrase Vulnerability Through Supervised Classification

---

## Overview

Evaluating credential security in local environments often introduces friction when developers rely on remote third-party APIs or brittle rule-based heuristics that generate high false-positive rates. **cryptographic-pass-evaluator** addresses this by providing a self-contained binary classification utility that runs entirely within the terminal. It translates raw passphrase strings into statistical feature vectors and applies logistic regression to categorize inputs as secure or vulnerable without transmitting data across external networks.

## How It Works

The system operates through a deterministic pipeline consisting of feature extraction, synthetic training data generation, model fitting, and real-time inference:

1. **Feature Extraction:** Incoming passphrases are parsed to extract numerical metrics: total string length, uppercase counts, lowercase counts, digit counts, and special character counts. Additionally, regular expression lookaheads scan for sequential numeric blocks (e.g., `123`) and repetitive character runs (e.g., `aaa`).
2. **Synthetic Training Distribution:** The program generates a curated baseline corpus of known vulnerable and secure passwords, converting each into identical feature vector representations.
3. **Classification Engine:** A supervised logistic regression estimator (`scikit-learn`) trains on this synthetic dataset to establish decision boundaries, calculating confidence probabilities for any arbitrary input string during interactive sessions.

## Key Features

* **Local Execution:** Zero external network calls or telemetry tracking, ensuring complete data privacy.
* **Deterministic Vectorization:** Consistent numerical representation of string characteristics for reliable model inference.
* **Interactive Terminal Interface:** Continuous evaluation loop with graceful handling of user interruptions and invalid inputs.
* **Clean Functional Design:** Minimalist architecture without unnecessary enterprise abstractions or wrapper boilerplate.

## Tech Stack & Core Dependencies Breakdown

* **Python 3.10+:** Core runtime environment utilizing standard library modules (`re`, `sys`).
* **`numpy` (`^1.20+`):** Handles efficient multi-dimensional array operations for feature vector matrices and numerical computations.
* **`scikit-learn` (`^1.0+`):** Implements the `LogisticRegression` binary classification algorithm and model fitting procedures.

## Environment & Web-Based Quick Start

### GitHub Codespaces
1. Open the repository in GitHub Codespaces.
2. Once the container initializes, install dependencies:
   ```bash
   pip install scikit-learn numpy
   ```
3. Run the evaluation script:
    ```bash
   python password_evaluator.py
   ```

### Local Virtual Environment (venv)
    ```bash
   python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install scikit-learn numpy
    python password_evaluator.py
   ```

## Repository Structure

```bash
cryptographic-pass-evaluator/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── password_evaluator.py
├── LICENSE
└── README.md
```

## Roadmap

**[ ] Type Annotations & Stubs:** Introduce comprehensive Python type hints (mypy-compliant) across all feature extraction functions.

**[ ] Asynchronous Batch Auditing:** Migrate single-line terminal inputs to support asynchronous batch file processing for auditing password lists.

**[ ] Optimized Feature Serialization:** Implement model persistence (joblib) to cache trained classification weights and eliminate startup training latency.