# Sequoia Light — extra-тема Omarchy (macOS Sequoia / Sonoma)

Светлая тема: окна off-white, хром system gray, акцент **System Blue** `#007AFF`, светофор `#FF5F57` / `#FEBC2E` / `#28C840`.

Репозиторий в формате extra-темы Omarchy: файлы темы **в корне** (`colors.toml`, `backgrounds/`, `waybar.css`, …), как у [alabaster](https://github.com/grierson/omarchy-alabaster-theme). `omarchy-theme-install` клонирует git-репо целиком в `~/.config/omarchy/themes/<имя>` и сразу применяет тему — вложенная папка `themes/…` не поддерживается.

Для Дмитрия Лысова / for Dmitriy Lyssov.

---

## Установка одной командой

Как любая extra-тема ([ручной](https://omarchy.org/manual/making-your-own-theme/), скрипт [`omarchy-theme-install`](https://github.com/basecamp/omarchy/blob/master/bin/omarchy-theme-install)):

```bash
omarchy-theme-install https://github.com/hellwigio/omarchy-sequoia-light-theme
```

То же через CLI Omarchy 4:

```bash
omarchy theme install https://github.com/hellwigio/omarchy-sequoia-light-theme
```

Или меню: **Install → Style → Theme**, вставить URL репозитория.

Имя в меню берётся из URL: `omarchy-sequoia-light-theme` → **`sequoia-light`**. Соглашение Omarchy: `omarchy-[имя]-theme`. Опубликуйте этот репозиторий под таким именем (GitHub / любой публичный git) и подставьте свой URL.

Публичный репозиторий: [hellwigio/omarchy-sequoia-light-theme](https://github.com/hellwigio/omarchy-sequoia-light-theme). Клон без логина. В меню тема называется **`sequoia-light`**.

---

## Палитра / Palette

| Role | Hex | Note |
| --- | --- | --- |
| Accent | `#007AFF` | Apple System Blue |
| Window | `#F5F5F7` / `#FFFFFF` | Sequoia off-white |
| Chrome | `#E8E8ED` `#E5E5EA` `#D1D1D6` | System Gray 5–6 |
| Label | `#1D1D1F` | Near-black |
| Mute | `#8E8E93` | System Gray |
| Close / Min / Zoom | `#FF5F57` `#FEBC2E` `#28C840` | Traffic lights |
| Red / Yellow / Green | `#FF3B30` `#FFCC00` `#34C759` | System colors |

---

## Обои

Фото [Unsplash License](https://unsplash.com/license) в `backgrounds/`. Авторы — `backgrounds/CREDITS.md`. Следующие обои: `omarchy-theme-bg-next`. Свои: `~/.config/omarchy/backgrounds/sequoia-light/`.

---

## GTK и иконки

`light.mode` + `mode = "light"` в `colors.toml` — светлая схема и Adwaita. `icons.theme` — **Yaru-blue**.

Опционально скопируйте `gtk.css` в `~/.config/gtk-3.0/gtk.css` и `~/.config/gtk-4.0/gtk.css`. Omarchy этот overlay сам не линкует.

---

## Что внутри

```text
colors.toml          # палитра Omarchy 4 (главный файл)
light.mode           # prefer-light
icons.theme          # Yaru-blue
gtk.css              # опциональный GTK overlay
hyprland.conf        # Omarchy 3
hyprland.lua         # Omarchy 4 (при install из git отбрасывается, см. ниже)
hyprlock.conf
waybar.css
walker.css
mako.ini
swayosd.css
shell.toml
alacritty.toml / kitty.conf / ghostty.conf / foot.ini
btop.theme
neovim.lua
helix.toml
vscode.json
chromium.theme
keyboard.rgb
backgrounds/
preview.png
preview-unlock.png
unlock.png
```

Клон через `omarchy theme install` на Omarchy 4 **не ставит** `*.lua`, конфиги терминалов и `vscode.json` ([политика extra-тем](https://omarchy.org/manual/making-your-own-theme/)): они запускают код. Цвета остаются — их генерируют шаблоны из `colors.toml`. `btop.theme`, `shell.toml`, `waybar.css`, `mako.ini`, обои — остаются.

---

## Sequoia Light — Omarchy extra theme

```bash
omarchy-theme-install https://github.com/hellwigio/omarchy-sequoia-light-theme
```

Repo root is the theme (not a nested `themes/` folder). Name the git repo `omarchy-sequoia-light-theme` so the menu shows `sequoia-light`.
