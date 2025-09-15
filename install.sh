set -e

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

uv pip install -r requirements.txt
