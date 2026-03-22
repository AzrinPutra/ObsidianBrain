---
title: Neovim Python IDE
path: "Neovim Python IDE"
url: https://www.notion.so/Neovim-Python-IDE-2c6bd926b4e4804fa83fe2a023d6be48
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2026-01-01T09:50:00.000Z
---

# Neovim Python IDE
## **Full Guide: Setting Up a Python IDE in Neovim (LazyVim, DAP, Autoformat, Git) for MacOs — 2025**
Build a **modern, beginner-friendly Python IDE** in Neovim with LazyVim on **macOS**.
___
### **1️⃣ Install Neovim**
Check your version:
```bash
nvim --version
```
Minimum recommended: **Neovim 0.9+**
Install via Homebrew:
```bash
brew install neovim
```
___
### **2️⃣ Bootstrap LazyVim**
1. Create config folder:
```bash
mkdir -p ~/.config/nvim
```
2. Open `init.lua`:
```bash
nvim ~/.config/nvim/init.lua
```
3. Paste the LazyVim bootstrap code:
** By right it can work with just this but now having some issues so use the full config in init.lua for now until a fix.
```lua
-- =========================
-- LazyVim + Python IDE
-- =========================

-- Bootstrap Lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none", "--branch=stable",
    "https://github.com/folke/lazy.nvim.git", lazypath
  })
end
vim.opt.rtp:prepend(lazypath)

-- =========================
-- Plugins
-- =========================
require("lazy").setup({

  -- LazyVim core
  {
    "LazyVim/LazyVim",
    import = "lazyvim.plugins",
    opts = {
      colorscheme = "catppuccin",
      disable_plugins = { "nvim-tree" }, -- fully disable nvim-tree
    },
  },

  -- Catppuccin Theme
  {
    "catppuccin/nvim",
    name = "catppuccin",
    priority = 1000,
    opts = {
      flavour = "mocha",
      integrations = {
        lualine = true,
        telescope = true,
        treesitter = true,
      },
    },
  },

  -- Telescope
  {
    "nvim-telescope/telescope.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      local telescope = require("telescope")
      local builtin = require("telescope.builtin")
      telescope.setup({})

      local map = vim.keymap.set
      map("n", "<leader>ff", builtin.find_files, { desc = "Find Files" })
      map("n", "<leader>fg", builtin.live_grep, { desc = "Live Grep" })
      map("n", "<leader>fb", builtin.buffers, { desc = "Buffers" })
      map("n", "<leader>fh", builtin.help_tags, { desc = "Help Tags" })

      -- New File
      map("n", "<leader>fn", function()
        vim.ui.input({ prompt = "New file: " }, function(f)
          if f and f ~= "" then vim.cmd("e " .. f) end
        end)
      end, { desc = "Create New File" })
    end,
  },

  -- Treesitter
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    opts = {
      highlight = { enable = true },
      indent = { enable = true },
      ensure_installed = { "python", "lua", "json", "bash" },
    },
  },

  -- Lualine
  {
    "nvim-lualine/lualine.nvim",
    opts = {
      options = {
        theme = "catppuccin",
        section_separators = "",
        component_separators = "",
      }
    },
  },

  -- Neo-tree (DO NOT OPEN AUTOMATICALLY)
  {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "nvim-tree/nvim-web-devicons",
      "MunifTanjim/nui.nvim",
    },
    opts = {
      filesystem = {
        hijack_netrw_behavior = "disabled",
        bind_to_cwd = false,
      },
      window = { auto_open = false },
    },
  },

  -- Autocomplete
  {
    "hrsh7th/nvim-cmp",
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",
      "L3MON4D3/LuaSnip",
      "saadparwaiz1/cmp_luasnip",
    }
  },

  -- Pyright LSP
  {
    "neovim/nvim-lspconfig",
    config = function()
      require("lspconfig").pyright.setup({})
    end,
  },

  -- Black Formatter
  {
    "stevearc/conform.nvim",
    opts = {
      formatters_by_ft = { python = { "black" } }
    }
  },

  -- Ruff Linter
  {
    "mfussenegger/nvim-lint",
    opts = {
      linters_by_ft = { python = { "ruff" } }
    }
  },

  -- Debug Adapter Protocol
  { "mfussenegger/nvim-dap" },

  -- Python Debugging (debugpy)
  {
    "mfussenegger/nvim-dap-python",
    ft = "python",
    dependencies = { "mfussenegger/nvim-dap" },
    config = function()
      local path = vim.fn.expand(
        "~/.local/share/nvim/mason/packages/debugpy/venv/bin/python"
      )
      require("dap-python").setup(path)
    end,
  },

}, {})

-- =========================
-- General Options
-- =========================
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.cmd.colorscheme("catppuccin")

-- Load custom keymaps directory
pcall(require, "keymaps")

-- =========================
-- Global Keymaps
-- =========================
local map = vim.keymap.set

-- Python
map("n", "<leader>r", ":w<CR>:term python3 %<CR>", { desc = "Run Python" })
map("n", "<leader>t", ":split | terminal<CR>", { desc = "Terminal Split" })
map("n", "<leader>v", ":!source .venv/bin/activate<CR>", { desc = "Activate venv" })

-- DAP
map("n", "<F5>", function() require("dap").continue() end)
map("n", "<F10>", function() require("dap").step_over() end)
map("n", "<F11>", function() require("dap").step_into() end)
map("n", "<F12>", function() require("dap").step_out() end)
map("n", "<leader>db", function() require("dap").toggle_breakpoint() end)
map("n", "<leader>dr", function() require("dap").repl.open() end)

-- =========================
-- Auto-format on save
-- =========================
vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = { "*.py" },
  callback = function()
    require("conform").format({ lsp_fallback = true })
    require("lint").try_lint()
  end,
})

```
4. Save (`:w`) and restart Neovim
___
### **3️⃣ Folder Structure**
```plain text
~/.config/nvim/
├─ init.lua
├─ lua/
│  ├─ plugins/
│  │  └─ python.lua      -- Python plugins
│  ├─ keymaps/
│  │  └─ python.lua      -- Python keymaps
│  └─ settings.lua       -- general options


```
___
### **4️⃣ Global Settings (**`**lua/settings.lua**`**)**
```lua
-- =========================
-- OPTIONS
-- =========================

vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.cmd.colorscheme("catppuccin")


```
___
### **5️⃣ Python Plugins (**`**lua/plugins/python.lua**`**)**
```lua
-- =========================
-- PYTHON PLUGINS
-- =========================

return {
  -- LSP: Pyright
  {
    "neovim/nvim-lspconfig",
    opts = { servers = { pyright = { settings = { python = { pythonPath = "python3" } } } } },
  },

  -- Formatter: Black
  { "stevearc/conform.nvim", opts = { format_on_save = true, formatters_by_ft = { python = { "black" } } } },

  -- Linter: Ruff
  { "mfussenegger/nvim-lint", opts = { linters_by_ft = { python = { "ruff" } } } },

  -- Debugger: DAP + nvim-dap-python
  { "mfussenegger/nvim-dap" },
  {
    "mfussenegger/nvim-dap-python",
    ft = "python",
    dependencies = { "mfussenegger/nvim-dap" },
    config = function()
      local debugpy_path = vim.fn.expand("~/.local/share/nvim/mason/packages/debugpy/venv/bin/python")
      require("dap-python").setup(debugpy_path)
    end,
  },

  -- Autoformat + lint on save
  {
    "williamboman/mason-lspconfig.nvim",
    config = function()
      vim.api.nvim_create_autocmd("BufWritePre", {
        pattern = { "*.py" },
        callback = function()
          require("conform").format({ lsp_fallback = true })
          require("lint").try_lint()
        end,
      })
    end,
  },
}


```
___
### **6️⃣ Python Keymaps (**`**lua/keymaps/python.lua**`**)**
```lua
-- =========================
-- PYTHON KEYMAPS
-- =========================

local map = vim.keymap.set

-- Run Python file
map("n", "<leader>r", ":w<CR>:term python3 %<CR>", { desc = "Run Python File" })

-- Open terminal split
map("n", "<leader>t", ":split | terminal<CR>", { desc = "Open Terminal Split" })

-- Activate virtualenv
map("n", "<leader>v", function()
  vim.cmd("split | terminal")
  vim.fn.chansend(vim.b.terminal_job_id, "source .venv/bin/activate\n")
end, { desc = "Activate Python venv" })

-- Debugging (DAP)
map("n", "<F5>", function() require("dap").continue() end, { desc = "DAP Continue" })
map("n", "<F10>", function() require("dap").step_over() end, { desc = "DAP Step Over" })
map("n", "<F11>", function() require("dap").step_into() end, { desc = "DAP Step Into" })
map("n", "<F12>", function() require("dap").step_out() end, { desc = "DAP Step Out" })
map("n", "<leader>db", function() require("dap").toggle_breakpoint() end, { desc = "Toggle Breakpoint" })
map("n", "<leader>dr", function() require("dap").repl.open() end, { desc = "Open DAP REPL" })


```
___
### **7️⃣ Telescope Keymaps (File Management)**
```lua
-- =========================
-- TELESCOPE KEYMAPS
-- =========================

local map = vim.keymap.set
map("n", "<leader>ff", "<cmd>Telescope find_files<cr>")
map("n", "<leader>fg", "<cmd>Telescope live_grep<cr>")
map("n", "<leader>fb", "<cmd>Telescope buffers<cr>")
map("n", "<leader>fh", "<cmd>Telescope help_tags<cr>")
map("n", "<leader>fn", function()
  local f = vim.fn.input("New file: ")
  if f ~= "" then vim.cmd("e " .. f) end
end)


```
___
### **8️⃣ Git Integration**
- LazyVim comes with **Lazygit integration**:
```plain text
<leader>gg  -- Open Lazygit


```
- Stage, commit, push, pull directly inside Neovim
___
### **9️⃣ Creating & Running a Python File**
5. **Create file:** `<leader>ff` → type `src/main.py` → Enter
6. **Save file:** `:w` (autoformats + lints)
7. **Run file:** `<leader>r` (opens terminal split, runs Python)
8. **Activate virtualenv:** `<leader>v`
9. **Debug:** F5-F12 / `<leader>db` / `<leader>dr`
___
### **🔧 Recommended Workflow**
```plain text
Create file → Save → Autoformat/lint → Run → Debug → Commit to Git


```
- Save often to autoformat
- Use virtualenv per project
- Lazygit (`<leader>gg`) handles Git without leaving Neovim
___
### **🔑 Key Cheat Sheet**

