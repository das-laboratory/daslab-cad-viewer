#!/usr/bin/env bash
# 웹 버전(cad-viewer.daslab.co.kr) 배포: 빌드한 dist/site/ 를 gh-pages 브랜치에 올립니다.
# 사용법: npm install && bash scripts/publish_site.sh
set -euo pipefail
cd "$(dirname "$0")/.."
python3 build.py
SRC_SHA="$(git rev-parse --short HEAD)"
TMP="$(mktemp -d)"
cp -a dist/site/. "$TMP/"
cd "$TMP"
git init -q -b gh-pages
git add -A
git -c user.name="$(git -C "$OLDPWD" config user.name)" -c user.email="$(git -C "$OLDPWD" config user.email)" \
  commit -q -m "웹 버전 배포 (main ${SRC_SHA})"
git push -f "$(git -C "$OLDPWD" remote get-url origin)" gh-pages:gh-pages
echo "gh-pages 배포 완료 → https://$(cat CNAME)"
