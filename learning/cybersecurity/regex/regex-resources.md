# Regex Resources & Practice

## Interactive Tutorials
- **RegexOne** — https://regexone.com/ — Interactive 15-lesson intro (recommended start)
- **RegexLearn** — https://regexlearn.com/ — Step-by-step from basics to advanced

## Practice Platforms
- **Regex Golf** — https://alf.nu/regexGolf — Challenge yourself, compare solutions
- **HackerRank Regex** — https://www.hackerrank.com/domains/regex — Practical challenges
- **LeetCode Regex** — https://leetcode.com/tag/regex/ — Algorithm-adjacent practice

## Cheat Sheets
- **Regex Cheat Sheet** — https://cheatography.com/davechild/cheat-sheet/regular-expressions/
- **MDN Regex Guide** — https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions

## Key Lessons from CSIT 128 Assignment

### Common Mistakes to Avoid
| Mistake | Wrong | Correct |
|---------|-------|---------|
| Whitespace | `/s` | `\s` |
| Anchors outside `[]` | `\^` or `\$` | `^` and `$` (no backslash) |
| Property vs Method | `matches.length()` | `matches.length` |
| Building dynamically | `/variable/g` | `new RegExp(variable, "g")` |

### Quick Reference (JavaScript)
```
\s     — whitespace (space, tab, newline)
\w     — word character [a-zA-Z0-9_]
\d     — digit [0-9]
^      — start of string
$      — end of string
.      — any character
*      — 0 or more
+      — 1 or more
?      — 0 or 1
[abc]  — any of a, b, or c
[^abc] — not a, b, or c
()     — capture group
```

## Practice Exercises

### Level 1: Basics
1. Match any 3-digit number → `\d{3}`
2. Match email format → `[\w.]+@[\w.]+\.\w+`
3. Match phone (SG format) → `\+65\d{8}`

### Level 2: Intermediate
1. Match dates (YYYY-MM-DD) → `\d{4}-\d{2}-\d{2}`
2. Match URLs → `https?://[\w./-]+`
3. Validate password (8+ chars, 1 num) → `(?=.*\d).{8,}`

### Level 3: Advanced
1. Extract all numbers from string
2. Replace all whitespace with single space
3. Validate credit card format (groups of 4)

## Notes from Assignment 2
- Always check empty string BEFORE regex test
- Use `new RegExp(var, "flags")` for dynamic patterns
- Test in browser console before submitting