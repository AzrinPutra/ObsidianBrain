# Linux Commands Refresher

## Quick Refresh

### grep — Search text
```bash
# Basic search
grep "error" log.txt

# Case insensitive
grep -i "error" log.txt

# Show line numbers
grep -n "error" log.txt

# Invert match (exclude)
grep -v "success" log.txt

# Recursive search
grep -r "error" /var/log/
```

### awk — Text processing
```bash
# Print 1st column
awk '{print $1}' data.txt

# Print specific columns
awk '{print $1, $3}' data.txt

# Use delimiter
awk -F',' '{print $2}' csv.txt

# Conditional
awk '$3 > 100 {print $1}' data.txt
```

## New Commands to Learn

### tee — Read + Write simultaneously
```bash
# Save to file AND show on screen
ls -la | tee output.txt

# Append mode
echo "new line" | tee -a output.txt

# Pipeline use
command1 | tee file.txt | command2
```

### sed — Stream editor (find & replace)
```bash
# Replace first occurrence
sed 's/old/new/' file.txt

# Replace all occurrences
sed 's/old/new/g' file.txt

# Replace on specific line
sed '3s/old/new/' file.txt

# Delete line containing pattern
sed '/pattern/d' file.txt

# In-place edit
sed -i 's/old/new/g' file.txt

# Using regex
sed 's/[0-9]\{3\}/XXX/g' file.txt
```

## Practice Examples

### Real-world combos
```bash
# Find errors, show line numbers, save to file
grep -n "ERROR" server.log | tee errors.txt

# Extract IPs from log
awk '{print $1}' access.log | sort | uniq -c | sort -rn

# Clean up CSV (replace commas with pipes)
sed 's/,/\|/g' data.csv > cleaned.csv

# Append timestamp to log
date | tee -a daily.log
```

## Common Flags Reference
| Command | Flag | Meaning |
|---------|------|---------|
| grep | -r | Recursive |
| grep | -i | Case insensitive |
| grep | -n | Line numbers |
| awk | -F | Field separator |
| sed | -i | In-place |
| sed | -g | Global (all matches) |