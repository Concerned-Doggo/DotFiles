
-- setting our vim options
require("vim-options")

-- adding lazy.nvim package manager
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- loads all the from ./lua/plugins/ directory
require("lazy").setup("plugins")

local opts = {}


-- loading our lazy.nvim config
require("lazy").setup(plugins, opts)

