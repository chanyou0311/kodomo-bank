#!/bin/bash

set -x

for file in `\find k8s -maxdepth 1 -type f`; do
    if echo $file | grep ingress; then
        echo 'ingress pass'
    elif echo $file | grep tls; then
        echo 'tls pass'
    elif echo $file | grep svc; then
        echo 'service pass'
    elif echo $file | grep daemonset; then
        echo 'daemonset pass'
    elif echo $file | grep cronjob; then
        echo 'cronjob pass'
    else
        kubectl rollout status -f $file
    fi
done
