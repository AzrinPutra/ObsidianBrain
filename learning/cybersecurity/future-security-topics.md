# Future Security Topics

## Regex & Security Links

### Regex to Obfuscation
- How regex patterns can be used to detect obfuscated payloads
- Reverse engineering obfuscated strings
- Malware detection using regex signatures

### Escaping & Vulnerabilities

#### Cross-Site Scripting (XSS)
- Understanding HTML entity encoding (`&` → `&amp;`)
- Context-aware escaping (HTML, JS, URL, CSS)
- Regex-based input validation bypasses
- DOM-based XSS

#### SQL Injection
- String escaping (`'` → `\'`)
- Regex to detect SQL injection patterns
- Weak validation exploitation

#### Command Injection
- Shell metacharacters (`;`, `|`, `&`, `` ` ``)
- Regex for dangerous input patterns

#### Path Traversal
- `../` sequences
- Regex to block directory traversal

### Weak Validation Bypass
- Regex edge cases (empty strings, null bytes)
- Unicode normalization issues
- Case sensitivity exploits

## Learning Path
1. OWASP Input Validation Cheat Sheet
2. PortSwigger Web Security Academy — Regex chapters
3. Practice: DVWA / PortSwigger Labs

## Notes
- "Escaping characters" → Security mindset
- Regex is both a defense tool (validation) and an attack surface (bypass)
- Weak regex = weak security