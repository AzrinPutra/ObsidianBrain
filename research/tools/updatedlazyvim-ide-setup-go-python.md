---
title: (Updated)LazyVim IDE Setup – Go + Python
path: "(Updated)LazyVim IDE Setup – Go + Python"
url: https://www.notion.so/Updated-LazyVim-IDE-Setup-Go-Python-2c8bd926b4e480cdaa5cc991f24cc801
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2026-02-15T14:06:00.000Z
---

# (Updated)LazyVim IDE Setup – Go + Python
## Guide
___
### **1. Prerequisites**
- [ ] **Install Homebrew** (macOS)
<details>
<summary>⚠️ Troubleshooting</summary>
- Ensure `/usr/local/bin` or `/opt/homebrew/bin` is in your PATH.
</details>
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


```
- [ ] **Install Go**
<details>
<summary>⚠️ Troubleshooting</summary>
- Make sure `$GOPATH/bin` is in your PATH: ```bash export PATH=$PATH:$(go env GOPATH)/bin ```
- Verify with `which go`.
</details>
```bash
brew install go
go version
go env GOPATH


```
- [ ] **Install Python**
<details>
<summary>⚠️ Troubleshooting</summary>
- Optional: create a virtual environment for projects: ```bash python3 -m venv .venv source .venv/bin/activate ```
</details>
```bash
brew install python
python3 --version


```
___
### **2. Install Language Tools**
#### Go Tools
- [ ] `gopls` (LSP)
```bash
go install golang.org/x/tools/gopls@latest


```
- [ ] `golangci-lint` (Linter)
```bash
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest


```
- [ ] Verify installations:
```bash
which gopls
which golangci-lint


```
#### Python Tools
- [ ] Install:
```bash
pip install black ruff debugpy


```
- [ ] Verify:
```bash
which black
which ruff
which python


```
___
### **3. Neovim Setup**
- [ ] Ensure Neovim ≥ 0.8
```bash
nvim --version


```
- [ ] Install LazyVim
```bash
git clone https://github.com/LazyVim/LazyVim ~/.config/nvim


```
- [ ] Add Go bin to `init.lua`:
```lua
vim.env.PATH = vim.env.PATH .. ":" .. vim.fn.expand("~") .. "/go/bin"


```
___
### **4. Plugins & LSP Setup**
- [ ] Install plugins:
	- LazyVim core
	- Catppuccin theme
	- Telescope
	- Treesitter
	- `ray-x/go.nvim`
	- `nvim-lspconfig`
	- `nvim-lint`
	- `conform.nvim`
	- `nvim-dap`, `nvim-dap-go`, `nvim-dap-python`
- [ ] Treesitter parsers:
```plain text
:TSUpdate go python


```
- [ ] Configure LSP (`gopls`, `pyright`) in `init.lua`.
<details>
<summary>⚠️ Troubleshooting</summary>
- If Treesitter fails: run `:TSUpdate go python`.
- If LSP doesn’t attach: ensure file is in a module folder (`go.mod` for Go, `.venv` for Python).
</details>
___
### **5. Formatter & Linter**
- [ ] Formatters:
	- Go: `goimports`, `gofmt`
	- Python: `black`
- [ ] Linters:
	- Go: `golangci-lint`
	- Python: `ruff`
- [ ] Auto-format & lint on save:
```lua
vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = {"*.go","*.py"},
  callback = function()
    require("lint").try_lint()
    vim.lsp.buf.format({timeout_ms=2000})
  end
})


```
<details>
<summary>⚠️ Common Errors</summary>
- `Linter not found`: Check `$PATH` and executable name.
- `Go module missing`: run `go mod init github.com/username/projectname`.
- `Parser could not be created`: run `:TSUpdate go python`.
</details>
___
### **6. Debugging Setup**
#### Go DAP
- [ ] Install Delve:
```bash
brew install delve
dlv version


```
- [ ] Configure `nvim-dap-go` in `init.lua`.
#### Python DAP
- [ ] Configure `nvim-dap-python` in `init.lua`.
<details>
<summary>⚠️ Common Errors</summary>
- `Parser could not be created`: run `:TSUpdate go python`.
- `Test redeclared`: Use `*_test.go` for test functions.
- `Go module missing`: run `go mod init` in project root.
</details>
___
### **7. Keymaps (Optional)**
**Go**
- `<leader>gr` → Go Run
- `<leader>gt` → Go Test
- `<leader>gb` → Go Build
- `<leader>gi` → Go Install Deps
**Debugging**
- F5 → Continue
- F10 → Step Over
- F11 → Step Into
- F12 → Step Out
- `<leader>db` → Toggle Breakpoint
- `<leader>dr` → Open REPL
**Python**
- `<leader>r` → Run current file
- `<leader>t` → Terminal split
- `<leader>v` → Activate virtualenv
___
### ✅ **8. Final **`**init.lua**`
```lua
-- =========================
-- LazyVim + Python + Go IDE
-- =========================

