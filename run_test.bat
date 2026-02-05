@echo off
REM Quick test script for Windows
REM This script tests the title case agent

echo Creating test environment...
cd /d %~dp0

echo.
echo Running title case agent on sample file...
python agent\title_case_agent.py examples\sample.html examples\output.html

echo.
echo Conversion complete! Check examples\output.html
echo.
pause
