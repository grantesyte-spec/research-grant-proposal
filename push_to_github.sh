#!/bin/bash
# Push skill to GitHub
# Usage: ./push_to_github.sh <github-username> <repo-name>

set -e

USERNAME=${1:-"your-github-username"}
REPO_NAME=${2:-"research-grant-proposal"}

echo "🚀 准备推送到 GitHub..."
echo "   用户名: $USERNAME"
echo "   仓库名: $REPO_NAME"
echo ""

# 检查是否需要创建仓库
echo "📋 请确保在 GitHub 上创建了空仓库: https://github.com/$USERNAME/$REPO_NAME"
echo ""

# 添加远程仓库
echo "🔗 添加远程仓库..."
git remote add origin "https://github.com/$USERNAME/$REPO_NAME.git"

# 推送到GitHub
echo "📤 推送到 GitHub..."
echo "   如果需要认证，请使用以下方式之一:"
echo ""
echo "   方式1: GitHub CLI (推荐)"
echo "   $ gh auth login"
echo "   $ git push -u origin main"
echo ""
echo "   方式2: Personal Access Token"
echo "   $ git push https://<TOKEN>@github.com/$USERNAME/$REPO_NAME.git main"
echo ""
echo "   方式3: SSH"
echo "   $ git remote set-url origin git@github.com:$USERNAME/$REPO_NAME.git"
echo "   $ git push -u origin main"
echo ""

# 检查远程仓库配置
echo "✅ 远程仓库已配置:"
git remote get-url origin
echo ""

# 提示下一步
echo "📝 下一步:"
echo "   1. 获取 GitHub Personal Access Token:"
echo "      https://github.com/settings/tokens → Generate new token → 勾选 'repo'"
echo ""
echo "   2. 运行以下命令:"
echo "      git push https://<YOUR_TOKEN>@github.com/$USERNAME/$REPO_NAME.git main"
echo ""
echo "   或者使用 GitHub CLI:"
echo "      gh auth login"
echo "      git push -u origin main"
