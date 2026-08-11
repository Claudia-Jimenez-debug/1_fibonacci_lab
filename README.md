# Session 1 lab — Fibonacci

MSA-DATI07-01 · Python Environments & Engineering Workflows

Your first hands-on exercise with **git, GitHub, and VS Code**. Fix a small Python module, commit your fixes as you go, push to your own GitHub. You have 60 minutes.

---

## What you'll do

The `fibonacci.py` module has **3 bugs**. Fix them. Then there's a **4th task** where you extend one of the functions.

Make **at least 4 commits** — one per task. I check the log.

---

## Setup (2 minutes)

**1. Fork this repository.** Click the `Fork` button at the top right of this page on GitHub. That creates a copy of the repo under your own account.

**2. Clone your fork.** Open a terminal (Terminal on macOS, Git Bash on Windows — not PowerShell) and run:

```bash
git clone https://github.com/YOUR-USERNAME/fibonacci-lab.git
cd fibonacci-lab
```

Replace `YOUR-USERNAME` with your actual GitHub username.

**3. Open the folder in VS Code:**

```bash
code .
```

**4. Verify Python works.** In VS Code's built-in terminal (`Ctrl` + backtick on Windows, `Cmd` + backtick on Mac):

```bash
python main.py
```

You should see a bunch of `[PASS]` and `[FAIL]` messages, ending with `Summary: 4/11 checks passing`. That's your starting point.

Your job: get to `11/11`.

---

## The tasks

Open `fibonacci.py` in VS Code. Read every docstring. The examples in the docstrings tell you exactly what each function should return.

### Task 1 — Fix `fib(n)`

`fib(7)` should return `13`. It doesn't. Read the loop carefully and figure out what's off.

**Hint:** the base cases work (`fib(0)` and `fib(1)` pass). Something is wrong with how the function returns the answer for larger `n`.

### Task 2 — Fix `fib_sequence(n)`

`fib_sequence(8)` should return `[0, 1, 1, 2, 3, 5, 8, 13]`. It returns something else. Look at what you're actually getting — the pattern is very telling.

### Task 3 — Fix `golden_ratio_approx(n)`

The docstring says this function should approach `phi ≈ 1.618`. You're getting `0.618`. That's a big hint on its own.

### Task 4 — Extend `fib(n)` to handle negative integers

Fibonacci extends naturally to negative indices via:

```
F(-n) = (-1)^(n+1) · F(n)
```

Which means:

| n     | F(n)  |
|-------|-------|
| -1    | 1     |
| -2    | -1    |
| -3    | 2     |
| -4    | -3    |
| -5    | 5     |
| -6    | -8    |
| -7    | 13    |

Right now, `fib(-1)` raises `ValueError`. Modify the function so negative arguments work using the formula above.

---

## Commit hygiene — this is graded

You saw the rules in the lecture. Recap:

- **One commit per task** (minimum 4 commits total)
- **Imperative mood:** "Fix off-by-one in fib return" — not "Fixed" or "fixes"
- **Under 50 characters** on the first line
- **No** `fix`, `wip`, `stuff`, `asdf`, `final`, or `update`

Good example: `Fix fib return value returning F(n+1) instead of F(n)`

Bad example: `fixed the thing`

You can commit from VS Code's Source Control panel (branch icon in the Activity Bar) or from the terminal — your choice. I recommend using the Source Control panel to see the diffs before you commit.

---

## When you're done

From the terminal:

```bash
git push
```

(Or click the sync button in the Source Control panel, or on the status bar at the bottom of VS Code.)

Then send me the URL of **your fork** — not the original — via the class channel.

---

## Common stuck points

**`python main.py` says `command not found`** → try `python3 main.py`. On some systems Python 3 isn't aliased to `python`.

**`git push` asks for a password and rejects it** → GitHub disabled password auth in 2021. Use a Personal Access Token (see slide 23 from today).

**You're not sure which line is buggy** → run `python main.py`, look at what actually gets printed vs what's expected. The gap between them tells you where to look.

**VS Code isn't showing changes in Source Control** → make sure you saved the file (`Ctrl+S` / `Cmd+S`). Unsaved changes don't appear.

**You accidentally broke something else** → run `git diff` in the terminal to see everything you've changed. If it's a mess, `git checkout fibonacci.py` restores the last committed version (careful — you lose unsaved edits).

---

## Files in this repo

| File            | Purpose |
|-----------------|---------|
| `main.py`       | The test runner. Run it to check your work. **Don't edit** unless you know why. |
| `fibonacci.py`  | The module with the 3 bugs and the extension task. **This is where you work.** |
| `README.md`     | This file. |
| `.gitignore`    | What git should ignore. |
