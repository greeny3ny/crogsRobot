console.log("botControl.js loaded");

var config = {
	apiKey: "AIzaSyA6pk5vRkVWlQRXKOjLJ_khMUMvGnTzlkQ",
	authDomain: "crogobot.firebaseapp.com",
	databaseURL: "https://crogobot.firebaseio.com",
	projectId: "crogobot",
	storageBucket: "",
	messagingSenderId: "345603303322"
};
firebase.initializeApp(config);

const DB_REF = new Firebase("https://crogobot.firebaseio.com");

var offline = false;

readFirebase();
//getVideo();
checkOnlineStatus();

function moveForwards(){
	document.getElementById("for").innerHTML = "Moving forward";
	DB_REF.update({cont: "up"});
	setTimeout(function test(){
		document.getElementById("for").innerHTML = "---------------------------";
		DB_REF.update({cont: "stop"});
	},2000);
}

function moveBackwards(){
	document.getElementById("bac").innerHTML = "Moving backwards";
	DB_REF.update({cont: "down"});
	setTimeout(function test(){
		document.getElementById("bac").innerHTML = "---------------------------";
		DB_REF.update({cont: "stop"});
	},2000);
}

function rightTurn(){
	document.getElementById("ritu").innerHTML = "Turning right";
	DB_REF.update({cont: "right"});
	setTimeout(function test(){
		document.getElementById("ritu").innerHTML = "---------------------------";
		DB_REF.update({cont: "stop"});
	},2000);
}

function leftTurn(){
	document.getElementById("letu").innerHTML = "Turning left";
	DB_REF.update({cont: "left"});
	setTimeout(function test(){
		document.getElementById("letu").innerHTML = "---------------------------";
		DB_REF.update({cont: "stop"});
	},2000);
}

function readFirebase(){
	console.log("reading firebase...");
	DB_REF.child("cont").on("value", function(snapshot){
		console.log(snapshot.val());
		var st = snapshot.val(); 
		document.getElementById("status").innerHTML = "Current status : " + st;
	});
}

function getVideo(){
	console.log("reading firebase...");
	DB_REF.child("vidSrc").on("value", function(snapshot){
		console.log(snapshot.val());
		var st = snapshot.val(); 
		document.getElementById("vid").src = "https://www.youtube.com/embed/" + st;
	});
}

function checkOnlineStatus(){
	console.log("reading firebase...");
	DB_REF.child("online").on("value", function(snapshot){
		console.log(snapshot.val());
		var st = snapshot.val(); 
		document.getElementById("onlineStatus").innerHTML = "IS LILY CURRENTLY ACTIVE? : " + st;
		if (st == "No"){
			offline = true;
			document.getElementById("status").innerHTML = "Current status : Offline";
			document.getElementById("vid").src = "https://www.youtube.com/embed/rPleicjySdI";
		}else{
			readFirebase();
			getVideo();
		}
		enableButtons(st);
	});
}

//Arbitrary 'i' chosen here
function enableButtons(i){
	console.log(i);
	if (i == 'No'){
		document.getElementById("forBut").disabled = true;
		document.getElementById("bacBut").disabled = true;
		document.getElementById("rigBut").disabled = true;
		document.getElementById("lefBut").disabled = true;
		document.getElementById("SLeBut").disabled = true;
		document.getElementById("SRiBut").disabled = true;
	} else {
		document.getElementById("forBut").disabled = false;
		document.getElementById("bacBut").disabled = false;
		document.getElementById("rigBut").disabled = false;
		document.getElementById("lefBut").disabled = false;
		document.getElementById("SLeBut").disabled = false;
		document.getElementById("SRiBut").disabled = false;
	}
}

function doFunction(){
	
	
	
	
}