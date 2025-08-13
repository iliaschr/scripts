@echo off
REM ===== Setup Logs Folder =====
if not exist logs (
    mkdir logs
)

:menu
cls
echo ==== My Tool Menu ====
echo 1. Ping a list of hosts
echo 2. Backup a folder
echo 3. Show system info
echo 4. Exit
set /p choice=Enter your choice: 

REM ===== Option 1: Ping Hosts =====
if "%choice%"=="1" (
    set "today=%date:/=-%"
    set "now=%time::=-%"
    set "now=%now: =0%"
    set "logfile=logs\ping_%today%_%now%.txt"

    echo ==== Ping Results on %today% %now% ==== > "%logfile%"
    for /f %%l in (link.txt) do (
        ping -n 1 %%l >nul
        if errorlevel 1 (
            echo %%l is NOT reachable.
            echo %%l is NOT reachable. >> "%logfile%"
        ) else (
            echo %%l is reachable.
            echo %%l is reachable. >> "%logfile%"
        )
    )
    echo Results saved to %logfile%
    pause
    goto menu
)

REM ===== Option 2: Backup Folder =====
if "%choice%"=="2" (
    set /p FOLDER=Enter the folder path: 
    set "today=%date:/=-%"
    set "now=%time::=-%"
    set "now=%now: =0%"
    set "logfile=logs\backup_%today%_%now%.txt"

    mkdir "Backup_%today%_%now%"
    echo ==== Backup Log on %today% %now% ==== > "%logfile%"
    echo Backing up "%FOLDER%" to "Backup_%today%_%now%\" >> "%logfile%"

    xcopy "%FOLDER%" "Backup_%today%_%now%\" /E /I /Y >> "%logfile%"
    echo Backup completed. >> "%logfile%"

    echo Backup completed. Log saved to %logfile%
    pause
    goto menu
)

REM ===== Option 3: System Info =====
if "%choice%"=="3" (
    set "today=%date:/=-%"
    set "now=%time::=-%"
    set "now=%now: =0%"
    set "logfile=logs\sysinfo_%today%_%now%.txt"

    echo ==== System Info on %today% %now% ==== > "%logfile%"
    echo Date: %today% >> "%logfile%"
    echo Time: %now% >> "%logfile%"

    echo Uptime: >> "%logfile%"
    systeminfo | find "System Boot Time" >> "%logfile%"

    echo IP Addresses: >> "%logfile%"
    ipconfig | find "IPv4 Address" >> "%logfile%"

    type "%logfile%"
    echo Log saved to %logfile%
    pause
    goto menu
)

REM ===== Option 4: Exit =====
if "%choice%"=="4" (
    exit
)

goto menu
