return {
  {
    "nvim-telescope/telescope.nvim",
    tag = "0.1.6",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      local builtin = require("telescope.builtin")
      -- keybind to search through all files present in directory
      vim.keymap.set("n", "<C-p>", builtin.find_files, {})

      -- keybind to search words accross all files
      vim.keymap.set("n", "<leader>fg", builtin.live_grep, {})

      -- keybind to search all the open buffers kinda like alt-tab
      vim.keymap.set("n", "<leader>fb", builtin.buffers, {})
    end,
  },
  {
    "nvim-telescope/telescope-ui-select.nvim",
    config = function()
      require("telescope").setup({
        extensions = {
          ["ui-select"] = {
            require("telescope.themes").get_dropdown({}),
          },
        },
      })
      require("telescope").load_extension("ui-select")
    end,
  },
}
