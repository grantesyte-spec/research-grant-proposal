# CNKI 文献验证步骤

## 适用范围
- 中国知网（CNKI）学术文献检索
- 验证中文护理研究文献

## 验证目标
- ✅ TOPIC：文献主题与研究课题匹配
- ✅ AUTHORS：至少前2-3位作者姓名正确
- ✅ YEAR：出版年份正确
- ⚠️ DOI：部分文献可能无DOI
- ⚠️ 卷期页码：需从详细信息页面获取

## 验证步骤

### 步骤1：打开CNKI高级检索页面
```bash
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
```

### 步骤2：获取页面快照（查找搜索框ref）
```bash
openclaw browser --browser-profile chrome snapshot --compact
```
**注意**：搜索框通常为 `ref=e18`，搜索按钮为 `ref=e33`

### 步骤3：输入搜索关键词
```bash
# 简化关键词策略：如果全关键词无结果，尝试逐步简化
openclaw browser --browser-profile chrome type [搜索框ref] "Orem 自理模式 糖尿病"
```

### 步骤4：点击搜索按钮
```bash
openclaw browser --browser-profile chrome click [搜索按钮ref]
```

### 步骤5：等待页面加载（关键！）
```bash
openclaw browser --browser-profile chrome wait --load networkidle
```

### 步骤6：获取搜索结果快照
```bash
openclaw browser --browser-profile chrome snapshot --compact
```
**成功标识**：
- 看到结果数量（如 "共找到 75 条结果"）
- 看到文献列表（标题、作者、期刊、发表时间）

### 步骤7：查看文献详细信息
```bash
# 点击文献标题链接
openclaw browser --browser-profile chrome click [文献ref]

# 等待加载
openclaw browser --browser-profile chrome wait --load networkidle

# 获取详细信息页面
openclaw browser --browser-profile chrome snapshot --compact
```

### 步骤8：提取完整文献信息
从详细信息页面提取：
- ✅ 完整标题
- ✅ 全部作者（注意"显示全部作者"链接）
- ✅ 期刊名称
- ✅ 发表日期（年-月-日）
- ⚠️ 卷期号（如 "28(6)"）
- ⚠️ 页码（如 "45-52"）
- ⚠️ DOI（如有）

## 验证结果记录格式

```markdown
## [序号] [待验证/已验证]

**题目**：[完整标题]
- **作者**：[前3位作者, 等]
- **期刊**：[期刊名称]
- **发表时间**：[YYYY-MM-DD]
- **被引次数**：[数字]
- **验证链接**：[CNKI URL]
- **验证状态**：[TOPIC✓ AUTHORS✓ YEAR✓ 卷期✓ 页码✓ DOI✓]

**手动验证链接**：
- CNKI：https://kns.cnki.net/kcms2/article/abstract?[article_id]
- Google Scholar：https://scholar.google.com/scholar?q="完整标题"
```

## 常见问题处理

### 问题1：搜索无结果
**症状**：`抱歉，暂无数据，请稍后重试。`
**解决方案**：
1. 简化关键词（去掉部分检索词）
2. 尝试：`Orem 自理模式` → `Orem 糖尿病` → `自理模式 糖尿病`
3. 检查是否需要验证码验证

### 问题2：页面元素ref失效
**症状**：`Element "e18" not found`
**解决方案**：
```bash
# 重新获取页面快照
openclaw browser --browser-profile chrome snapshot --compact
# 使用新的ref值
```

### 问题3：ref在导航后变化
**原因**：`Refs are not stable across navigations`
**解决方案**：每次页面变化后必须重新 `snapshot`

### 问题4：部分作者信息隐藏
**原因**：长列表默认折叠
**解决方案**：点击"显示全部作者"链接

### 问题5：缺少卷期页码信息
**原因**：部分期刊文章信息不完整
**解决方案**：
1. 查看HTML阅读版本
2. 使用Google Scholar补充
3. 标记为 `[部分验证]`

## 验证检查清单

执行验证后，确认以下项目：

- [ ] 文献可正常访问
- [ ] 标题与引用一致
- [ ] 前3位作者姓名正确
- [ ] 期刊名称正确
- [ ] 发表年份正确
- [ ] 卷期号已获取（如有）
- [ ] 页码范围已获取（如有）
- [ ] DOI已获取（如有）
- [ ] 验证链接可正常访问

## 注意事项

1. **简化策略**：复杂检索式可能无结果，建议逐步简化
2. **等待时间**：每次页面跳转后必须 `wait --load networkidle`
3. **Ref变化**：导航后ref失效，必须重新获取快照
4. **验证码**：如果出现验证码，可能需要手动处理
5. **信息完整性**：并非所有文献都有完整的DOI和页码信息
