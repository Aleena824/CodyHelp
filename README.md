# CodyHelp
CodyHelp is a command-line interface tool that can analyse source code files, provide explanations, detect possible bugs, and suggest improvements.

Built for CS students and junior developers who are tired of switching between browser tabs, forgetting syntax, and blanking out when asked "can you walk me through this code?"

## Goal:
To build a lightweight developer assistant that works directly in the terminal, similar to modern AI coding tools.

## Inspiration:
As a CS student, I constantly found myself stuck, such as, forgetting syntax, not knowing how to explain my own code, and dreading the "walk me through this" question in interviews.

CodyHelp was built to fix that. It's the tool I wish I had when I started coding.

## Core Features:
* Explain code files
* Interview mode code explanation
* Detect possible bugs in code
* Review code and suggest improvements
* Error explanation from stack traces
* Support multiple programming languages

## Installation
pip install codyhelp

## Setup
1. Get a free GitHub Models token at github.com/marketplace/models
2. Set your token:
   - Windows: $env:GITHUB_TOKEN="your_token_here"
   - Mac/Linux: export GITHUB_TOKEN="your_token_here"
3. You're ready to use it!

## Usage
codyhelp explain main.py

codyhelp explain main.py --interview

codyhelp review main.py

codyhelp stacktrace error.txt

## Example:
**Run CodyHelp from the terminal:**

codyhelp explain linkedList.py --interview

**Example output:**

INTERVIEW MODE — linked_list.py

How to explain this in an interview:

"This implements a singly linked list with insert and traversal operations. Each node stores a value and a pointer to the next node, giving us dynamic memory allocation unlike arrays..."

Complexity to mention:

+ Insert at head: O(1)
+ Search: O(n)
+ Space: O(n)

Follow-up questions an interviewer might ask:

* "How would you detect a cycle in this linked list?"
* "How is this different from a doubly linked list?"
* "When would you choose a linked list over an array?"

Concepts you should know to fully defend this code:

+ Node structure and pointers
+ Dynamic vs static memory allocation
+ Singly vs doubly linked lists
  
## Technologies

- Python
- CLI (Command-line interface)
- Github models
- Git and Github

## Future Improvements

- [ ] Git diff code review
- [ ] Repository-level code understanding
- [ ] Leetcode practice suggestions
