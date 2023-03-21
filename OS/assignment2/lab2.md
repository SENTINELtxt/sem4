## OS Lab Assignment 2

---

_a) Create a directory structure in your home directory (cse, two subdirectories cprogs and projects under cse) while being in your home directory._

```bash
$ cd ~
$ mkdir cse
$ mkdir cse/cprogs cse/projects
```

---

_b) Change to the directory projects._

```bash
$ cd cse/projects
```

---

_c) Create a file called biodata and store your name, age, sex, and address in it._

```bash
$ cat>biodata.txt
name: lord puneet
age: 69
sex: alpha male
address: earth
ctrl+z
```

---

_d) Make a copy of the file biodata into another file text within the directory cprogs._

```bash
$ cp biodata.txt ../cprogs/text.txt
```

---

_e) Move the file text from cprogs to projects._

```bash
$ mv ../cprogs/text.txt .
```

---

_f) Combine the contents of the file biodata and text into another file datatext._

```bash
$ cat biodata.txt text.txt>datatext.txt
```

---

_g) Rename the file text to newtext._

```bash
$ mv text.txt newtext.txt
```

---

_h) Change the permissions of the file newtext to rw-rw-rw-._

```bash
$ chmod 666 newtext.txt
```

---

_i) List all filenames starting with ‘a’ or ‘b’ or ‘m’._

```bash
$ find . -type f -name "[a-b-m]*"
```

---

_j) List all filenames that end with a digit._

```bash
$ find . -type f -name "*[0-9].*"
```

---

_k) List all files in the current directory whose second character is a digit._

```bash
$ find . -type f -name "?[0-9]*"
```

---

_l) Use command(s) to create a directory in your home directory called KeepOut whose contents can be read only by you._

```bash
$ cd ~
$ mkdir KeepOut
$ chmod 400 KeepOut
```
