# SCIST Scoreboard 規劃

預計支援 OJ
- UVa
- ZOJ
- TOJ
- TIOJ
- Kattis
- AtCoder
- CodeForces

## OJ 相關

### UVa

UVa 可以透過 Uhunt API 獲取解題狀況。

> https://uhunt.onlinejudge.org/api

UVa 解題的 Status 分成幾種:

| Verdict ID | Status              |
| ---------- | ------------------- |
| 10         | Submission error    |
| 15         | Can't be judged     |
| 20         | In queue            |
| 30         | Compile error       |
| 35         | Restricted function |
| 40         | Runtime error       |
| 45         | Output limit        |
| 50         | Time limit          |
| 60         | Memory limit        |
| 70         | Wrong answer        |
| 80         | PresentationE       |
| 90         | Accepted            |

### ZOJ

ZOJ 並沒有正式的 API 可以查詢，僅有已知一組可以查詢使用者通過題目列表的連結。

> https://zerojudge.tw/User/V1.0/Accepted?account={Username}

ZOJ 解題的 Status 分成幾種:

| Verdict | Status                |
| ------- | --------------------- |
| AC      | Accepted              |
| WA      | Wrong Answer          |
| NA      | Wrong Answer(Multiple)|
| TLE     | Time Limit Exceeded   |
| MLE     | Memory Limit Exceeded |
| OLE     | Output Limit Exceeded |
| RE      | Runtime Error         |
| CE      | Compile Error         |

### TOJ

TOJ 具有查詢特定使用者以及特定題目解題狀況的功能，但基本上就是少了 CSS 的網站，稱不上是 API。

如果透過爬取個人頁面的解題狀況也許更實際。

> http://210.70.137.215/oj/be/chal?proid={PID}&acctid={UID}

TOJ 解題的 Status 分成幾種:

| Verdict | Status                |
| ------- | --------------------- |
| AC      | Accepted              |
| WA      | Wrong Answer          |
| RE      | Runtime Error         |
| TLE     | Time Limit Exceeded   |
| MLE     | Memory Limit Exceeded |
| CE      | Compile Error         |
| IE      | Internal Error        |

### TIOJ

TIOJ 有 API 可以使用。在 submissions 頁面搜尋後，在網址的 submissions 後面加上 `.json` 就可以獲得 json 的回傳格式。

> https://tioj.ck.tp.edu.tw/submissions.json?filter_username={UserID}&filter_problem={ProblemID}

Github 連結: https://github.com/adrien1018/tioj/blob/master/app/views/submissions/show.json.jbuilder

TIOJ 解題的 Status 分成幾種:

| Status              |
| ------------------- |
| Accepted            |
| Wrong Answer        |
| Time Limit Exceeded |
| Segementation Fault |
| Runtime Error       |
| Compilation Error   |

### Kattis

Kattis 並沒有 API 可以直接提供查詢解題狀況，因此需要使用者自行到 Profile 當中查看 Submission，再搭配我們的 JavaScript 去取得資料並回傳。

Kattis 解題的 Status 分成幾種:

| Status                |
| --------------------- |
| Accepted              |
| Compile Error         |
| Run Time Error        |
| Time Limit Exceeded   |
| Wrong Answer          |
| Output Limit Exceeded |
| Memory Limit Exceeded |
| Judge Error           |

### AtCoder
AtCoder 有第三方的 API 可以使用。

> https://kenkoooo.com/atcoder/atcoder-api/results?user={Username}

> https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md

AtCoder 解題的 Status 分成幾種:

| Verdict | Status                 |
| ------- | ---------------------- |
| AC      | Accpted                |
| WA      | Wrong Answer           |
| TLE     | Time Limit Exceeded    |
| MLE     | Memory Limit Exceeded  |
| RE      | Runtime Error          |
| CE      | Compile Error          |
| QLE     | 不清楚                 |
| OLE     | Output Limit Exceeded  |
| IE      | Internal Error         |
| WJ      | Waiting for Judging    |
| WR      | Waiting for Re-judging |
| Judging | Judging                |

### Codeforces

Codeforces 有官方的 API 可以使用，但是需要先申請一組 Key 與 Secret。

