max_attempts=10
timeout_seconds=10
count=0
last_attempt_time

:start

echo "Loading Server ..."
java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.19.2-43.2.6/win_args.txt nogui
clear
if [[ $count -ge 1 ]]; then
    goto check_attempt
fi


#Rebooting Server after 10 seconds. 
#If max_attempts reached before 1 hour then human intervention needed.
:reboot
if [[$count -eq $max_attempts]];then
    goto end
fi
echo "Reboot Atempt: $count" 
echo "Server Rebooting ... Press Ctrl+C to abort script."
last_attempt_time=$(($(date +%s) / 60))
count=$((count+1))
clear
goto start


:check_attempt
current_time=$(($(date +%s) / 60))
time_diff=$((current_time-last_attempt_time))
if [[time_diff -geq 60]]; then
    echo "No attempts made in the last hour, resetting count"
    count=0
fi
goto reboot

:end

echo "Something went wrong. Contacting Admin for Rescue ..."