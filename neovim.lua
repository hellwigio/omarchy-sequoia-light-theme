return {
  {
    "bjarneo/aether.nvim",
    branch = "v3",
    name = "aether",
    priority = 1000,
    opts = {
      colors = {
        bg = "#F5F5F7",
        dark_bg = "#E8E8ED",
        darker_bg = "#D1D1D6",
        lighter_bg = "#FFFFFF",

        fg = "#1D1D1F",
        dark_fg = "#8E8E93",
        light_fg = "#3A3A3C",
        bright_fg = "#000000",
        muted = "#8E8E93",

        red = "#FF3B30",
        yellow = "#FFCC00",
        orange = "#FF9500",
        green = "#34C759",
        cyan = "#32ADE6",
        blue = "#007AFF",
        magenta = "#AF52DE",
        brown = "#A2845E",

        bright_red = "#FF6961",
        bright_yellow = "#FFD60A",
        bright_green = "#30D158",
        bright_cyan = "#64D2FF",
        bright_blue = "#0A84FF",
        bright_magenta = "#BF5AF2",

        accent = "#007AFF",
        cursor = "#000000",
        foreground = "#1D1D1F",
        background = "#F5F5F7",
        selection = "#B3D7FF",
        selection_foreground = "#000000",
        selection_background = "#B3D7FF",
      },
    },
  },
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "aether",
    },
  },
}
