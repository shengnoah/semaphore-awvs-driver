#!/usr/bin/env bash
dot arch.dot -T png -o arch.png
mmdc -i sequence.mermaid  -o sequence.png