|Action|Keymap|
|---|---|
|Run Python file|`<leader>r`|
|Open terminal split|`<leader>t`|
|Activate virtualenv|`<leader>v`|
|Debug continue|`F5`|
|Debug step over|`F10`|
|Debug step into|`F11`|
|Debug step out|`F12`|
|Toggle breakpoint|`<leader>db`|
|Open DAP REPL|`<leader>dr`|
|Find files (Telescope)|`<leader>ff`|
|Live grep (Telescope)|`<leader>fg`|
|Buffers (Telescope)|`<leader>fb`|
|Help tags (Telescope)|`<leader>fh`|
|New file|`<leader>fn`|
|Lazygit|`<leader>gg`|
___
This setup gives you a **full Python IDE experience** in Neovim:
- Syntax-aware **LSP with Pyright**
- **Black + Ruff** on save
- **DAP debugging**
- **Telescope file navigation**
- **Git workflow** with Lazygit
- **Python virtualenv support**

## Working with Python File in Neovim

This guide walks you through:
- Creating a new Python file
- Running Python code
- Activating virtual environments
- Debugging with DAP
- Autoformatting and linting on save
___
### **1️⃣ Open Neovim in your project**
```bash
nvim .


```
This opens your project folder.
___
### **2️⃣ Create a new Python file**
#### Option A: Using Telescope
10. Press `<leader>fn` (`SPACE + f + n`)
11. A buffer will be created as [No Name]
12. Use :w and Type the file path to save as a new Python file, e.g.:
```plain text
:w src/main.py
```
#### Option B: Direct command
```plain text
:new src/main.py


```
> :new = touch new empty file

