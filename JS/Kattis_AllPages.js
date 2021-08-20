// config
var id = undefined;
var username = undefined;
var secret = undefined;

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
		ret[key]['Status'] = 'OE';
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

if(d.children.length === 100 && document.querySelector('#problem_list_next').className === 'enabled'){
    window.open(document.querySelector('#problem_list_next').href);
}
