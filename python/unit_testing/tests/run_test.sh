PYTHONPATH="$(git rev-parse --show-toplevel)/python"
export PYTHONPATH

echo "${PYTHONPATH}"

pytest ./*.py

