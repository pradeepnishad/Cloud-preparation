🐧 Basic Linux Commands
1. date — Display current date and time

Shows the current system date and time.

date

Example:

Sat Sep 12 00:50:12 IST 2026
2. hostname — Display system hostname

Shows the name assigned to the computer/server/VM.

hostname

Example:

ubuntu-server

You can also change the hostname with:

sudo hostnamectl set-hostname my-server
3. pwd — Print Working Directory

Shows the directory you're currently inside.

pwd

Example:

/home/pradeep

Think:

pwd = "Where am I?"
4. whoami — Display current user

Shows which user account you're currently logged in as.

whoami

Example:

pradeep

If you're root:

root

Think:

whoami = "Who am I logged in as?"
5. w — Show logged-in users and activity

Shows users currently logged in, their terminals, login time, and what they're doing.

w

Example:

USER      TTY      FROM       LOGIN@   IDLE   WHAT
pradeep   pts/0    10.0.0.5   00:20    2:00   bash

It doesn't simply tell you "how many users are connected"; it gives you information about active login sessions.

For just seeing logged-in users:

who
6. history — Show previously executed commands

Displays commands you've previously entered in the shell.

history

Example:

  1  pwd
  2  ls
  3  cd /etc
  4  cat hostname
  5  history

You can execute a previous command using its number:

!3

This executes command number 3.

You can also search your command history with:

Ctrl + R
7. man — Manual/help for commands

man means manual.

It provides detailed documentation for commands.

man ls
man cp
man chmod

Inside man:

Space       → next page
b           → previous page
/keyword    → search
q           → quit

For example:

man ls

will explain the options available for ls.


-> listing files and directories 

Yep — you mean the **common variations/options (flags), syntax, and useful suffixes** for each command. I'll keep the same structure.

# Viewing & Reading Files

### `ls` — List files and directories

**Basic:**

```bash
ls
```

**Common variations:**

```bash
ls -l
```

→ Long/detailed listing.

```bash
ls -a
```

→ Shows hidden files.

```bash
ls -la
```

→ Detailed listing + hidden files.

```bash
ls -h
```

→ Shows file sizes in human-readable format.

```bash
ls -lh
```

→ Detailed listing with human-readable sizes.

```bash
ls -R
```

→ Lists directories recursively.

**Useful suffixes/options:**

```text
-l  → long format
-a  → all files, including hidden
-h  → human-readable sizes
-R  → recursive
-t  → sort by modification time
-S  → sort by file size
```

---

### `cat` — Display file contents

**Basic:**

```bash
cat file.txt
```

**Common variations:**

```bash
cat -n file.txt
```

→ Shows line numbers.

```bash
cat -b file.txt
```

→ Numbers only non-empty lines.

```bash
cat -A file.txt
```

→ Shows hidden/non-printing characters.

**Useful options:**

```text
-n  → number all lines
-b  → number non-empty lines
-A  → show non-printing characters
```

---

### `more` — View file one page at a time

```bash
more file.txt
```

Useful controls:

```text
Space → next page
Enter → next line
q     → quit
```

`more` is mainly for moving **forward** through a file.

---

### `less` — View file one page at a time

```bash
less file.txt
```

Useful controls:

```text
Space → next page
b     → previous page
↑     → previous line
↓     → next line
/word → search for word
n     → next search result
q     → quit
```

`less` is generally more powerful than `more`.

---

### `head` — Display beginning of a file

**Basic:**

```bash
head file.txt
```

By default → **first 10 lines**.

**Common variations:**

```bash
head -n 5 file.txt
```

→ Shows first 5 lines.

```bash
head -n 20 file.txt
```

→ Shows first 20 lines.

You can also write:

```bash
head -5 file.txt
```

**Useful option:**

```text
-n NUMBER → number of lines to display
```

---

### `tail` — Display end of a file

**Basic:**

```bash
tail file.txt
```

By default → **last 10 lines**.

**Common variations:**

```bash
tail -n 5 file.txt
```

→ Shows last 5 lines.

```bash
tail -n 20 file.txt
```

→ Shows last 20 lines.

A very important variation:

```bash
tail -f file.txt
```

→ **Continuously watches the file** and displays new lines as they are added.

This is extremely useful for monitoring logs:

```bash
tail -f /var/log/syslog
```

**Useful options:**

```text
-n NUMBER → number of lines
-f        → follow file as it grows
```

### Quick cheat sheet

```text
ls       → list files
ls -la   → detailed + hidden files

cat      → display entire file

more     → read page by page
less     → read page by page + search/navigation

head     → beginning of file
head -n 5 → first 5 lines

tail     → end of file
tail -n 5 → last 5 lines
tail -f  → continuously monitor file
```

**One terminology point:** `-l`, `-a`, `-n`, `-f`, etc. are generally called **options/flags** (or switches), not suffixes.