💡 :!rm src/main.py

This to delete a specific file, in this case delete main.py
___
### **3️⃣ Save your file**
```plain text
:w


```
- Saves changes
- Triggers **autoformat + Ruff lint** if `.py` file
___
### **4️⃣ Run Python code**
Press:
```plain text
<leader>r
```
- `<leader>` = SPACE
- Runs the current file in a terminal split
- Saves automatically before running
___
### **5️⃣ Open a terminal split**
Press:
```plain text
<leader>t


```
- Opens a terminal in a horizontal split
- Useful for running commands manually
___
### **6️⃣ Activate virtual environment**
Press:
```plain text
<leader>v


```
- Opens a terminal and runs:
```bash
source .venv/bin/activate


```
> Assumes your project venv is in .venv/
- Now your Python commands use the virtualenv
___
### **7️⃣ Debug Python code with DAP**
- Place cursor in file
- Press **F5** → Run/debug current file
- Step over: **F10**
- Step into: **F11**
- Step out: **F12**
- Toggle breakpoint: `<leader>db`
- Open DAP REPL: `<leader>dr`
___
### **8️⃣ Autoformat & Lint on Save**
- When you save a Python file:
```plain text
:w
```
- Automatically formats with **Black**
- Lints with **Ruff**
- No extra commands needed
___
### **9️⃣ Optional: Keymap Cheatsheet**

