# System Patterns
Один файл `index.html`, без сервера и внешних зависимостей; сессии хранятся в браузере.
Отдельные страницы — тоже по одному самодостаточному файлу: `ldnr.html` (/ldnr/), `paketbalan.html` (/paketbalan/). В `paketbalan.html` встроен 7-Zip WASM (npm `7z-wasm` 1.2.0: wasm gzip+base64 в `<script id="sevenZipWasm">`, распаковка через `DecompressionStream`; блок между `<!--VENDOR:7z-->` и `<!--/VENDOR:7z-->` перегенерирует `tools/embed-7z.py`) — поэтому файл ~1 МБ; 7-Zip поднимается только при первом архиве, на каждый архив — новый экземпляр модуля.
