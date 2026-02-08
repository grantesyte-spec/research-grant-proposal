#!/bin/bash
# Push skill to GitHub
# Usage: ./push_to_github.sh

set -e

echo "📤 推送到 GitHub..."

cd "$(dirname "$0")"

# 推送到已存在的远程仓库
git push origin main

echo "✅ 推送完成!"
echo "🔗 https://github.com/grantesyte-spec/research-grant-proposal"