|Action|Keymap|
|---|---|
|Run Python file|`<leader>r`|
|Open terminal split|`<leader>t`|
|Activate virtualenv|`<leader>v`|
|Debug (DAP) continue|`F5`|
|Debug step over|`F10`|
|Debug step into|`F11`|
|Debug step out|`F12`|
|Toggle breakpoint|`<leader>db`|
|Open DAP REPL|`<leader>dr`|
|Find files (Telescope)|`<leader>ff`|
|Live grep (Telescope)|`<leader>fg`|
|Buffers (Telescope)|`<leader>fb`|
|Help tags (Telescope)|`<leader>fh`|
|New file|`<leader>fn`|
___
### **🔧 Tips for Beginners**
- Always create a `.venv` per project
- Save files often (`:w`) to autoformat
- Use `<leader>ff` to quickly navigate files
- Debugging is safer than `print()` for large projects
- Lazygit integration (`<leader>gg`) works alongside this IDE

## 🚀 Git Setup
13. **Generate SSH Key (if not exist)**
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519


```
14. **Add key to GitHub**
Copy your key:
```bash
cat ~/.ssh/id_ed25519.pub


```
- Paste in **GitHub → Settings → SSH & GPG keys → New SSH key**
15. **Test connection**
```bash
ssh -T git@github.com


```
16. **Lazygit inside Neovim**
```plain text
<leader>gg  -- opens Lazygit interface


```
- Stage, commit, push, pull without leaving Neovim
___
### **9️⃣ Beginner Workflow**

|Step|Keymap / Command|Description|
|---|---|---|
|Create new file|`<leader>fn` or Telescope `<leader>ff`|Creates `src/main.py`|
|Save & autoformat|`:w`|Runs Black + Ruff|
|Run Python|`<leader>r`|Runs current file in terminal split|
|Terminal|`<leader>t`|Open shell inside Neovim|
|Activate venv|`<leader>v`|Activate project `.venv`|
|Debug|F5-F12, `<leader>db`, `<leader>dr`|DAP debugging|
|Git|`<leader>gg`|Open Lazygit, stage/commit/push|
___
### **🔧 Recommended Workflow**
```plain text
Create file → Save (autoformat + lint) → Run → Debug → Commit → Push


```
- Always save (`:w`) before running
- Keep a `.venv` per project
- Use Lazygit to manage commits and branches

## 🐙 **Lazygit Guide for Neovim (LazyVim + Python IDE)**
Lazygit is a terminal UI for Git. With LazyVim, you can open it directly in Neovim.
___
### **1️⃣ Open Lazygit in Neovim**
- Press:
```plain text
<leader>gg


```
- `<leader>` = `SPACE` by default
- Opens Lazygit in a split or floating terminal
- Works in your project root folder
___
### **2️⃣ Main Lazygit Panels**
When you open Lazygit:
17. **Branches Panel**: Shows all Git branches
18. **Files Panel**: Shows tracked, modified, untracked files
19. **Staging Panel**: Shows staged files ready to commit
20. **Commit Panel**: Enter commit messages
21. **Logs Panel**: Shows commit history
Use **arrow keys** or `hjkl` to navigate.
___
### **3️⃣ Basic Workflow**
#### **A) Stage Files**
22. Navigate to a modified/untracked file in the **Files Panel**
23. Press `Space` → stage the file
24. Staged files move to **Staging Panel**
___
#### **B) Commit Changes**
25. Press `c` → opens commit message input
26. Type your commit message
27. Press `Enter` → commit changes
___
#### **C) Push Changes**
28. Press `P` → select `Push`
29. Push to the remote repository
> Make sure your SSH key is added to GitHub (ssh-add ~/.ssh/id_ed25519)
___
#### **D) Pull / Fetch Changes**
30. Press `F` → select `Pull` or `Fetch`
31. Pulls changes from remote into your local branch
___
#### **E) Checkout Branch / Create Branch**
- Press `b` → list branches
- Press `n` → create a new branch
- Press `Enter` → switch to a branch
___
#### **F) View Commit Logs**
- Press `l` → opens commit logs
- Press `Enter` → view details of a commit
___
### **4️⃣ Useful Lazygit Shortcuts**

|Action|Key|
|---|---|
|Stage file|`Space`|
|Unstage file|`u`|
|Commit staged changes|`c`|
|Push to remote|`P`|
|Pull from remote|`F`|
|Checkout branch|`b`|
|Create new branch|`n`|
|View commit logs|`l`|
|Quit Lazygit|`q`|
___
### **5️⃣ Tips for Beginners**
- Always open Lazygit in the **project root folder**
- Use **stage → commit → push** for small, frequent commits
- Combine with `<leader>r` in Python IDE workflow:
```plain text
Edit Python file → Save (:w) → Run (<leader>r) → Commit & Push (<leader>gg)


