# SCIST Scoreboard 規劃

預計支援 OJ
- [UVa](#UVa)
- [ZOJ](#ZOJ)
- [TOJ](#TOJ)
- [TIOJ](#TIOJ)
- [Kattis](#Kattis)
- [AtCoder](#AtCoder)
- [CodeForces](#CodeForces)

## OJ 相關

### UVa
UVa 可以透過 Uhunt API 獲取解題狀況。

> https://uhunt.onlinejudge.org/api

UVa 解題的 Status 分成幾種:

| Status Code | Mean                | Correspond |
| ----------- | ------------------- | ---------- |
| 10          | Submission error    | OS         |
| 15          | Can't be judged     | OS         |
| 20          | In queue            | OS         |
| 30          | Compile error       | CE         |
| 35          | Restricted function | OS         |
| 40          | Runtime error       | RE         |
| 45          | Output limit        | OS         |
| 50          | Time limit          | TLE        |
| 60          | Memory limit        | MLE        |
| 70          | Wrong answer        | WA         |
| 80          | PresentationE       | OS         |
| 90          | Accepted            | AC         |

### ZOJ
ZOJ 並沒有正式的 API 可以查詢，僅有已知一組可以查詢使用者通過題目列表的連結。

> https://zerojudge.tw/User/V1.0/Accepted?account={Username}

ZOJ 解題的 Status 分成幾種:

| Status Code | Mean                   | Correspond |
| ----------- | ---------------------- | ---------- |
| AC          | Accepted               | AC         |
| WA          | Wrong Answer           | WA         |
| NA          | Wrong Answer(Multiple) | WA         |
| TLE         | Time Limit Exceeded    | TLE        |
| MLE         | Memory Limit Exceeded  | MLE        |
| OLE         | Output Limit Exceeded  | OS         |
| RE          | Runtime Error          | RE         |
| CE          | Compile Error          | CE         |

### TOJ
TOJ 具有查詢特定使用者以及特定題目解題狀況的功能，但基本上就是少了 CSS 的網站，稱不上是 API。
如果透過爬取個人頁面的解題狀況也許更實際。

> http://210.70.137.215/oj/be/chal?proid={PID}&acctid={UID}

TOJ 解題的 Status 分成幾種:

| Status Code | Mean                  | Correspond |
| ----------- | --------------------- | ---------- |
| AC          | Accepted              | AC         |
| WA          | Wrong Answer          | WA         |
| RE          | Runtime Error         | RE         |
| TLE         | Time Limit Exceeded   | TLE        |
| MLE         | Memory Limit Exceeded | MLE        |
| CE          | Compile Error         | CE         |
| IE          | Internal Error        | OS         |

### TIOJ
TIOJ 有 API 可以使用。在 submissions 頁面搜尋後，在網址的 submissions 後面加上 `.json` 就可以獲得 json 的回傳格式。

> https://tioj.ck.tp.edu.tw/submissions.json?filter_username={UserID}&filter_problem={ProblemID}

Github 連結: https://github.com/adrien1018/tioj/blob/master/app/views/submissions/show.json.jbuilder

TIOJ 解題的 Status 分成幾種:

| Status Code | Mean                  | Correspond |
| ----------- | --------------------- | ---------- |
| AC          | Accepted              | AC         |
| WA          | Wrong Answer          | WA         |
| RE          | Runtime Error         | RE         |
| TLE         | Time Limit Exceeded   | TLE        |
| MLE         | Memory Limit Exceeded | MLE        |
| CE          | Compile Error         | CE         |

### Kattis
Kattis 並沒有 API 可以直接提供查詢解題狀況，因此需要使用者自行到 Profile 當中查看 Submission，再搭配我們的 JavaScript 去取得資料並回傳。

Kattis 解題的 Status 分成幾種:

| Status Code           | Mean                  | Correspond |
| --------------------- | --------------------- | ---------- |
| Accepted              | Accepted              | AC         |
| Compile Error         | Compile Error         | CE         |
| Run Time Error        | Run Time Error        | RE         |
| Time Limit Exceeded   | Time Limit Exceeded   | TLE        |
| Wrong Answer          | Wrong Answer          | WA         |
| Output Limit Exceeded | Output Limit Exceeded | OS         |
| Memory Limit Exceeded | Memory Limit Exceeded | MLE        |
| Judge Error           | Judge Error           | OS         |

### AtCoder
AtCoder 有第三方的 API 可以使用。

> https://kenkoooo.com/atcoder/atcoder-api/results?user={Username}
> https://github.com/kenkoooo/AtCoderProblems/blob/master/doc/api.md

AtCoder 解題的 Status 分成幾種:

| Status Code | Mean                   | Correspond |
| ----------- | ---------------------- | ---------- |
| AC          | Accpted                | AC         |
| WA          | Wrong Answer           | WA         |
| TLE         | Time Limit Exceeded    | TLE        |
| MLE         | Memory Limit Exceeded  | MLE        |
| RE          | Runtime Error          | RE         |
| CE          | Compile Error          | CE         |
| QLE         | 不清楚                 | OS         |
| OLE         | Output Limit Exceeded  | OS         |
| IE          | Internal Error         | OS         |
| WJ          | Waiting for Judging    | OS         |
| WR          | Waiting for Re-judging | OS         |
| Judging     | Judging                | OS         |

### CodeForces
Codeforces 有官方的 API 可以使用，但是需要先申請一組 Key 與 Secret。

> https://codeforces.com/api/user.status?handle={Handle}
> https://codeforces.com/apiHelp

| Status Code                   | Mean             | Correspond |
| ------------------------- | ------------------- | ------- |
| OK                        | Accepted            | AC |
| PARTIAL                   | 不清楚              | OS |
| COMPILATION_ERROR         | Compile Error       | CE |
| RUNTIME_ERROR             | Runtime Error       | RE |
| WRONG_ANSWER              | Wrong Answer        | WA |
| PRESENTATION_ERROR        | PresentationE       | OS |
| TIME_LIMIT_EXCEEDED       | Time Limit Exceed   | TLE |
| MEMORY_LIMIT_EXCEEDED     | Memory Limit Exceed | MLE |
| IDLENESS_LIMIT_EXCEEDED   | 不清楚              | OS |
| SECURITY_VIOLATED         | 不清楚              | OS |
| CRASHED                   | 不清楚              | OS |
| INPUT_PREPARATION_CRASHED | 不清楚              | OS |
| CHALLENGED                | 不清楚              | OS |
| SKIPPED                   | 不清楚              | OS |
| TESTING                   | 不清楚              | OS |
| REJECTED                  | 不清楚              | OS |

## 規劃

現在預計將所有的 OJ 都分開來做，因此當計分版要爬取資料時，需要透過一個整合的程式將請求分給不同的爬蟲去做。
可以透過爬蟲來做的 OJ 都會使用 Scrapy 來製作，其餘則是由學員半手動更新到 Google Spreadsheet 上，請求的時候再去爬這張表。

### 使用者 OJ 資訊
不同的 OJ 查詢所使用的資料不太相同，因此這裡制定好每個 OJ 需要給哪些資料。

> 這裡只會列舉出一般 OJ 的部分，關於特殊 OJ 請參閱 [特殊 OJ 處理](#%E7%89%B9%E6%AE%8A-OJ-%E8%99%95%E7%90%86)

| OJ         | 須提供資料 |
| ---------- | ---------- |
| Uva        | UserID     |
| TOJ        | UserID     |
| TIOJ       | Username   |
| AtCoder    | Username   |
| Codeforces | Handle     |


### 查詢格式
這裡假設要更新的時候，會是以一個記分板為單位來抓，每個記分板的使用者資料、記分板題目分開兩個檔案寫。當要請求更新時

***users.json***

```json=
{
    "users": {
        "username1": {
            "judge": {
                "TOJ": "TOJ_ID",
                "TIOJ": "TIOJ_ID",
                ...
            }
        },
        ...
    }
}
```

***problems.json***

```json=
{
    "Scoreboard1": {
        "problems": [
            {
                "judge_name": "TOJ",
                "problem_id": "pid"
            },
            {
                "judge_name": "TOJ",
                "problem_id": "pid"
            },
            ...
        ],
        "users": [
            "name1",
            "name2",
            ...
        ]
    },
    ...
}
```


### 回傳格式

爬蟲回傳格式:

```json=
{
    "scoreboard": [
        "username1": {
            "pid1": "status",
            "pid2": "status",
            ...
        },
        "username2": {
            "pid1": "status",
            "pid2": "status",
            ...
        },
        ...
    ],
    ...
}
```

每個 OJ 使用的 Status 都不太相同，這裡將所有的 Status 都歸類在以下的 StatusCode 當中。

| StatusCode |        Mean         |
|:----------:|:-------------------:|
|     AC     |      Accepted       |
|     WA     |    Wrong answer     |
|     CE     |    Compile error    |
|     RE     |    Runtime error    |
|    TLE     |  Time limit exceed  |
|    MLE     | Memory limit exceed |
|     NE     |     Not Exists      |
|     OS     |     Other Status     |

如果該題的 Submission 不存在，歸類在 `NE`。
如果出現上述以外的情況，全部歸類在 `OS`。

### 特殊 OJ 處理
部分 OJ 如 Kattis, ZOJ 是需要登入才能查詢特定使用者的解題狀態，因此考慮使用其他方式。
這裡設定一張權限比較低的表可以讓學員半手動的更新這些沒辦法爬或不好爬的 OJ，然後記分板再去爬這張表。
而學員更新這張表的方法是**使用我們提供的 JavaScript** ，**透過瀏覽器的 extension** ，當瀏覽特定網址時執行，**自動爬然後自動更新到表上**。

後段會提到各個 OJ 所使用的 JS，至於 extension 如下:

> Chrome https://chrome.google.com/webstore/detail/run-javascript/lmilalhkkdhfieeienjbiicclobibjao/related

> FireFox https://addons.mozilla.org/en-US/firefox/addon/javascript/


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

## JS Code

### Kattis

```javascript=
// config
var id = 1;
var username = "Koios1143";
var secret = "testkey";

// Get Data
var d = document.querySelector("#wrapper > div > div:nth-child(2) > section > table > tbody");
var res = {}
for(var i=1 ; i <= d.children.length ; i++){
    var Timestamp = document.querySelector(`#wrapper > div > div:nth-child(2) > section > table > tbody > tr:nth-child(${i}) > td:nth-child(1)`).innerText;
	var Problem = document.querySelector(`#wrapper > div > div:nth-child(2) > section > table > tbody > tr:nth-child(${i}) > td:nth-child(3)`).innerText;
	var Status = document.querySelector(`#wrapper > div > div:nth-child(2) > section > table > tbody > tr:nth-child(${i}) > td:nth-child(4)`).innerText;
    
    // Some Weired Situation
    // "Fluortanten"
    // Accepted (100) => AC
    // Accepted (32) => WA
    if(Status.split(' ')[0] === 'Accepted'){
        if(Status.split(' ')[1] === '(100)'){
            Status = 'Accepted';
        }
        else if(Status.split(' ')[1] !== undefined){
            Status = 'Wrong Answer';
        }
    }
    
	if(res[Problem] === undefined){
        res[Problem] = {};
		res[Problem]['Status'] = Status;
        res[Problem]['Timestamp'] = Timestamp;
	}
	else if(Status === 'Accepted'){
		res[Problem]['Status'] = Status;
        res[Problem]['Timestamp'] = Timestamp;
	}
}
var ret = JSON.parse(`{\"ID\" : ${id}, \"Username\" : \"${username}\",\"Key\" : \"${secret}\"}`);
for(const [key, value] of Object.entries(res)){
    var Status = value['Status'];
    var Timestamp = value['Timestamp'];
    ret[key] = {};
    ret[key]['Timestamp'] = Timestamp;
    if(Status === 'Accepted'){
		ret[key]['Status'] = 'AC';
	}
	else if(Status === 'Wrong Answer'){
		ret[key]['Status'] = 'WA';
	}
	else if(Status === 'Compile Error'){
		ret[key]['Status'] = 'CE';
	}
	else if(Status === 'Run Time Error'){
		ret[key]['Status'] = 'RE';
	}
	else if(Status === 'Time Limit Exceeded'){
		ret[key]['Status'] = 'TLE';
	}
	else if(Status === 'Memory Limit Exceeded'){
		ret[key]['Status'] = 'MLE';
	}
	else{
		ret[key]['Status'] = 'OS';
	}
}
ret = JSON.stringify(ret);

// Parse to Google AppScript
Url= ["https://script.google.com/a/scist.org/macros/s/AKfycbykq72FNQcmv61Ayjpr26LysAgVWMI-A7PwAMfUJg/exec","https://script.google.com/macros/s/AKfycbxuBsnD5l6pNyuM39UsP4O7FdmUjSQy_nQtyOpKECsPHXg2sBVt/exec"];
judgeTime(ret);
function judgeTime(ret){
    var date = new Date();
    var Time = date.getTime();
    Time /= (1000*60);
    Time %= 10;

    if(Time<5){
        Ajax(0, ret);
    }
    else{
        Ajax(1, ret);
    }
}

function Ajax(urlIndex, ret){
    if(urlIndex <= 3){
        $.ajax({
            type:'post',
            cache: false,
            timeout: 8000,
            url: Url[urlIndex%2],
            data: ret,
            datatype:'json',
            success: function(respond){
                console.log(respond);
            },
            error: function(){
                Ajax(++urlIndex);
            }
        });
    }
}
```

如果要一次更新全部頁面可以在最後面加上:

```javascript=
if(d.children.length === 100 && document.querySelector('#problem_list_next').className === 'enabled'){
    window.open(document.querySelector('#problem_list_next').href);
}
```

> https://script.google.com/macros/s/AKfycbxuBsnD5l6pNyuM39UsP4O7FdmUjSQy_nQtyOpKECsPHXg2sBVt/exec

> https://script.google.com/a/scist.org/macros/s/AKfycbykq72FNQcmv61Ayjpr26LysAgVWMI-A7PwAMfUJg/exec

### ZeroJudge

```javascript=
// config
var id = 1;
var username = "Koios1143";
var secret = "testkey";

// Get Data
var d = document.querySelector("body > div.container > div > table > tbody");
var res = {}
for(var i=2 ; i <= d.children.length ; i++){
    var Timestamp = document.querySelector(`body > div.container > div > table > tbody > tr:nth-child(${i}) > td:nth-child(1)`).innerText;
	var Problem = document.querySelector(`body > div.container > div > table > tbody > tr:nth-child(${i}) > td:nth-child(3)`).innerText.split('.')[0];
	var Status = document.querySelector(`body > div.container > div > table > tbody > tr:nth-child(${i}) > td:nth-child(4)`).innerText.split(' ')[0];
	if(res[Problem] === undefined){
        res[Problem] = {};
		res[Problem]['Status'] = Status;
        res[Problem]['Timestamp'] = Timestamp;
	}
	else if(Status === 'Accepted'){
		res[Problem]['Status'] = Status;
        res[Problem]['Timestamp'] = Timestamp;
	}
}
var ret = JSON.parse(`{\"ID\" : ${id}, \"Username\" : \"${username}\",\"Key\" : \"${secret}\"}`);
for(const [key, value] of Object.entries(res)){
    var Status = value['Status'];
    var Timestamp = value['Timestamp'];
    ret[key] = {};
    ret[key]['Timestamp'] = Timestamp;
    if(Status === 'AC'){
		ret[key]['Status'] = 'AC';
	}
	else if(Status === 'WA'){
		ret[key]['Status'] = 'WA';
	}
	else if(Status === 'CE'){
		ret[key]['Status'] = 'CE';
	}
	else if(Status === 'RE'){
		ret[key]['Status'] = 'RE';
	}
	else if(Status === 'TLE'){
		ret[key]['Status'] = 'TLE';
	}
	else if(Status === 'MLE'){
		ret[key]['Status'] = 'MLE';
	}
	else{
		ret[key]['Status'] = 'OS';
	}
}
ret = JSON.stringify(ret);

// Parse to Google AppScript
Url = ["https://script.google.com/a/scist.org/macros/s/AKfycbwkVqaS98AcAehZthWvG0x6rE7TCxAaNfxwIiNj/exec", "https://script.google.com/a/scist.org/macros/s/AKfycbxienr-XKjqWbogxzH1PGMYo5kJfTopn4N6sAiF6A/exec"];
judgeTime(ret);
function judgeTime(ret){
    var date = new Date();
    var Time = date.getTime();
    Time /= (1000*60);
    Time %= 10;

    if(Time<5){
        Ajax(0, ret);
    }
    else{
        Ajax(1, ret);
    }
}

function Ajax(urlIndex, ret){
    if(urlIndex <= 3){
        $.ajax({
            type:'post',
            cache: false,
            timeout: 8000,
            url: Url[urlIndex%2],
            data: ret,
            datatype:'json',
            success: function(respond){
                console.log(respond);
            },
            error: function(){
                Ajax(++urlIndex);
            }
        });
    }
}
```

如果要一次更新全部頁面可以在最後面加上:

```javascript=
if(d.children.length == 21){
    window.open(document.querySelector('#pagging > a:nth-child(3)').href);
}
```

因為插件在每次瀏覽都會執行一次 JS，所以只要這一頁 submission 是滿的，也就是可能存在下一頁的情況，在送出結果後再開到下一頁，就會變成一個循環。

> https://script.google.com/a/scist.org/macros/s/AKfycbwkVqaS98AcAehZthWvG0x6rE7TCxAaNfxwIiNj/exec

> https://script.google.com/a/scist.org/macros/s/AKfycbxienr-XKjqWbogxzH1PGMYo5kJfTopn4N6sAiF6A/exec

### Demo


![](https://i.imgur.com/UonDrX8.gif)


###### tags: `SCIST`