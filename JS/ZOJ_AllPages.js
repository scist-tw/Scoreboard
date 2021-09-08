// config
var id = undefined;
var username = undefined;
var secret = undefined;

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

if(d.children.length == 21){
    window.open(document.querySelector('#pagging > a:nth-child(3)').href);
}