```
- Lazygit is fully keyboard-driven → no mouse needed

## 🧠 Neovim Cheat Sheet
### Yanking (Copy) & Deleting
___
### 🔑 Core Concepts
- **Yank = Copy**
- **Delete = Cut**
- **Put = Paste**
- Everything uses **operators + motions**
___
### 📋 YANKING (COPY)
#### ⚡ Quick Yank

|Action|Command|
|---|---|
|Yank current line|`yy`|
|Yank N lines|`5yy`|
|Yank word|`yw`|
|Yank to end of line|`y$`|
|Yank whole file|`:%y`|
___
#### 🎯 Yank with Motions (Precise)

|What|Command|
|---|---|
|Yank inside quotes|`yi"`|
|Yank inside brackets|`yi(`|
|Yank paragraph|`yap`|
|Yank function (Treesitter)|`yaf`|
|Yank around word|`yaw`|
___
#### 👁 Visual Yank

|Mode|Command|
|---|---|
|Line-wise|`V → y`|
|Character-wise|`v → y`|
|Block-wise|`Ctrl + v → y`|
___
### 📋 SYSTEM CLIPBOARD (IMPORTANT)

|Action|Command|
|---|---|
|Yank to system clipboard|`"+y`|
|Yank line to clipboard|`"+yy`|
|Paste from clipboard|`"+p`|
💡 Use this when copying into **Notion, browser, terminal, Slack**, etc.
___
### 🗂 REGISTERS (ADVANCED)

|Register|Purpose|
|---|---|
|`"`|Default|
|`+`|System clipboard|
|`0`|**Last yank only**|
|`1–9`|Delete history|
|`_`|Black hole (discard)|
#### Paste last yank (safe)
```plain text
"0p


```
___
### 🧹 DELETING (CUT)
#### ⚡ Quick Delete

|Action|Command|
|---|---|
|Delete line|`dd`|
|Delete N lines|`5dd`|
|Delete word|`dw`|
|Delete to end of line|`d$`|
|Delete whole file|`:%d`|
___
#### 🎯 Delete with Motions

|What|Command|
|---|---|
|Delete inside quotes|`di"`|
|Delete inside brackets|`di(`|
|Delete paragraph|`dap`|
|Delete function|`daf`|
___
#### 🚫 Delete Without Overwriting Yank (VERY IMPORTANT)

|Action|Command|
|---|---|
|Delete safely|`"_dd`|
|Delete selection safely|`"_d`|
👉 Prevents losing copied text.
___
### 📥 PASTING (PUT)

|Action|Command|
|---|---|
|Paste after cursor|`p`|
|Paste before cursor|`P`|
|Paste from clipboard|`"+p`|
|Paste last yank only|`"0p`|
___
### 🔥 FAST WORKFLOWS
#### Copy → Delete → Paste (Safe)
```plain text
yy
"_dd
p


```
#### Replace line with clipboard
```plain text
"_dd
"+p


```
___
### 🧠 PRO TIPS
- `.` → repeat last delete/yank
- `gv` → reselect last visual selection
- `"_d` → delete without touching clipboard
- `yaf` / `daf` → function-aware editing (Treesitter)
___
### 🏆 MOST USED (MEMORIZE THESE)
```plain text
yydd      p
yw      dw
yi"     di"
"+y     "+p
"_dd
"0p

```