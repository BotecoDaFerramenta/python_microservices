set -e

#activate
source .venv/bin/activate
#run
uvicorn main.server:app --reload