vim.cmd("set expandtab")
vim.cmd("set tabstop=4")
vim.cmd("set softtabstop=2")
vim.cmd("set shiftwidth=2")

vim.cmd("set number")
vim.cmd("set relativenumber")

-- setting leader
vim.g.mapleader = " "

vim.cmd("set clipboard=unnamedplus")

------------------------------------ keymaps
-- to change tab
vim.api.nvim_set_keymap("n", "<leader>b", ":BufferLinePick<CR>" ,{desc = "to change tab"})

-- to close current tab
vim.api.nvim_set_keymap("n", "<leader>X", ":bd<CR>" ,{desc = "to close current tab"})

-- to save current tab
vim.api.nvim_set_keymap("n", "<C-s>", ":w<CR>" ,{desc = "to save current tab"})


-- navigation key maps for nvim
vim.keymap.set('n', '<c-k>', ':wincmd k<CR>')
vim.keymap.set('n', '<c-j>', ':wincmd j<CR>')
vim.keymap.set('n', '<c-h>', ':wincmd h<CR>')
vim.keymap.set('n', '<c-l>', ':wincmd l<CR>')
