@echo off
setlocal enabledelayedexpansion

REM Set the project root directory
set "PROJECT_DIR=demo"
set "SRC_DIR=%PROJECT_DIR%\src"
set "OUTPUT_DIR=%PROJECT_DIR%\tests"

REM List of modules to process
set MODULES=algorithms inventory data_structures

REM Optional verbose flag (-v)
set "VERBOSE="
if "%1"=="-v" (
    set "VERBOSE=-v"
    echo Verbose mode enabled
)

REM Create output directory
if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
)

echo Starting Pynguin test generation for all modules...

for %%M in (%MODULES%) do (
    echo Processing module: %%M

    set "MODULE_OUTPUT_DIR=%OUTPUT_DIR%\%%M"
    if not exist "!MODULE_OUTPUT_DIR!" (
        mkdir "!MODULE_OUTPUT_DIR!"
    )

    pynguin %VERBOSE% ^
        --project-path "%PROJECT_DIR%" ^
        --output-path "!MODULE_OUTPUT_DIR!" ^
        --module-name "src.%%M" ^
        --assertion-generation=SIMPLE ^
        --algorithm DYNAMOSA ^
        --seed 42

    if !errorlevel! EQU 0 (
        echo ✅ Successfully generated tests for %%M
    ) else (
        echo ❌ Failed to generate tests for %%M
    )

    echo -------------------------------------------
)

echo Test generation complete! Tests are available in %OUTPUT_DIR%

endlocal

