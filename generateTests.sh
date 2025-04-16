#!/bin/bash

PROJECT_DIR="demo"
SRC_DIR="${PROJECT_DIR}/src"
OUTPUT_DIR="${PROJECT_DIR}/tests"

MODULES=("algorithms" "data_structures" "inventory")

mkdir -p "$OUTPUT_DIR"

VERBOSE=""
if [[ "$1" == "-v" ]]; then
  VERBOSE="-v"
  echo "Verbose mode enabled"
fi

echo "Starting Pynguin test generation for all modules..."

for module in "${MODULES[@]}"; do
    echo "Processing module: $module"
    
    MODULE_OUTPUT_DIR="${OUTPUT_DIR}/${module}"
    mkdir -p "$MODULE_OUTPUT_DIR"
    
    
    pynguin \
        $VERBOSE \
        --project-path "$PROJECT_DIR" \
        --output-path "$MODULE_OUTPUT_DIR" \
        --module-name "src.$module" \
        --assertion-generation=SIMPLE \
        --algorithm DYNAMOSA \
        --seed 42
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully generated tests for $module"
    else
        echo "❌ Failed to generate tests for $module"
    fi
    
    echo "-------------------------------------------"
done

echo "Test generation complete! Tests are available in $OUTPUT_DIR"
