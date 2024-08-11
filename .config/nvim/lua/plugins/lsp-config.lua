return {
  {
    "williamboman/mason.nvim",
    lazy = false,
    opts = {
      ensure_installed = {
        "lua-language-server",
        "typescript-language-server",
        "prettierd",
        "html-lsp",
        "css-lsp",
        "clangd",
        "clang-format",
        "tailwindcss-language-server",
      }
    },
    config = function()
      require("mason").setup()
    end,
  },
  {
    "williamboman/mason-lspconfig.nvim",
    lazy = false,
    opts = {
      auto_install = true,
    },
  },
  {
    "neovim/nvim-lspconfig",
    lazy = false,
    config = function()
      local capabilities = require('cmp_nvim_lsp').default_capabilities()

      local lspconfig = require("lspconfig")
      lspconfig.tailwindcss.setup({
        capabilities = capabilities
      })
      lspconfig.tsserver.setup({
        capabilities = capabilities
      })
      lspconfig.html.setup({
        capabilities = capabilities
      })
      lspconfig.lua_ls.setup({
        capabilities = capabilities
      })
      lspconfig.gdscript.setup({
        capabilities = capabilities
      })
      lspconfig.clangd.setup({
        on_attach = function(client, bufnr)
          client.server_capabilities.signatureHelpProvider = false
        end,
        capabilities = capabilities
      })

      vim.keymap.set("n", "K", vim.lsp.buf.hover, {})
      vim.keymap.set("n", "<leader>gd", vim.lsp.buf.definition, {})
      vim.keymap.set("n", "<leader>gr", vim.lsp.buf.references, {})
      vim.keymap.set("n", "<leader>ca", vim.lsp.buf.code_action, {})
    end,
  },
}
