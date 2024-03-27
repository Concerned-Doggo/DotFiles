return {
  "ggandor/leap.nvim",
  event = "VeryLazy",
  config = function()
    require('leap').create_default_mappings()
  end
}
