# Tech Context
Браузер (Chrome/Edge/Firefox). Запуск — открыть `index.html`. Сборки и серверной части нет.
`paketbalan.html` требует `DecompressionStream` и WebAssembly (Chrome/Edge 80+, Firefox 113+). Обновить встроенный 7-Zip: `npm pack 7z-wasm@<версия>`, распаковать, `python3 tools/embed-7z.py <папка>/package`.

## Команды на сервере (проверенные; писать владелице блоком `# 1. …`, см. CLAUDE.md п. 7)

Сервер: root@8314715-nw871204 (Timeweb). Здесь фиксируем реальные пути репозитория, имя службы, пользователя, логи и команды деплоя/диагностики этого проекта. Вносить только то, что подтверждено успешным выводом или взято из `deploy/`; на каждый новый путь или команду, которые оказались верными, — сразу запись сюда. Секреты не записывать.

Опубликовано на сервере: **https://meotida.salamashkina.ru/markirovka/** («Маркировочный стол») и **https://meotida.salamashkina.ru/ldnr/** («ЛДНР в ЭДО без кодов» — отдельная страница, файл `ldnr.html`), с 30.10.2026 (после слияния и запуска скрипта) — **https://meotida.salamashkina.ru/paketbalan/** («Пакеты Балан», файл `paketbalan.html`, строка `paketbalan|meotida_3|-|paketbalan.html`) — nginx + сертификат Let's Encrypt. Настраивает всё скрипт `deploy/publish-sites.sh` в репозитории `meotida_2` (таблица путей и факты сервера — в его `memory-bank/techContext.md`); с 26.10.2026 скрипт принимает 4-е поле в строке `SITES` — имя файла в репозитории (по умолчанию `index.html`), так `/ldnr/` публикуется из `ldnr.html` репозитория `meotida_3`. На сервере: страницы `/var/www/apps/<путь>/index.html`, код — `/opt/sites-src/meotida_3`. Проверено владелицей 2026-10-01: ответ 200, повторный запуск скрипта тоже.

Обновить сайт после изменений в `main` этого репозитория (проверено владелицей 2026-10-01):

```bash
# 1. Подтянуть main и запустить скрипт публикации из клона на сервере
git -C /opt/sites-src/meotida_2 pull -q origin main && bash /opt/sites-src/meotida_2/deploy/publish-sites.sh   # ожидается: в конце 5 путей и главная → 200
# 2. Проверить
curl -sI https://meotida.salamashkina.ru/markirovka/ | head -3   # ожидается: HTTP/1.1 200 OK
```
Не скачивать скрипт по ссылке `raw.githubusercontent.com` сразу после слияния: она кэшируется несколько минут и отдаёт старую версию. Главная страница со списком всех приложений — `https://meotida.salamashkina.ru/` (источник — `meotida_2/deploy/home/index.html`).
Vercel остаётся запасным вариантом (в РФ часто недоступен из-за РКН).
