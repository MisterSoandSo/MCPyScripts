@echo off
title MC Server
rem Define max reboot attempt variables
set max_attempts=10
set timeout_seconds=10
set count=0
set last_attempt_time=


:start
color 0A
echo Loading Server ...
java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.19.2-43.2.6/win_args.txt nogui
cls


rem Rebooting Server after 10 seconds. 
rem If max_attempts reached before 1 hour then human intervention needed.

cls
if %count% geq 1 goto check_attempt

:reboot
color 0E
if %count% equ %max_attempts% goto end
echo Reboot Atempt: %count% 
echo Server Rebooting ... Press Ctrl+C to abort script.
TIMEOUT /T %timeout_seconds%
set /a count+=1
set last_attempt_time=%time%
cls
goto start

rem If no reboot attempts occur within the hour, reset count
:check_attempt
set current_time=%time%
set /a time_diff=(%current_time:~0,2% - %last_attempt_time:~0,2%)*60 + (%current_time:~3,2% - %last_attempt_time:~3,2%)
if %time_diff% geq 60 (
echo "No attempts made in the last hour, resetting count"
set count=0
set last_attempt_time=
)
goto reboot


:end
color 0C
echo "Something went wrong. Contacting Admin for Rescue ..."
rem Feature can be added on request ... $
pause
