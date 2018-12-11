#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

SCRIPT_ROOT=$(dirname ${BASH_SOURCE})/..

cd ${SCRIPT_ROOT}
python3 ./hack/generate-resource-readme.py
cd - > /dev/null
