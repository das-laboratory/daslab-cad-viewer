# DAS Lab 도면 뷰어

설치 없이 브라우저에서 **DWG · DXF · PDF · SVG · 이미지** 도면을 여는 무료 뷰어입니다.
HTML 파일 하나로 동작하고, 인터넷 없이도 열리며, 도면 파일은 사용자 기기 안에서만 처리됩니다.

- **웹에서 바로 쓰기:** https://das-laboratory.github.io/daslab-cad-viewer/
- **파일로 받기 (오프라인용):** [Releases](https://github.com/das-laboratory/daslab-cad-viewer/releases/latest)에서 `daslab-cad-viewer.html`을 받아 더블클릭

만든 곳: [DAS Lab](https://daslab.co.kr) · Instagram [@das_laboratory](https://www.instagram.com/das_laboratory/)

## 기능

- 레이어 켜기/끄기, 확대 · 이동, 커서 좌표 표시
- 거리 재기 — DWG · DXF는 끝점에 자동으로 붙음
- 축척 맞추기 — 길이를 아는 두 점을 찍고 실제 길이를 넣으면 PDF · 이미지에서도 m 단위로 측정
- 지원 형식: DWG(AutoCAD R13~2018 형식 위주 — 일부 파일은 안 열릴 수 있음), DXF(ASCII), PDF(여러 쪽), SVG, PNG · JPG · WebP · GIF

화면 표시와 측정값은 참고용입니다. 실제 설계 · 시공 판단은 원본 CAD 파일에서 확인하세요.

## 빌드

```bash
npm install
python3 build.py
```

| 결과물 | 용도 |
|---|---|
| `dist/daslab-cad-viewer.html` | 단독 실행 파일 (Releases에 올리는 파일) |
| `docs/index.html` | GitHub Pages 웹 버전 (위와 같은 파일) |

## 구성

| 경로 | 내용 |
|---|---|
| `src/viewer.html` | 뷰어 본체 — DXF 파서, 렌더러, 화면 구성 |
| `src/entry.mjs` | DWG 엔진(libredwg-web) 번들 진입점 |
| `assets/` | DAS Lab 로고, 예시 도면 |
| `build.py` | 의존성을 HTML 하나로 묶는 빌드 스크립트 |
| `LICENSE` | GNU GPL v3 전문 |
| `THIRD_PARTY_NOTICES.md` | 함께 쓴 오픈소스 고지 |

## 라이선스

Copyright © 2026 주식회사 다스랩 (DAS Lab)

이 프로그램은 GNU General Public License v3.0 또는 그 이후 버전(GPL-3.0-or-later)으로 배포됩니다.
DWG 읽기에 GPL 라이선스인 LibreDWG를 쓰기 때문에 뷰어 전체가 GPL을 따릅니다.
누구나 자유롭게 쓰고, 고치고, 다시 배포할 수 있습니다. 다시 배포할 때는 같은 라이선스로, 소스 코드와 함께 배포해야 합니다.

‘DAS Lab’ 이름과 로고는 GPL에 포함되지 않습니다 (GPLv3 제7조 e항).
수정본을 배포할 때는 로고를 빼고, 출처 표시로만 이름을 써 주세요.

이 프로그램은 어떤 보증도 없이 제공됩니다 (GPLv3 제15 · 16조).

## 포함된 오픈소스의 원본 소스

| 구성 요소 | 원본 소스 |
|---|---|
| libredwg-web 0.7.15 (LibreDWG 포함) | https://github.com/mlightcad/libredwg-web/tree/v0.7.15 — 커밋 `18588818df66d4258b83fda19aa40fd892cdf49d` |
| PDF.js 3.11.174 | https://github.com/mozilla/pdf.js/tree/v3.11.174 |

DWG 엔진(`libredwg-web.wasm`)은 위 libredwg-web v0.7.15 소스를 그대로 빌드한 npm 패키지 `@mlightcad/libredwg-web@0.7.15`에서 가져옵니다.
자세한 고지는 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)를 보세요.
