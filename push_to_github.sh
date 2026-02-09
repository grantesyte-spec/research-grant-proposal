#!/bin/bash
set -euo pipefail

echo "Pushing to GitHub..."
cd "$(dirname "$0")"
git push origin main

echo "Done."
