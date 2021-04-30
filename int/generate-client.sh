#!/usr/bin/env bash

cd "$(dirname "$0")" || exit

CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-docker}
IMAGE="openapitools/openapi-generator-cli"

${CONTAINER_RUNTIME} pull ${IMAGE}:latest

${CONTAINER_RUNTIME} run --rm \
    -v $PWD:/local:z \
    openapitools/openapi-generator-cli generate \
    -i /local/swagger.yaml \
    -g python \
    -o /local/acapy-client \
    --skip-validate-spec \
    --additional-properties=packageName=acapy_client

rm -rf --preserve-root ./acapy-client/docs
rm -rf --preserve-root ./acapy-client/test
