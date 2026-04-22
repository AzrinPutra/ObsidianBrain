# JavaScript Learning Notes

## JavaScript Date & Time
- Use `new Date()` with `getDay()`, `getMonth()`, `getDate()`, `getFullYear()`, `getHours()`, `getMinutes()`
- `getMonth()` and `getDay()` return 0-based indexes — use arrays to get full names
- Days array must start with "Sunday" (getDay() returns 0 for Sunday)
- 12hr conversion: subtract 12 if hours > 12, set ampm, fix midnight (hours === 0 → hours = 12), fix noon (hours === 12 stays 12)
- Leading zero fix: `minutes = minutes < 10 ? "0" + minutes : minutes`
- Auto-update textbox every second: `setInterval(updateDate, 1000)`

## JavaScript General
- Use `//` for comments, never `<!-- -->`
- Never use `\` for line continuation in browser JS
- camelCase for variables/functions, UPPER_SNAKE_CASE for constants, PascalCase for classes
- Ternary operator: `condition ? valueIfTrue : valueIfFalse`
- `==` compares, `=` assigns
- Arrow function `() => {}` and regular function `foo() {}` are interchangeable

## HTML Form
- `<form>` wraps `<table>`, not inside it
- All content inside `<tr>` must be in `<td>`
- Button types: `type="submit"` triggers onsubmit, `type="button"` does nothing alone, `type="reset"` resets fields
- Default button type inside a form is `type="submit"`
- `onsubmit="return validateName()"` — return is required to block submission

## Form Validation
- Add `id` to inputs so JS can find them with `getElementById`
- Add `<span id="nameError" style="color:red"></span>` for error messages
- Empty check: `userName === ""`
- Special character check: `/[^A-Za-z0-9\s]/.test(userName)` returns true when special char found
- `^` inside `[ ]` means NOT, outside `[ ]` means start of string
- `\s` = spaces, `$` inside `[ ]` = literal dollar sign

## Completed validateName() Function
```javascript
function validateName() {
  var userName = document.getElementById("userName").value.trim();
  if (userName === "") {
    document.getElementById("nameError").innerHTML = "Name cannot be empty";
    return false;
  }
  if (/[^A-Za-z0-9\s]/.test(userName)) {
    document.getElementById("nameError").innerHTML = "No Special Characters Allowed!";
    return false;
  }
  document.getElementById("nameError").innerHTML = "";
  return true;
}
```