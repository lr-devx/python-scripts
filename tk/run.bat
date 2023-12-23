@echo off

where python3 > nul 2>&1
if %errorlevel% == 0 (
    set pythonCommand=python3
) else (
    where python > nul 2>&1
    if %errorlevel% == 0 (
        set pythonCommand=python
    ) else (
        echo "Python3 doesn't seem to be installed"
        exit /b 1
    )
)

%pythonCommand% -m pip install -r requirements.txt
%pythonCommand% tk_main.py