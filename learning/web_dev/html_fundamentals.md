---
tags: [html, web_dev, fundamentals]
created: 2026-04-01
---

# Day 1: HTML Fundamentals

---

## 🧱 What is HTML?

HTML (HyperText Markup Language) is used to format and structure content sent between machines. Browsers like Chrome and Safari read HTML files and render them visually.

- HTML uses tags defined by the W3C — you cannot make up your own
- Tags are case-insensitive (<HTML> = <html>)
- Most tags come in pairs: an opening tag and a closing tag

<tagname>Content goes here</tagname>

Every HTML document follows this base structure:

<html>
 <head>
 <title>My Page Title</title>
 </head>
 <body>
 <p>Hello, World!</p>
 </body>
</html>

> 💡 <head> = page metadata (title, settings). <body> = visible content.
> 

---

## 📝 Text & Structure Tags

### Headings

<h1>Largest Heading</h1>
<h2>Slightly Smaller</h2>
<h3>Even Smaller</h3>
<h6>Smallest Heading</h6>
<p>Normal paragraph text</p>

<h1> is the biggest, <h6> is the smallest. Use headings to label sections.

---

### Paragraphs & Spacing

HTML ignores extra spaces and blank lines in your code. Everything gets squished together unless you use the right tags.

<!-- This will display on ONE line despite the line break in code -->
<p>
 This is line one.
 This is line two.
</p>

<!-- Use <br> to force a line break -->
<p>
 This is line one.<br>
 This is line two.
</p>

<!-- Use <hr> for a horizontal dividing line -->
<hr>

---

### Non-Breaking Space & Character Entities

Because < and > are used by HTML tags, you can't type them directly in content. Use character entities instead.

| You want to show | Use this |
| --- | --- |
| (extra space) | &nbsp; |
| < | &lt; |
| > | &gt; |
| & | &amp; |
| © | &copy; |

<!-- Two forced spaces -->
<p>Price:&nbsp;&nbsp;$10.00</p>

<!-- Displaying HTML code as text -->
<p>An HTML document starts with &lt;html&gt; and ends with &lt;/html&gt;</p>

---

### Text Formatting Tags

<b>Bold text</b>
<i>Italic text</i>
<mark>Highlighted text</mark>
<del>Strikethrough text</del>
<ins>Underlined text</ins>
<small>Smaller relative text</small>
<sup>Superscript</sup> <!-- e.g. x² -->
<sub>Subscript</sub> <!-- e.g. H₂O -->

Example — a chemistry formula:

<p>Water is H<sub>2</sub>O and energy is E=mc<sup>2</sup></p>

---

### Preserving Format with <pre>

By default, HTML collapses all whitespace. Use <pre> when you want content to appear exactly as typed (useful for poems, code, or aligned text).

<pre>
 Mary had a little lamb,
 Its fleece was white as snow,
 And everywhere that Mary went,
 The lamb was sure to go.
</pre>

> ⚠️ Be careful with indentation — <pre> includes any spaces before it in your editor.
> 

---

### Code Blocks

<!-- blockquote: indented quote from another source -->
<blockquote>This is a quoted block of text.</blockquote>

<!-- code: marks a segment as code (different font, useful for screen readers & search) -->
<code>print("Hello, World!")</code>

---

## 🖼 Images

<img src="filename.jpg" alt="Description of image" width="300" height="200">

| Attribute | Purpose |
| --- | --- |
| src | Path to the image file |
| alt | Text shown if image fails to load; read by screen readers |
| width / height | Optional — resize the image display |

### File Paths: Relative vs Absolute

Always use relative paths in your assignments. Absolute paths break when files move to a different drive or machine.

<!-- ✅ Relative — same folder as HTML file -->
<img src="logo.jpg" alt="Logo">

<!-- ✅ Relative — image is inside a subfolder called "images" -->
<img src="./images/logo.jpg" alt="Logo">

<!-- ✅ Relative — image is one folder UP, then inside "images" -->
<img src="../images/logo.jpg" alt="Logo">

<!-- ❌ Absolute — NEVER use this in assignments -->
<img src="C:/Users/Student/Desktop/logo.jpg" alt="Logo">

> 💡 . = current folder, .. = one level up (parent folder)
> 

---

## 🔗 Links (Hyperlinks)

<a href="https://www.uow.edu.au" target="_blank">Visit UOW</a>

