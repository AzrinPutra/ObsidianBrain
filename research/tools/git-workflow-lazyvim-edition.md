---
title: GIT WORKFLOW (LazyVim Edition)
path: "GIT WORKFLOW (LazyVim Edition)"
url: https://www.notion.so/GIT-WORKFLOW-LazyVim-Edition-2c8bd926b4e480b1ba84f0926f002b4f
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2025-12-13T12:56:00.000Z
---

# GIT WORKFLOW (LazyVim Edition)
This guide covers:
1. Create Git repo (local + GitHub)
2. Connect them
3. Commit changes
4. Push to GitHub
5. Use Lazygit inside Neovim (`<leader>gg`)
6. Fix common beginner errors
Let’s begin.
___
## 🧱 **Step 1 — Your project folder**
Go to your project:
```bash
cd ~/.config/nvim


```
(or any project folder)
___
## 🌱 **Step 2 — Initialize Git (create a repo)**
This creates a new Git repository:
```bash
git init


```
You now have a local Git repo — but it has NO commits and NO remote yet.
___
## 📦 **Step 3 — Add your files**
```bash
git add .


```
___
## 📝 **Step 4 — Make your first commit**
```bash
git commit -m "Initial commit"


```
Now Git is officially tracking your project.
___
## 🌐 **Step 5 — Create a GitHub repo**
Go to:
#### [https://github.com/new](https://github.com/new)
Create a repo named:
```plain text
nvim


```
(or anything you want)
After creation, GitHub shows instructions like:
```plain text
git remote add origin git@github.com:USERNAME/REPO.git


```
Keep this page open.
___
## 🔗 **Step 6 — Link your local repo to GitHub**
Using **SSH** (recommended):
```bash
git remote add origin git@github.com:USERNAME/REPO.git


```
To check:
```bash
git remote -v


```
___
## 🚀 **Step 7 — Push your code to GitHub**
Rename your branch to `main` (modern default):
```bash
git branch -M main


```
Then push everything:
```bash
git push -u origin main


```
Your project is now backed up on GitHub.
___
## 🎉 STOP HERE — YOU NOW KNOW BASIC GIT
From now on, you only need **three commands**:
7. `git add .`
8. `git commit -m "message"`
9. `git push`
OR…
you use the **LazyVim Git UI**, which is easier.

## 🚀 **How to Set Up SSH for GitHub (Beginner-Friendly Guide — macOS)**
Using SSH is the easiest and safest way to push code to GitHub without entering your username/password every time.
Follow this step-by-step guide.
___
## 🧩 **1. Check if you already have SSH keys**
Open Terminal and run:
```bash
ls ~/.ssh


```
If you see files like:
- `id_ed25519`
- `id_ed25519.pub`
- `id_rsa`
- `id_rsa.pub`
Then you already have SSH keys.
If you see **nothing**, don’t worry — we’ll create one.
___
## 🔑 **2. Create a new SSH key (only if needed)**
Run this command:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"


```
GitHub recommends **ed25519** (modern and secure).
You will see:
```plain text
Enter file in which to save the key (/Users/you/.ssh/id_ed25519):


```
Just press **Enter**
(accept default location)
Then it asks:
```plain text
Enter passphrase (empty for no passphrase):


```
Press **Enter**
(and Enter again to confirm)
This creates two files:
- `id_ed25519` → your **private** key
- `id_ed25519.pub` → your **public** key (safe to share)
___
## 📋 **3. Copy your public SSH key**
Run:
```bash
pbcopy < ~/.ssh/id_ed25519.pub


```
This copies your SSH key into your clipboard.
___
## 🌐 **4. Add SSH key to GitHub**
10. Go to **GitHub**
11. Click your profile → **Settings**
12. Left sidebar: **SSH and GPG Keys**
13. Click **New SSH key**
14. Title:
**MacBook Key** (or anything you like)
15. Key type:
**Authentication Key**
16. Paste your copied key into the big box
17. Click **Add SSH key**
Done!
___
## 🧪 **5. Test your SSH connection**
Run:
```bash
ssh -T git@github.com


```
The first time, you’ll see:
```plain text
Are you sure you want to continue connecting? (yes/no)


```
Type:
```plain text
yes


```
If everything is correct, you’ll see:
```plain text
Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.


```
This means SSH is working perfectly.
___
## 🔗 **6. Link your project to the GitHub repo (SSH version)**
Inside your project folder, run:
```bash
git remote add origin git@github.com:USERNAME/REPO.git


```
(Replace `USERNAME` and `REPO`)
Then push for the first time:
```bash
git branch -M main
git push -u origin main


```
___
## 🚀 **7. Daily Git workflow (SSH mode)**
Now that SSH is set up, pushing your work is easy:
```bash
git add .
git commit -m "message"
git push


```
No passwords.
No tokens.
No prompts.
___

## For GO Git workflow

In Go, **every project that uses **`**go test**`** needs a module** (with `go.mod`). Without it, `go test` cannot resolve packages or dependencies.
Here’s how to fix it:
___
#### 1. Initialize a Go module
Go to the folder containing your `.go` files (e.g., `~/Projects/my-go-project`) and run:
```bash
go mod init github.com/yourusername/projectname

ie. go mod init github.com/AzrinPutra/nvimgo
```



- Replace `github.com/yourusername/projectname` with a valid module path (can be local if you’re not publishing).
- This creates a `go.mod` file in your folder.
___
#### 2. Add dependencies (if needed)
If your code imports external packages, run:
```bash
go get ./...


```
This will download and add dependencies to your module.
___
#### 3. Now test
Inside the module folder:
```bash
go test ./...


```
- `_test.go` files will be detected automatically.
- If you use `dap-go.debug_test()` in Neovim, it will now work because there’s a proper module context.
___
#### 4. Directory structure example
```plain text
my-go-project/
├── go.mod
├── main.go
├── main_test.go


```
- `main.go` → normal code
- `main_test.go` → tests
- Neovim + dap-go will now debug tests successfully.