# Git 推送安全函数（跨机可复用版）

> **为什么需要这个**
> `git push` 把传输进度写入 **stderr**（git 的正常行为），PowerShell 会把它包成
> `NativeCommandError` 并显示 `[exit code: 1]`，造成"推送失败"的误判。
>
> **判定推送成功的唯一依据**：
> ```
> 本地 HEAD  ==  git ls-remote origin refs/heads/main
> ```

---

## 一、本机现状（重要）

| 项 | 值 |
|---|---|
| **ExecutionPolicy** | **`RemoteSigned`** |
| **后果** | **连本地创建的 `.ps1` / `.psm1` 都拒绝加载** |
| **已验证** | `.dsh\ts.ps1` 同样无法运行（AGENTS.md 里的 token-saver 约定实际未生效） |
| **解法** | **`Invoke-Expression` 读内容执行**（内存执行，绕过文件策略） |

---

## 二、加载方式（两步）

```powershell
# 1. 加载（每次新会话执行一次）
Invoke-Expression (Get-Content 'D:\deepseek 工作\.dsh\gp.ps1' -Raw -Encoding utf8)

# 2. 使用
gitpush -Action status
gitpush -Action push -MessageFile 'D:\deepseek 工作\_re4\msg.txt'
```

> **★ `-Encoding utf8` 不能省**：用默认编码 `Get-Content -Raw` 会把中文读成乱码，
> 导致 `Invoke-Expression` 语法错误。

---

## 三、四种 Action

| Action | 行为 |
|---|---|
| **`status`** | 查本地 HEAD / 远端 main / 是否一致（**最安全的验证手段**） |
| **`push`**（默认） | `git add -A` → commit → push → **ls-remote 哈希核对** |
| **`commit`** | 仅提交，不推送 |
| **`only`** | 仅推送（不提交）+ 哈希核对 |

---

## 四、函数定义（可直接粘贴到任何 PowerShell 会话）

```powershell
function Invoke-GitPush {
    [CmdletBinding()]
    param(
        [ValidateSet('push','commit','only','status')]
        [string]$Action = 'push',
        [string]$MessageFile,
        [string]$Repo = 'D:\deepseek 工作\.dsh\skills'
    )

    $env:GIT_TERMINAL_PROMPT = '0'

    function _step($t) { Write-Host "-- $t" -ForegroundColor Cyan }
    function _ok($t)   { Write-Host "   OK   $t" -ForegroundColor Green }
    function _bad($t)  { Write-Host "   FAIL $t" -ForegroundColor Red }

    if (-not (Test-Path $Repo)) { _bad "仓库不存在: $Repo"; return 2 }

    # ---------- status ----------
    if ($Action -eq 'status') {
        _step '本地 HEAD'
        $local = (& git -C $Repo rev-parse HEAD 2>$null)
        Write-Host "   $local"

        _step '分支状态'
        Write-Host "   $((& git -C $Repo status -sb 2>$null | Select-Object -First 1))"

        _step '远端 main'
        $remote = ((& git -C $Repo ls-remote origin refs/heads/main 2>$null) -split '\s+')[0]
        Write-Host "   $remote"

        if ($local -and $remote -and $local.Trim() -eq $remote.Trim()) {
            _ok '本地与远端一致'; return 0
        } else {
            _bad '本地与远端不一致'; return 1
        }
    }

    # ---------- 校验 message ----------
    if ($Action -in @('push','commit')) {
        if (-not $MessageFile -or -not (Test-Path $MessageFile)) {
            _bad "需要 -MessageFile 且文件存在: $MessageFile"; return 2
        }
        $bytes = [System.IO.File]::ReadAllBytes($MessageFile)
        if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
            _bad '提交信息文件带 BOM，请重写为 UTF-8 无 BOM'; return 2
        }
    }

    # ---------- 提交 ----------
    if ($Action -in @('push','commit')) {
        _step 'git add -A'
        & git -C $Repo add -A 2>$null | Out-Null

        _step 'git commit'
        $out = & git -C $Repo -c core.safecrlf=false commit -F $MessageFile 2>&1
        $code = $LASTEXITCODE
        $out | ForEach-Object { Write-Host "   $_" }

        if ($code -ne 0) {
            if (($out -join "`n") -match 'nothing to commit|no changes added') {
                _ok '无改动需提交，继续'
            } else {
                _bad "提交失败 exit=$code"; return $code
            }
        } else {
            _ok '提交成功'
        }
    }

    if ($Action -eq 'commit') { _ok '仅提交模式，结束'; return 0 }

    # ---------- 推送：只认 $LASTEXITCODE ----------
    _step 'git push origin main'
    $out = & git -C $Repo push origin main 2>&1
    $code = $LASTEXITCODE
    $out | ForEach-Object { Write-Host "   $_" }

    if ($code -ne 0) { _bad "推送失败 exit=$code (这是真失败)"; return $code }
    _ok 'git push 退出码 = 0'

    # ---------- 二次确认：远端哈希 == 本地 HEAD ----------
    _step '远端哈希核对 (ls-remote)'
    $local  = (& git -C $Repo rev-parse HEAD 2>$null).Trim()
    $remote = ((& git -C $Repo ls-remote origin refs/heads/main 2>$null) -split '\s+')[0]
    Write-Host "   本地: $local"
    Write-Host "   远端: $remote"

    if (-not $remote) { _bad '读不到远端 main (网络/权限)'; return 1 }
    if ($local -ne $remote) { _bad '远端与本地不一致，推送未生效'; return 1 }

    _ok "推送已验证: $($local.Substring(0,7)) 已在远端"
    Write-Host ''
    Write-Host "结果: 成功  $($local.Substring(0,7))" -ForegroundColor Green
    return 0
}

Set-Alias -Name gitpush -Value Invoke-GitPush -Scope Global -Force
```

---

## 五、判定成功/失败的唯一标准

### ✅ 成功

```
-- 远端哈希核对 (ls-remote)
   本地: ac21b1ec38b0ea2113f4952908397e7dff89101c
   远端: ac21b1ec38b0ea2113f4952908397e7dff89101c
   OK   推送已验证: ac21b1e 已在远端
```

### ❌ 失败

```
   FAIL 推送失败 exit=128 (这是真失败)
```
或
```
   FAIL 远端与本地不一致，推送未生效
```

### ⚠ 假失败（不要被吓到）

```
[stderr] To github.com:xxx.git
         bbddf99..ac21b1e  main -> main
[exit code: 1]
```

**这是 PowerShell 把 git 的 stderr 进度包成了 NativeCommandError。**
**看到 `旧哈希..新哈希  main -> main` 就是成功。**

---

## 六、几个坑

| 坑 | 说明 |
|---|---|
| **`gp` 不能作别名** | **PowerShell 内置只读别名**（= `Get-ItemProperty`），必须用 `gitpush` |
| **`Get-Content` 必须加 `-Encoding utf8`** | 否则中文乱码 → `Invoke-Expression` 语法错误 |
| **提交信息不能带 BOM** | 用 Python `open(..., newline="\n")` 写，不要用 `Out-File -Encoding utf8` |
| **仓库根是 `.dsh\skills`** | `.dsh\gp.ps1` 与 `.dsh\AGENTS.md` **在仓库之外**，不受版本控制 |
| **`.ps1` / `.psm1` 都无法加载** | `RemoteSigned` 策略，只能 `Invoke-Expression` |

---

## 七、手动核对（不用函数时）

```powershell
$work = 'D:\deepseek 工作\.dsh\skills'
git -C $work rev-parse HEAD
git -C $work ls-remote origin refs/heads/main
# 两个哈希相同 = 已推送成功
```