| Attribute | Value | Behaviour |
| --- | --- |
| href | URL or filename | Where to go when clicked |
| target | _blank | Opens in a new tab |
| target | _self | Opens in the same tab (default) |### Linking to Another HTML File

<a href="contact.html">Contact Us</a>

### Image as a Link

<a href="https://www.uow.edu.au">
 <img src="logo.jpg" alt="UOW Logo">
</a>

### Internal Links (Jump to Section on Same Page)

Use id to mark a target, then #id in the href to jump to it.

<!-- Navigation at the top -->
<a href="#introduction">Go to Introduction</a>
<a href="#conclusion">Go to Conclusion</a>

<!-- Sections further down the page -->
<h2 id="introduction">Introduction</h2>
<p>Content here...</p>

<h2 id="conclusion">Conclusion</h2>
<p>Content here...</p>

> ⚠️ id values must be unique on the page and contain no spaces.
> 

---

## 📋 Lists

### Unordered List (Bullet Points)

<ul>
 <li>HTML</li>
 <li>CSS</li>
 <li>JavaScript</li>
</ul>

### Ordered List (Numbered)

<ol>
 <li>Open your editor</li>
 <li>Write your HTML</li>
 <li>Save and open in browser</li>
</ol>

### Definition List (Term + Explanation)

<dl>
 <dt>HTML</dt>
 <dd>HyperText Markup Language — used to structure web content.</dd>

 <dt>CSS</dt>
 <dd>Cascading Style Sheets — used to style web content.</dd>
</dl>

---

## 📊 Tables

<table border="1" width="80%">
 <caption>Student Records</caption>
 <tr>
 <th>Username</th>
 <th>First Name</th>
 <th>Last Name</th>
 </tr>
 <tr>
 <td>jsmith</td>
 <td>John</td>
 <td>Smith</td>
 </tr>
</table>

| Tag | Purpose |
| --- | --- |
| <table> | Creates the table |
| <tr> | Table Row |
| <th> | Table Header cell (bold, centred) |
| <td> | Table Data cell (regular) |
| <caption> | Title displayed above the table |
| border | 1 = show borders, 0 = hide borders |

### Column Span & Row Span

Use colspan to merge across columns, rowspan to merge across rows. Both are attributes on <td> or <th>.

<table border="1">
 <tr>
 <!-- This cell spans 2 columns -->
 <th colspan="2">Student Details</th>
 </tr>
 <tr>
 <td>Name</td>
 <td>John Smith</td>
 </tr>
 <tr>
 <!-- This cell spans 2 rows -->
 <td rowspan="2">Scores</td>
 <td>85</td>
 </tr>
 <tr>
 <td>90</td>
 </tr>
</table>

> 💡 Use width="50%" on the table so it scales with the browser window instead of being a fixed pixel size.
> 

---

## 💬 Comments

Comments are ignored by the browser — use them to explain your code.

<!-- This is a comment. The browser will not display this. -->

<!-- TODO: Add navigation bar here -->
<h1>Welcome</h1>

---

## 🔒 Security Note: index.html

When someone visits www.yoursite.com without specifying a file, the server returns index.html by default. If there's no index.html, some servers will display a directory listing — showing all your files to anyone visiting.

/
├── index.html ← Always have this as your home page
├── contact.html
├── about.html
└── images/

> ⚠️ A visible directory listing is a security vulnerability — it exposes your site structure to potential attackers.
> 

---

## 📌 Quick Reference Cheat Sheet

| Tag | Purpose |
| --- | --- |
| <h1> – <h6> | Headings (largest to smallest) |
| <p> | Paragraph |
| <br> | Line break |
| <hr> | Horizontal rule (divider line) |
| <pre> | Preserve formatting exactly |
| <b> | Bold |
| <i> | Italic |
| <mark> | Highlight |
| <del> | Strikethrough |
| <ins> | Underline |
| <sup> / <sub> | Superscript / Subscript |
| <img> | Image |
| <a> | Hyperlink |
| <ul> / <ol> | Unordered / Ordered list |
| <li> | List item |
| <dl>, <dt>, <dd> | Definition list |
| <table>, <tr>, <th>, <td> | Table elements |
| <!-- --> | Comment |

---

## ⏭️ Coming Up Next

- HTML Forms — collecting user input and submitting to a server
- CSS — styling and visual design
- JavaScript — interactivity and logic
