# CSIT128 Web Dev Assignment 1 - Part 4: JavaScript Form

## Step-by-Step Guide

### Step 1: Basic HTML Form Structure
- Use `<form>` wrapping a `<table>`
- Each field in `<tr><td>label</td><td><input/textarea/select></td></tr>`
- Use `id` attributes for all inputs so JS can find them

### Step 2: Name Field
- `<input type="text" id="name">`
- JS: Check not empty, check regex `/[^A-Za-z0-9\s]/.test(value)` returns true if special chars found

### Step 3: Module Code
- `<input type="text" id="module">`
- JS: If empty → OK. If not empty, check regex `/^[A-Z]{4}[4-8]{3}$/`
- Pattern: 4 uppercase letters + 3 digits (each 4-8)

### Step 4: Current Date
- `<input type="text" id="date" readonly>`
- JS: Use `new Date()`, getDay() (0=Sun), getMonth() (0=Jan)
- Build string: date + " " + month + " " + year + " " + day + " " + time
- Use `setInterval(updateDate, 1000)` to update every second

### Step 5: Message & Find/Replace
- Message: `<textarea id="message" rows="4" cols="20">Hello 202604</textarea>`
- Find: `<input type="text" id="find">`
- Replace: `<input type="text" id="replace" disabled>`
- On Find input: `replace.disabled = (find.value === "")`
- On button click: `msg.value.split(find).join(replace)` to replace all

### Step 6: Radio & Select
- Radio: `<input type="radio" name="source" value="English" checked>`
- Select: `<select id="target"><option value="zh-CN" selected>Chinese</option>...`
- Use `value` attributes for translation API

### Step 7: Submit
- `<button type="submit" onclick="return validateForm()">Translate</button>`
- Validate name & module first
- Open Google Translate in new tab with message & target language

### Step 8: Reset
- `<button type="reset">` - HTML handles this automatically

## Key Regex Patterns to Remember
- `[^A-Za-z0-9\s]` = NOT letters/numbers/spaces
- `^[A-Z]{4}[4-8]{3}$` = exactly 4 uppercase + 3 digits 4-8