-- Load Go binaries
vim.env.PATH = vim.env.PATH .. ":" .. vim.fn.expand("~") .. "/go/bin"

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
      integrations = { lualine = true, telescope = true, treesitter = true },
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
      ensure_installed = { "python", "lua", "json", "bash", "go" },
    },
  },

  -- Lualine
  {
    "nvim-lualine/lualine.nvim",
    opts = {
      options = { theme = "catppuccin", section_separators = "", component_separators = "" }
    },
  },

  -- Neo-tree (do not auto-open)
  {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    dependencies = { "nvim-lua/plenary.nvim", "nvim-tree/nvim-web-devicons", "MunifTanjim/nui.nvim" },
    opts = { filesystem = { hijack_netrw_behavior = "disabled", bind_to_cwd = false }, window = { auto_open = false } },
  },

  -- Autocomplete
  {
    "hrsh7th/nvim-cmp",
    dependencies = { "hrsh7th/cmp-nvim-lsp", "L3MON4D3/LuaSnip", "saadparwaiz1/cmp_luasnip" },
  },

  -- Go development
  {
    "ray-x/go.nvim",
    ft = { "go", "gomod" },
    dependencies = { "ray-x/guihua.lua", "neovim/nvim-lspconfig", "nvim-treesitter/nvim-treesitter" },
    config = function()
      require("go").setup({ gofmt = "goimports", lsp_on_attach = true, lsp_cfg = false })
    end,
  },

  -- Python & Go LSP
  {
    "neovim/nvim-lspconfig",
    config = function()
      local lspconfig = require("lspconfig")
      lspconfig.pyright.setup({})
      lspconfig.gopls.setup({
        settings = { gopls = { analyses = { unusedparams = true, shadow = true }, staticcheck = true } }
      })
    end,
  },

  -- nvim-lint with golangci-lint
  {
    "mfussenegger/nvim-lint",
    config = function()
      local lint = require("lint")

      -- Register golangci-lint
      lint.linters.golangci_lint = {
        cmd = "golangci-lint",
        stdin = false,
        args = { "run", "--out-format", "json", "--path-prefix", vim.fn.getcwd() },
        stream = "stdout",
        parser = require("lint.parser").from_json({
          source = "Pos",
          severity = "Severity",
          message = "Text",
          check = function(diag) return diag.Source == "golangci-lint" end,
        }),
      }

      lint.linters_by_ft = { python = { "ruff" }, go = { "golangci_lint" } }
    end,
  },

  -- Black Formatter
  {
    "stevearc/conform.nvim",
    opts = { formatters_by_ft = { python = { "black" }, go = { "goimports", "gofmt" } } },
  },

  -- DAP
  { "mfussenegger/nvim-dap" },

  -- Python DAP
  {
    "mfussenegger/nvim-dap-python",
    ft = "python",
    dependencies = { "mfussenegger/nvim-dap" },
    config = function()
      local path = vim.fn.expand("~/.local/share/nvim/mason/packages/debugpy/venv/bin/python")
      require("dap-python").setup(path)
    end,
  },

  -- Go DAP
  {
    "leoluz/nvim-dap-go",
    ft = "go",
    dependencies = { "mfussenegger/nvim-dap" },
    config = function()
      require("dap-go").setup()
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

-- Load custom keymaps
pcall(require, "keymaps")

-- =========================
-- Keymaps
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
-- Go
map("n", "<leader>gr", ":GoRun<CR>", { desc = "Go Run" })
map("n", "<leader>gt", ":GoTest<CR>", { desc = "Go Test" })
map("n", "<leader>gb", ":GoBuild<CR>", { desc = "Go Build" })
map("n", "<leader>gi", ":GoInstallDeps<CR>", { desc = "Go Install Deps" })

-- =========================
-- Autoformat on save
-- =========================
vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = { "*.py", "*.go" },
  callback = function()
    if vim.bo.filetype == "python" then
      require("conform").format({ lsp_fallback = true })
      require("lint").try_lint()
    elseif vim.bo.filetype == "go" then
      require("lint").try_lint()
      vim.lsp.buf.format({ timeout_ms = 2000 })
    end
  end,
})

```
