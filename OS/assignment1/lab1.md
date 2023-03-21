## OS Lab Assignment 1

---

_a) List the names of the users logged in and their total count without displaying any further details._

```bash
$ who -q
```

---

_b) Find out your terminal’s device name._

```bash
$ tty
```

---

_c) Display current date in the form dd/mm/yyyy._

```bash
$ date +%d/%m/%y
```

---

_d) Find out your machine’s name and the version of the operating system._

```bash
$ uname -nr
```

---

_e) Clear the screen and place the cursor at row 12, column 25._

```bash
$ clear
$ tput cup 12 25
```

---

_f) Find the decimal equivalent of 1101001._

```bash
$ echo "ibase=2; 1101001" | bc
```

---

_g) Find out the users who are idling._

```bash
$ w
```

---

_h) Use man to get help_

```bash
$ man tty
```

---

_i) Ensure that bc displays the results of all divisions using three decimal places._

```bash
$ bc
scale=3
10/3
3.333
quit
```
