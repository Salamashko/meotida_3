#!/usr/bin/env python3
"""Встраивает 7-Zip (npm-пакет 7z-wasm) в paketbalan.html, чтобы страница распаковывала архивы без внешних файлов.

Запуск:  python3 tools/embed-7z.py ПАПКА_ПАКЕТА [paketbalan.html]
ПАПКА_ПАКЕТА — распакованный `npm pack 7z-wasm@1.2.0` (в ней 7zz.umd.js и 7zz.wasm).
wasm хранится gzip+base64 (≈0,9 МБ вместо 1,6 МБ) и распаковывается в браузере через DecompressionStream.
Заменяет всё между маркерами <!--VENDOR:7z--> и <!--/VENDOR:7z--> (или маркер <!--VENDOR--> при первом запуске).
"""
import base64, gzip, re, sys
from pathlib import Path

pkg = Path(sys.argv[1])
page = Path(sys.argv[2] if len(sys.argv) > 2 else Path(__file__).resolve().parent.parent / "paketbalan.html")
js = (pkg / "7zz.umd.js").read_text(encoding="utf-8")
assert "</script" not in js.lower()
version = __import__("json").loads((pkg / "package.json").read_text())["version"]
b64 = base64.b64encode(gzip.compress((pkg / "7zz.wasm").read_bytes(), 9, mtime=0)).decode()
b64 = "\n".join(b64[i:i + 120] for i in range(0, len(b64), 120))
block = (
    "<!--VENDOR:7z-->\n"
    f"<!-- 7-Zip WASM (npm 7z-wasm {version}, 7-Zip © Igor Pavlov, GNU LGPL + unRAR restriction; https://www.7-zip.org/) -->\n"
    f'<script id="sevenZipWasm" type="application/octet-stream">\n{b64}\n</script>\n'
    f"<script>\n{js}\n</script>\n"
    "<!--/VENDOR:7z-->"
)
html = page.read_text(encoding="utf-8")
new, n = re.subn(r"<!--VENDOR:7z-->.*?<!--/VENDOR:7z-->", lambda m: block, html, flags=re.S)
if not n:
    assert "<!--VENDOR-->" in html, "нет маркера"
    new = html.replace("<!--VENDOR-->", block, 1)
page.write_text(new, encoding="utf-8")
print(f"{page}: {len(new.encode())} байт, 7z-wasm {version}")
