# DWG 엔진 원본 소스 보관본

`libredwg-web-v0.7.15-src.tar.xz` 는 이 뷰어에 들어간 DWG 엔진의 대응 소스(Corresponding Source, GPLv3 제6조)입니다.

| 항목 | 값 |
|---|---|
| 원본 | https://github.com/mlightcad/libredwg-web — 태그 `v0.7.15`, 커밋 `18588818df66d4258b83fda19aa40fd892cdf49d` |
| 포함된 서브모듈 | `jsmn` (https://github.com/zserge/jsmn, 커밋 `85695f3d5903b1cd5b4030efe50db3b4f5f3c928`, MIT) |
| 라이선스 | GPL-3.0-or-later (LibreDWG, © Free Software Foundation, Inc.) · GPL-3.0 (libredwg-web, © MLight Lee) |
| 보관본 SHA-256 | `9971bd01435bef85cce341f82525b1a7a276a98c5165c18d375091bd41ca045f` |

크기를 줄이기 위해 아래 두 가지만 뺐습니다. 둘 다 엔진을 빌드하는 데 필요하지 않습니다.

- `test/test-data/` — 테스트용 샘플 도면 (약 53MB)
- `bindings/javascript/wasm/*.wasm` — 빌드 결과물. 이 뷰어가 쓰는 파일과 같은 것입니다 (SHA-256 `431576487027122a28e5ac99d91fe6366f81ecda743a4676878c75c85fe82c53`)

빌드 방법은 압축을 푼 뒤 `bindings/javascript/README.md` 를 따르면 됩니다 (emscripten · automake · pnpm 필요).
