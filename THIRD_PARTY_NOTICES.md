# 오픈소스 고지 (Third-Party Notices)

DAS Lab 도면 뷰어는 아래 오픈소스를 포함하거나 사용합니다.

| 구성 요소 | 버전 | 라이선스 | 저작권 | 원본 소스 |
|---|---|---|---|---|
| LibreDWG | libredwg-web v0.7.15에 포함된 버전 | GPL-3.0-or-later | © Free Software Foundation, Inc. | https://github.com/mlightcad/libredwg-web/tree/v0.7.15 (upstream: https://github.com/LibreDWG/libredwg) |
| libredwg-web | 0.7.15 (커밋 `18588818df66d4258b83fda19aa40fd892cdf49d`) | GPL-3.0 | © MLight Lee | https://github.com/mlightcad/libredwg-web/tree/v0.7.15 |
| PDF.js (pdfjs-dist) | 3.11.174 | Apache-2.0 | © Mozilla Foundation | https://github.com/mozilla/pdf.js/tree/v3.11.174 |
| IBM Plex Sans KR, IBM Plex Mono | Google Fonts | SIL Open Font License 1.1 | © IBM Corp. | https://github.com/IBM/plex |

- LibreDWG와 libredwg-web은 WebAssembly와 번들 JavaScript 형태로 포함됩니다. 라이선스 전문은 [`LICENSE`](LICENSE)(GNU GPL v3)에 있습니다.
- PDF.js는 `pdf.min.js`와 `pdf.worker.min.js` 형태로 포함되며, 파일 안의 라이선스 주석을 그대로 유지합니다. 라이선스 전문은 [`licenses/Apache-2.0.txt`](licenses/Apache-2.0.txt)에 있습니다.
- IBM Plex 웹폰트는 파일에 포함하지 않고, 인터넷에 연결된 경우에만 Google Fonts에서 불러옵니다.
