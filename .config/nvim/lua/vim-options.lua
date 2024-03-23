vim.cmd("set expandtab")
vim.cmd("set tabstop=4")
vim.cmd("set softtabstop=2")
vim.cmd("set shiftwidth=2")

vim.cmd("set number")
vim.cmd("set relativenumber")

-- setting leader
vim.g.mapleader = " "


------------------------------------ keymaps
-- to change tab
vim.api.nvim_set_keymap("n", "<leader>b", ":BufferLinePick<CR>" ,{})

-- to close current tab
vim.api.nvim_set_keymap("n", "<leader>X", ":bd<CR>" ,{})

-- to save current tab
vim.api.nvim_set_keymap("n", "<C-s>", ":w<CR>" ,{})
