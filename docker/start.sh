#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset
 
uvicorn api_project.composites.api:app --host 0.0.0.0 --reload
