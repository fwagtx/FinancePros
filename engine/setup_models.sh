#!/usr/bin/env bash
# Download the free Kokoro voice model (Apache 2.0) into engine/models/
set -e; cd "$(dirname "$0")"; mkdir -p models
base=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -f models/kokoro-v1.0.onnx ] || curl -sL -o models/kokoro-v1.0.onnx $base/kokoro-v1.0.onnx
[ -f models/voices-v1.0.bin ] || curl -sL -o models/voices-v1.0.bin $base/voices-v1.0.bin