> https://codeforces.com/api/user.status?handle={Handle}

> https://codeforces.com/apiHelp

| Verdict                   | Status              |
| ------------------------- | ------------------- |
| OK                        | Accepted            |
| PARTIAL                   | 不清楚              |
| COMPILATION_ERROR         | Compile Error       |
| RUNTIME_ERROR             | Runtime Error       |
| WRONG_ANSWER              | Wrong Answer        |
| PRESENTATION_ERROR        | PresentationE       |
| TIME_LIMIT_EXCEEDED       | Time Limit Exceed   |
| MEMORY_LIMIT_EXCEEDED     | Memory Limit Exceed |
| IDLENESS_LIMIT_EXCEEDED   | 不清楚              |
| SECURITY_VIOLATED         | 不清楚              |
| CRASHED                   | 不清楚              |
| INPUT_PREPARATION_CRASHED | 不清楚              |
| CHALLENGED                | 不清楚              |
| SKIPPED                   | 不清楚              |
| TESTING                   | 不清楚              |
| REJECTED                  | 不清楚              |

## 規劃

### 特殊 OJ 處理

部分 OJ 如 Kattis, ZOJ 是需要登入才能查詢特定使用者的解題狀態，因此考慮使用其他方式。
這裡設定一張權限比較低的表可以讓學員半手動的更新這些沒辦法爬或不好爬的 OJ，然後記分板再去爬這張表。

而學員更新這張表的方法是**使用我們提供的 JavaScript** ，**透過瀏覽器的 extension** ，當瀏覽特定網址時執行，**自動爬然後自動更新到表上**。

Extension 如下:

> Chrome https://chrome.google.com/webstore/detail/run-javascript/lmilalhkkdhfieeienjbiicclobibjao/related

> FireFox https://addons.mozilla.org/en-US/firefox/addon/javascript/

JavaScript 的部分可以在 `JS` 資料夾中看到。

### 查詢格式

這裡假設要更新的時候，會是以一個記分板為單位來抓，所以會一次包含多個使用者以及多個題目，期待的查詢格式如下:

```json=
[
    Username: [
        "username1",
        "username2",
        ...
    ],
    ProblemID: {
        "UVa": [
            "PID1",
            "PID2",
            ...
        ],
        "ZOJ": [
            "PID1",
            "PID2",
            ...
        ],
        "TOJ": [
            "PID1",
            "PID2",
            ...
        ],
        ...
    }
]
```

### 回傳格式

爬蟲回傳格式:

```json=
[
    "username1": {
        "UVa": {
            "PID" : "StatusCode",
            "PID" : "StatusCode",
            ...
        },
        "ZOJ": {
            "PID" : "StatusCode",
            "PID" : "StatusCode",
            ...
        },
        ...
    }
]
```

部分 OJ 沒有提供 API ，因此改用 JavaScript 去抓，再更新到 Google spreadsheet 上。

因此，這裡的回傳都是以**個人**、**特定 OJ** 的方式，因此 username 只會出現一次，也不會有不同 OJ 的項目。除了 username 以外，還需要傳入 key 作驗證。

```json=
{
    "ID" : 1,
    "Key" : "key",
    "Username" : "username",
    "PID1" : {
        "Status" : "AC";
        "Timestamp" : 7530014
    },
    "PID2" : {
        "Status" : "AC";
        "Timestamp" : 7530015
    },
    "PID3" : {
        "Status" : "AC";
        "Timestamp" : 7530016
    },
    ...
}
```

每個 OJ 使用的 Verdict 都不太相同，這裡將所有的 Verdict 都歸類在以下的 StatusCode 當中。

| StatusCode |        Mean         |
|:----------:|:-------------------:|
|     AC     |      Accepted       |
|     WA     |    Wrong answer     |
|     CE     |    Compile error    |
|     RE     |    Runtime error    |
|    TLE     |  Time limit exceed  |
|    MLE     | Memory limit exceed |
|     NE     |     Not Exists      |
|     OE     |     Other Error     |

如果該題的 Submission 不存在，歸類在 `NE`。

如果出現上述以外的情況，全部歸類在 `OE`。

## Demo JS with Extenstion

![](https://i.imgur.com/UonDrX8.gif)
