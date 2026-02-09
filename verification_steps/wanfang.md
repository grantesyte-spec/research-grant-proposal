# Wanfang Research Script

**Purpose**: Research Chinese literature on Wanfang, generate wanfang_results.md

---

## ⚠️ BROWSER BEST PRACTICES (Critical!)

**Learned from experience:**
1. **Single tab only** - Do NOT open multiple tabs simultaneously
2. **No rapid operations** - Wait between each action
3. **Use `navigate` NOT `open`** - Prevents new tab creation
4. **One URL per session** - Stay on the same tab throughout
5. **If connection lost**: Restart browser service → `open` once → complete all actions

**Correct workflow:**
```bash
# ✅ RIGHT - Single tab, navigate between pages
browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
snapshot  # Get refs
type [ref] "keyword" --submit
wait --load networkidle
snapshot  # Get article refs
navigate "article-url"  # Stay in same tab!

# ❌ WRONG - Multiple opens or click opens new tab
browser open "url1"
browser open "url2"
click [article-ref]  # May open new tab!
```

---

## IMPORTANT

**Search Order**: CNKI FIRST → PubMed SECOND → Wanfang LAST (supplementary)

---

## STEP 0: Break Down Topic

Same keywords as CNKI:
```bash
"Orem 自理模式 护理"
"动机行为转化理论 护理"
"股骨颈骨折 护理"
"糖尿病 护理"
```

---

## STEP 1: Research Phase

### 1.1 Open Wanfang
```bash
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
```

### 1.2 Search
```bash
# Get refs FIRST
snapshot

# Search (find ref from snapshot)
type [search-ref] "Orem 自理模式" --submit
wait --load networkidle
snapshot
```

### 1.3 Search other keywords
```bash
type [ref] "动机行为转化理论 护理" --submit
wait --load networkidle
snapshot
```

---

## STEP 2: Selection Phase

### 2.1 Navigate to article (Stay in same tab!)
```bash
# Option A: Use navigate to article URL
navigate "https://www.wanfangdata.com.cn/details/detail.aspx?FileName=[ID]"
wait --load networkidle
snapshot

# Option B: Click and IMMEDIATELY use navigate instead of new tab
# click [article-ref]  # May open new tab - avoid!
```

### 2.2 Extract citation
```
**Title**: [Full Title]
**Authors**: [First 2-3], et al.
**Journal**: [Journal], [Year]
**URL**: [verification-url]
```

---

## STEP 3: Verification Phase

### 3.1 Verify 5 elements
```bash
# Stay in article tab - NO tab switching needed!
wait --load networkidle
snapshot
```

**Check:**
```
✓ TOPIC: Title matches? YES/NO
✓ AUTHORS: First 2-3 match? YES/NO
✓ YEAR: Year matches? YES/NO
✓ ABSTRACT: Relevant? YES/NO
✓ URL: Accessible? YES/NO
```

---

## STEP 4: Generate Output

**Create wanfang_results.md:**

```markdown
# Wanfang Research Results

## Topic
[Research topic]

## Search Keywords & Results
| Keyword | Results |
|---------|---------|
| Orem 自理模式 护理 | [number] |
| 动机行为转化理论 护理 | [number] |

## Selected References
| # | Title | Authors | Journal | Year | Relevance |
|---|-------|---------|---------|------|-----------|
| 1 | [Title] | [Authors] | [Journal] | [Year] | Medium |

## Verified References

### #1 - VERIFIED ✓
**Title**: [Full Title]
**Authors**: [Authors]
**Journal**: [Journal], [Year]
**URL**: [url]
Status: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ URL✓

### #2 - [status]
...
```

---

## EXECUTION

```bash
# Read this file first
read /Users/nathanlinte/.openclaw/skills/research-grant-proposal/verification_steps/wanfang.md

# Execute steps 1-3
# Then create wanfang_results.md
```

---

## OUTPUT FILE
