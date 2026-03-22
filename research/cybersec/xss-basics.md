---
title: XSS Basics
path: "XSS Basics"
url: https://www.notion.so/XSS-Basics-200bd926b4e480c1bb96e7a5d58b2178
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2025-05-29T07:05:00.000Z
---

# XSS Basics
### Injecting Malicious Javascript
```html
<h1>Welcome <script>alert(1)</script></h1>
```
This runs an alert() function in javascript to create a pop up with the str value of ‘1’. This is a very basic example of inserting arbitrary code using <script></script>.

### Injecting Malicious Event Handler
```html
<h1>Welcome <svg onload=alert(1)></h1>
```
Let’s focus on `<svg onload=alert(1)>` . `<svg>` creates a svg(scalable vector graphics) element. `onload=alert(1)` runs the script specified in this case `alert(1)` when the svg element has loaded. This allows us to insert arbitrary code via creating an empty svg element and running onload.

### Injecting Malicious Link with Javascript:URL
```html
<h1>Welcome <a href=javascript:alert(1)>Click me</a></h1>
```
We are able to insert an anchor tag <a></a> in this example. However, instead of passing a link into the href attribute, we inserted a javascript function via javascript:

### Beyond alert(1)
Using the above examples, we are able to run alert(1). However this is not enough for an xss attack. We need to go in depth and show that we can run arbitrary code.

💡 Start off by using double quotes (””) and < > to close off html strings then build on it.
### Using loaders

