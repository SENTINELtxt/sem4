## OS Home Assignment 7

---

_1. Write a shell script to print last twenty commands issued by the user. The user name is supplied as a command line argument to the script (use bash-history file)._

```bash
#!/bin/bash

username=$1
history_file="/home/$username/.bash_history"

if [ ! -f $history_file ]; then
    echo "Error: history file for user $username not found"
    exit 2
fi

tail -n 20 $history_file
```

---

_2. Write a shell program, which displays the message "welcome" and prints the date when you login to your system._

**To display a welcome message and print the date when you login to your system, you can add the following lines to your `.bashrc` file:**

```bash
#!/bin/bash

echo "Welcome"
echo "Today is $(date)"
```

**The `.bashrc` file is executed every time you open a new terminal or login to your system.**

---

_3. Accept a string from the terminal and echo a suitable message if it doesn't have at least ten characters._

```bash
#!/bin/bash

echo "Enter a string:"
read string

if (( ${#string} < 10 )); then
  echo "The string is too short."
else
  echo "The string is at least ten characters long."
fi
```

---

_4. Write a shell script which receives either the LOGNAME or the UID supplied at the command prompt and finds out at how many terminals this user has logged in._

```bash
#!/bin/bash

if [ "$1" == "-u" ]; then
  user=$(getent passwd "$2" | cut -d: -f1)
else
  user=$1
fi

num_terminals=$(who | grep "$user" | wc -l)
echo "$user is logged into $num_terminals terminal(s)."
```

---

_5. Write a shell script, which gets executed the moment a user logs in. It should display the message "GOOD MORNING" or "GOOD AFTERNOON" or "GOOD EVENING" depending upon the time at which the user logs in._

```bash
nano ~/.bashrc
```

```bash
hour=$(date +%H)

if [ $hour -lt 12 ]; then
  echo "GOOD MORNING"
elif [ $hour -lt 18 ]; then
  echo "GOOD AFTERNOON"
else
  echo "GOOD EVENING"
fi
```

---
