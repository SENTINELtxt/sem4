## OS Lab Assignment 7

---

_1. Write a shell script that displays a list of all files in the current directory to which you have read, write and execute permissions._

```bash
#!/bin/bash

for file in ./*; do
    if [ -r "$file" ] && [ -w "$file" ] && [ -x "$file" ]; then
        echo "$file"
    fi
done
```

---

_2. Write a shell script that lists files by modification time when called with lm and by access time when called with la. By default, the script should show the listing of all files in the current directory._

```bash
#!/bin/bash

case $1 in
    lm) ls -lt;;
    la) ls -lut;;
    *) ls -l;;
esac
```

---

_3. Write a shell script to display the files created or updated within fourteen days from the current date._

```bash
#!/bin/bash

find . -type f -atime -14 -mtime -14 | sort -u
```

---

_4. Develop a shell script which displays all files with all attributes those have been created or modified in the month of November._

```bash
#!/bin/bash

current_year=$(date +%Y)
find . -type f -newermt "$current_year-11-01" ! -newermt "$current_year-12-01" -ls
```
