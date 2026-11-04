# Reprofy Demo Shop

A small synthetic storefront for demonstrating Reprofy's customer-report workflow. It contains no real customers, orders, or payment processing.

## Demo scenario

This project intentionally starts with a tax-rounding bug. For three items priced at $0.10 each, the receipt rounds tax per line and shows $0.03, while checkout aggregates the unrounded tax and shows $0.02. Report the mismatch through **Report an issue**; Reprofy can create a reproduction, propose a fix, and prepare it on a separate Git branch for review.

The project is an early Python prototype. Checkout is for demonstration only and does not collect payment information.

## Run the storefront

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev,web]'
cp .env.example .env
```

Set `REPROFY_API_URL` and `REPROFY_API_TOKEN` in `.env` to the local Reprofy intake API, then run:

```bash
python -m uvicorn demo_app:app --host 127.0.0.1 --port 8000
```

Open <http://127.0.0.1:8000/catalog>, choose **Preview checkout**, then use **Report an issue** to submit the mismatch. The form sends reports only to the local Reprofy API configured by `REPROFY_API_URL`.

## Reprofy project

This repository includes `reprofy.yaml` and the source project. Clone it locally, configure your Reprofy model credentials and intake API, then initialize or open this folder in the Reprofy CLI. Keep `.env` and `.reprofy/` local; they are excluded from Git. Set the project to automatic mode only when the Reprofy worker is running.

The intentionally seeded issue is part of the demo baseline. Reprofy's proposed fix should be reviewed before merging the generated branch or pull request.
