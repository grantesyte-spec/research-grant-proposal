#!/usr/bin/env python3
"""
Create GitHub repository and push skill
创建GitHub仓库并推送skill

Usage:
    python create_github_repo.py --username "your-github-username" --token "ghp_xxxxx"
    python create_github_repo.py --interactive
"""

import argparse
import subprocess
import sys
import os

def run_command(cmd, check=True):
    """Run shell command."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        print(f"   Error: {result.stderr}")
        sys.exit(1)
    return result

def create_repo_gh(username, token, repo_name, description=""):
    """Create repo using GitHub API via curl."""
    import json
    
    print(f"📦 创建仓库: {username}/{repo_name}")
    
    # Create repository using API
    api_cmd = f'''curl -X POST -H "Authorization: token {token}" \
      -H "Accept: application/vnd.github.v3+json" \
      https://api.github.com/user/repos \
      -d '{{"name":"{repo_name}","description":"{description}","private":false}}' '''
    
    result = run_command(api_cmd, check=False)
    
    if "already exists" in result.stdout or result.returncode == 0:
        print(f"✅ 仓库已存在或创建成功")
    else:
        print(f"⚠️  API响应: {result.stdout[:200]}")
    
    return True

def push_to_github(username, token, repo_name):
    """Push to GitHub."""
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(skill_dir)
    
    print(f"📤 推送到 GitHub...")
    
    # Set remote with token
    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    
    # Remove existing remote if exists
    run_command("git remote remove origin 2>/dev/null || true")
    
    # Add remote
    run_command(f'git remote add origin "{remote_url}"')
    
    # Push
    result = run_command("git push -u origin main", check=False)
    
    if result.returncode == 0:
        print(f"✅ 推送成功!")
        print(f"   仓库地址: https://github.com/{username}/{repo_name}")
    else:
        print(f"❌ 推送失败")
        print(f"   请手动运行: git push https://{token}@github.com/{username}/{repo_name}.git main")
    
    return result.returncode == 0

def interactive_mode():
    """Interactive mode."""
    print("\n🚀 GitHub 仓库创建工具")
    print("=" * 50)
    
    username = input("请输入 GitHub 用户名: ").strip()
    if not username:
        print("❌ 用户名不能为空")
        return
    
    token = input("请输入 GitHub Personal Access Token: ").strip()
    if not token:
        print("❌ Token 不能为空")
        print("   获取方式: https://github.com/settings/tokens")
        print("   权限要求: repo")
        return
    
    repo_name = input("仓库名 (直接回车使用默认名): ").strip()
    if not repo_name:
        repo_name = "research-grant-proposal"
    
    description = input("仓库描述 (可选): ").strip()
    
    print(f"\n📋 配置:")
    print(f"   用户名: {username}")
    print(f"   仓库名: {repo_name}")
    print(f"   描述: {description or '无'}")
    print("")
    
    # Create and push
    create_repo_gh(username, token, repo_name, description)
    push_to_github(username, token, repo_name)

def main():
    parser = argparse.ArgumentParser(description='创建GitHub仓库并推送skill')
    parser.add_argument('--username', '-u', help='GitHub用户名')
    parser.add_argument('--token', '-t', help='GitHub Personal Access Token')
    parser.add_argument('--repo', '-r', help='仓库名', default='research-grant-proposal')
    parser.add_argument('--interactive', '-i', action='store_true', help='交互模式')
    parser.add_argument('--description', '-d', help='仓库描述', 
                        default='A Claude/Codex skill for generating academic research grant proposals in Chinese')
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
    elif args.username and args.token:
        create_repo_gh(args.username, args.token, args.repo, args.description)
        push_to_github(args.username, args.token, args.repo)
    else:
        parser.print_help()
        print("\n💡 提示:")
        print("   1. 先获取 Personal Access Token:")
        print("      https://github.com/settings/tokens")
        print("   2. 运行:")
        print(f"      python {sys.argv[0]} -u YOUR_USERNAME -t YOUR_TOKEN -r {args.repo}")
        print("   或者使用交互模式:")
        print(f"      python {sys.argv[0]} --interactive")

if __name__ == '__main__':
    main()
