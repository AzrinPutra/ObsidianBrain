# PowerShell Resources & Practice

## Learning Paths
- **Microsoft Learn PowerShell** — https://learn.microsoft.com/en-us/powershell/ — Official docs, start with "Learn PowerShell"
- **CURRENT FOCUS** → https://learn.microsoft.com/en-us/training/paths/get-started-windows-powershell/ — "Get Started with Windows PowerShell" path
- **PowerShell in 60 Seconds** — https://www.power-shell.com/ — Quick tutorials
- **Flattening the Curve with PowerShell** — Free ebook series by Mike F Robbins

## Interactive Tutorials
- **TryHackMe PowerShell** — https://tryhackme.com/module/powershell — Hands-on exercises
- **PentesterAcademy PowerShell** — https://www.pentesteracademy.com/ — Advanced/Red team focused

## Practice Platforms
- **PowerShell Quiz** — https://powershell.org/quiz/ — Test your knowledge
- **HackerRank PowerShell** — https://www.hackerrank.com/domains/powershell — Basic challenges

## Recommended Learning Order

### Week 1: Basics
1. Variables, data types, operators
2. Cmdlets (Get-*, Set-*, etc.)
3. Pipeline (`|`) and objects
4. Comparison operators (`-eq`, `-gt`, `-like`, etc.)

### Week 2: Intermediate
1. Functions and parameters
2. Control flow (if/else, switch, foreach, while)
3. Working with files (Get-Content, Set-Content, CSV, JSON)
4. Error handling (Try/Catch)

### Week 3: Advanced
1. Remoting (Invoke-Command, WinRM)
2. Modules and packages
3. Regex in PowerShell
4. Security and encoding

### Week 4+: Specialization
- **Blue Team**: Log analysis, SIEM integration
- **Red Team**: Automation, C2 frameworks
- **SysAdmin**: Active Directory, Exchange, Azure

## Quick Reference

### Common Cmdlets
```powershell
# Navigation
Get-Location, Set-Location, Get-ChildItem, Get-Content

# Files
Get-Item, Set-Item, Copy-Item, Remove-Item, New-Item

# Objects
Get-Member, Select-Object, Where-Object, ForEach-Object

# System
Get-Process, Get-Service, Get-EventLog, Get-WmiObject

# Network
Test-Connection, Invoke-WebRequest, Test-NetConnection
```

### Variables & Operators
```powershell
$var = "value"
$num = 5
$arr = @(1,2,3)

# Comparison
-eq, -ne, -gt, -ge, -lt, -le
-like, -notlike, -match, -notmatch
-in, -notin

# Logical
-and, -or, -not
```

### Pipeline Examples
```powershell
# Filter and transform
Get-Process | Where-Object CPU -gt 100 | Select-Object Name, CPU

# Export data
Get-Service | Where-Object Status -eq Running | Export-Csv services.csv

# Loop through items
Get-ChildItem -Recurse | ForEach-Object { $_.FullName }
```

## Practice Exercises

### Level 1: Basics
1. Display "Hello World" script
2. Create variable, perform math, output result
3. List all running processes
4. Find files modified in last 7 days

### Level 2: Intermediate
1. Read CSV, filter rows, export filtered results
2. Create function with parameters
3. Parse JSON file and extract values
4. Write script with error handling (Try/Catch)

### Level 3: Advanced
1. Script to bulk rename files
2. Automated system inventory reporter
3. Parse Windows Event Logs for failed logins
4. Remotely execute command on multiple servers

## Common Mistakes to Avoid
| Mistake | Wrong | Correct |
|---------|-------|---------|
| String comparison | `==` | `-eq` |
| Variable in string | `$var` | `"$var"` or `"$($var)"` |
| Piping to variable | `$var = Get-Process \|` | `$var = Get-Process` |
| Case sensitivity | `-EQ` | `-eq` (PowerShell is case-insensitive) |
| Missing space in operator | `-eq` | `-eq` (space matters!) |

## Use Cases for Your Goals
- **Splunk**: PowerShell to generate/process logs, feed to Splunk
- **Cyber Security**: Log analysis, endpoint enumeration, automation
- **SysAdmin**: Server management, automation, AD operations

## Notes
- Tab completion is your friend (hit Tab after cmdlets)
- `Get-Help <cmdlet> -Full` for detailed docs
- `Get-Member` (`gm) to inspect object properties