from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>JARVIS AI</title>

<link rel="icon" href="https://cdn-icons-png.flaticon.com/512/8649/8649595.png">

<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"/>

<style>

:root{
--bg:#020617;
--blue:#00bfff;
--green:#00ff88;
--purple:#9333ea;
--pink:#ff2ea6;
--card:rgba(255,255,255,0.05);
--text:#ffffff;
--sub:#94a3b8;
--border:rgba(255,255,255,0.08);
}

*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{
background:var(--bg);
font-family:"Poppins",sans-serif;
color:white;
overflow:hidden;
}

/* BACKGROUND */

.bg{
position:fixed;
width:100%;
height:100%;
overflow:hidden;
z-index:-1;
}

.circle{
position:absolute;
border-radius:50%;
filter:blur(120px);
opacity:0.4;
animation:float 10s infinite ease-in-out;
}

.c1{
width:500px;
height:500px;
background:var(--blue);
top:-100px;
left:-100px;
}

.c2{
width:500px;
height:500px;
background:var(--green);
bottom:-120px;
right:-120px;
}

.c3{
width:400px;
height:400px;
background:var(--purple);
top:50%;
left:50%;
transform:translate(-50%,-50%);
}

@keyframes float{
0%,100%{
transform:translateY(0px);
}
50%{
transform:translateY(40px);
}
}

/* LOGIN */

.login-screen{
position:fixed;
width:100%;
height:100%;
display:flex;
justify-content:center;
align-items:center;
background:#020617;
z-index:9999;
}

.login-box{
width:430px;
padding:40px;
border-radius:30px;
background:rgba(255,255,255,0.05);
backdrop-filter:blur(20px);
border:1px solid rgba(255,255,255,0.1);
text-align:center;
}

.ai-logo{
width:130px;
height:130px;
margin:auto;
padding:12px;
border-radius:50%;
background:#071426;

box-shadow:
0 0 20px var(--blue),
0 0 60px var(--blue);

animation:pulse 2s infinite;
}

.ai-logo img{
width:100%;
height:100%;
object-fit:contain;
}

@keyframes pulse{
0%,100%{
transform:scale(1);
}
50%{
transform:scale(1.08);
}
}

.login-title{
font-size:45px;
margin:20px 0;
font-family:"Orbitron",sans-serif;

background:linear-gradient(90deg,var(--blue),var(--green));
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.login-box input{
width:100%;
padding:16px;
margin-bottom:15px;
border:none;
border-radius:15px;
background:rgba(255,255,255,0.08);
color:white;
outline:none;
font-size:16px;
}

.login-box button{
width:100%;
padding:16px;
border:none;
border-radius:15px;
font-size:16px;
font-weight:700;
cursor:pointer;

background:linear-gradient(90deg,var(--blue),var(--green));
}

/* APP */

.app{
display:none;
width:100%;
height:100vh;
}

/* SIDEBAR */

.sidebar{
width:340px;
background:rgba(255,255,255,0.04);
backdrop-filter:blur(15px);
border-right:1px solid var(--border);
padding:20px;
overflow-y:auto;
}

.logo{
text-align:center;
margin-bottom:25px;
}

.logo-circle{
width:95px;
height:95px;
margin:auto;
padding:10px;
border-radius:50%;
background:#071426;

box-shadow:
0 0 20px var(--blue),
0 0 40px var(--blue);
}

.logo-circle img{
width:100%;
height:100%;
object-fit:contain;
}

.logo h1{
margin-top:15px;
font-size:34px;
font-family:"Orbitron",sans-serif;

background:linear-gradient(90deg,var(--blue),var(--green));
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.profile{
padding:20px;
border-radius:20px;
background:rgba(255,255,255,0.05);
text-align:center;
margin-bottom:20px;
}

.profile img{
width:90px;
height:90px;
border-radius:50%;
border:3px solid var(--blue);
}

.profile h2{
margin-top:10px;
}

.profile p{
font-size:14px;
color:var(--sub);
}

.section{
margin:20px 0 10px;
font-size:12px;
letter-spacing:2px;
color:var(--blue);
}

.sidebar button{
width:100%;
padding:15px;
margin-bottom:10px;
border:none;
border-radius:15px;
background:rgba(255,255,255,0.05);
color:white;
cursor:pointer;
text-align:left;
font-size:15px;
transition:0.3s;
}

.sidebar button:hover{
transform:translateX(5px);

background:linear-gradient(90deg,var(--blue),var(--green));
color:black;
}

.sidebar i{
margin-right:10px;
}

/* MAIN */

.main{
flex:1;
display:flex;
flex-direction:column;
}

.topbar{
height:80px;
display:flex;
justify-content:space-between;
align-items:center;
padding:0 30px;
background:rgba(255,255,255,0.04);
border-bottom:1px solid var(--border);
}

.top-left{
display:flex;
align-items:center;
gap:15px;
}

.top-logo{
width:60px;
height:60px;
padding:6px;
border-radius:50%;
background:#071426;

box-shadow:
0 0 15px var(--blue),
0 0 30px var(--blue);
}

.top-logo img{
width:100%;
height:100%;
object-fit:contain;
}

.title{
font-size:24px;
font-family:"Orbitron",sans-serif;
color:var(--blue);
}

.status{
color:var(--green);
font-weight:700;
}

/* CHAT */

.chat{
flex:1;
overflow-y:auto;
padding:30px;
}

.welcome{
text-align:center;
}

.welcome h1{
font-size:80px;
font-family:"Orbitron",sans-serif;

background:linear-gradient(90deg,var(--blue),var(--green));
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.welcome p{
font-size:18px;
color:var(--sub);
}

.messages{
max-width:1000px;
margin:auto;
margin-top:30px;
}

.message{
padding:18px;
border-radius:18px;
margin-bottom:15px;
animation:fade 0.4s ease;
}

.user{
background:rgba(0,191,255,0.15);
border-left:4px solid var(--blue);
margin-left:20%;
}

.ai{
background:rgba(0,255,136,0.12);
border-left:4px solid var(--green);
margin-right:20%;
}

@keyframes fade{
from{
opacity:0;
transform:translateY(20px);
}
to{
opacity:1;
transform:translateY(0px);
}
}

/* INPUT */

.input-area{
padding:20px;
background:rgba(255,255,255,0.04);
border-top:1px solid var(--border);
}

.input-box{
display:flex;
gap:10px;
}

.input-box input{
flex:1;
padding:16px;
border:none;
border-radius:16px;
background:rgba(255,255,255,0.08);
color:white;
font-size:16px;
outline:none;
}

.input-box button{
padding:16px 24px;
border:none;
border-radius:16px;
cursor:pointer;
font-size:16px;
font-weight:700;

background:linear-gradient(90deg,var(--blue),var(--green));
}

/* SCROLLBAR */

::-webkit-scrollbar{
width:6px;
}

::-webkit-scrollbar-thumb{
background:var(--blue);
border-radius:10px;
}

</style>

</head>

<body>

<div class="bg">
<div class="circle c1"></div>
<div class="circle c2"></div>
<div class="circle c3"></div>
</div>

<!-- LOGIN -->

<div class="login-screen" id="loginScreen">

<div class="login-box">

<div class="ai-logo">
<img src="https://cdn-icons-png.flaticon.com/512/8649/8649595.png">
</div>

<div class="login-title">
JARVIS AI
</div>

<input type="text" id="username" placeholder="Username">

<input type="password" id="password" placeholder="Password">

<button onclick="login()">
LOGIN
</button>

</div>

</div>

<!-- APP -->

<div class="app" id="app">

<!-- SIDEBAR -->

<div class="sidebar">

<div class="logo">

<div class="logo-circle">
<img src="https://cdn-icons-png.flaticon.com/512/8649/8649595.png">
</div>

<h1>JARVIS AI</h1>

</div>

<div class="profile">

<img src="https://cdn-icons-png.flaticon.com/512/9131/9131529.png">

<h2 id="profileName">
User
</h2>

<p>
Advanced AI User
</p>

</div>

<div class="section">
MOVIES
</div>

<button onclick="openWebsite('https://www.hotstar.com')"><i class="fas fa-tv"></i> Hotstar</button>

<button onclick="openWebsite('https://www.netflix.com')"><i class="fas fa-film"></i> Netflix</button>

<button onclick="openWebsite('https://www.primevideo.com')"><i class="fas fa-video"></i> Prime Video</button>

<button onclick="openWebsite('https://www.youtube.com')"><i class="fab fa-youtube"></i> YouTube</button>

<div class="section">
GAMES
</div>

<button onclick="openWebsite('https://www.roblox.com')"><i class="fas fa-gamepad"></i> Roblox</button>

<button onclick="openWebsite('https://store.steampowered.com')"><i class="fab fa-steam"></i> Steam</button>

<button onclick="openWebsite('https://www.minecraft.net')"><i class="fas fa-cube"></i> Minecraft</button>

<div class="section">
AI TOOLS
</div>

<button onclick="openWebsite('https://chat.openai.com')"><i class="fas fa-brain"></i> ChatGPT</button>

<button onclick="openWebsite('https://gemini.google.com')"><i class="fas fa-gem"></i> Gemini</button>

<div class="section">
TOOLS
</div>

<button onclick="openWebsite('https://mail.google.com')"><i class="fas fa-envelope"></i> Gmail</button>

<button onclick="openWebsite('https://www.wikipedia.org')"><i class="fas fa-book"></i> Wikipedia</button>

<button onclick="logout()">
<i class="fas fa-sign-out-alt"></i> Logout
</button>

</div>

<!-- MAIN -->

<div class="main">

<div class="topbar">

<div class="top-left">

<div class="top-logo">
<img src="https://cdn-icons-png.flaticon.com/512/8649/8649595.png">
</div>

<div class="title">
JARVIS AI
</div>

</div>

<div class="status" id="clock">
ONLINE
</div>

</div>

<div class="chat">

<div class="welcome">

<h1>JARVIS</h1>

<p>
Ask anything like:
Who is Albert Einstein?
or
Open YouTube
</p>

</div>

<div class="messages" id="messages"></div>

</div>

<div class="input-area">

<div class="input-box">

<input type="text" id="userInput" placeholder="Ask JARVIS AI anything...">

<button onclick="sendMessage()">
<i class="fas fa-paper-plane"></i> Send
</button>

</div>

</div>

</div>

</div>

<script>

const input = document.getElementById("userInput");
const messages = document.getElementById("messages");

/* LOGIN */

function login(){

const username = document.getElementById("username").value;
const password = document.getElementById("password").value;

if(username && password){

localStorage.setItem("jarvisUser", username);

document.getElementById("loginScreen").style.display = "none";
document.getElementById("app").style.display = "flex";

document.getElementById("profileName").innerHTML = username;

addMessage("ai","Welcome " + username + ". JARVIS AI online.");

}else{

alert("Enter username and password.");

}

}

/* AUTO LOGIN */

window.onload = function(){

updateClock();

const savedUser = localStorage.getItem("jarvisUser");

if(savedUser){

document.getElementById("loginScreen").style.display = "none";
document.getElementById("app").style.display = "flex";

document.getElementById("profileName").innerHTML = savedUser;

addMessage("ai","Hello " + savedUser + ". Systems ready.");

}

};

/* LOGOUT */

function logout(){

localStorage.removeItem("jarvisUser");
location.reload();

}

/* CLOCK */

function updateClock(){

const now = new Date();

document.getElementById("clock").innerHTML =
"● " + now.toLocaleTimeString([],{
hour:'2-digit',
minute:'2-digit',
hour12:true
});

}

setInterval(updateClock,1000);

/* MESSAGE */

function addMessage(type,text){

const div = document.createElement("div");

div.className = "message " + type;

div.innerHTML = `
<strong>${type === "user" ? "👤 YOU" : "⚡ JARVIS AI"}</strong>
<br><br>
${text}
`;

messages.appendChild(div);

messages.scrollTop = messages.scrollHeight;

}

/* SPEAK */

function speak(text){

if(!window.speechSynthesis) return;

speechSynthesis.cancel();

const speech = new SpeechSynthesisUtterance(text);

speech.rate = 1;
speech.pitch = 1.1;

speechSynthesis.speak(speech);

}

/* OPEN WEBSITE */

function openWebsite(url){

window.open(url,"_blank");

}

/* SEND MESSAGE */

async function sendMessage(){

const text = input.value.trim();

if(!text) return;

addMessage("user", text);

input.value = "";

const lower = text.toLowerCase();

/* WEBSITE DATABASE */

const websites = {

"youtube":"https://youtube.com",
"hotstar":"https://www.hotstar.com",
"netflix":"https://www.netflix.com",
"prime video":"https://www.primevideo.com",
"roblox":"https://www.roblox.com",
"steam":"https://store.steampowered.com",
"minecraft":"https://www.minecraft.net",
"google":"https://google.com",
"instagram":"https://instagram.com",
"github":"https://github.com",
"chatgpt":"https://chat.openai.com",
"gmail":"https://mail.google.com",
"wikipedia":"https://wikipedia.org"

};

/* OPEN WEBSITE */

if(lower.startsWith("open ")){

let siteName = lower.replace("open ","").trim();

if(websites[siteName]){

addMessage("ai","Opening " + siteName + "...");

speak("Opening " + siteName);

window.open(websites[siteName], "_blank");

return;

}else{

addMessage("ai","Website not found.");

return;

}

}

/* BASIC RESPONSES */

if(lower.includes("hello") || lower.includes("hi")){

addMessage("ai","Hello. JARVIS AI online.");

speak("Hello. JARVIS AI online.");

return;

}

if(lower.includes("time")){

let response = "Current time is " + new Date().toLocaleTimeString();

addMessage("ai",response);

speak(response);

return;

}

if(lower.includes("date")){

let response = "Today's date is " + new Date().toDateString();

addMessage("ai",response);

speak(response);

return;

}

/* WIKIPEDIA SEARCH */

try{

let searchText = text
.replace("who is","")
.replace("what is","")
.replace("tell me about","")
.trim();

if(searchText.length > 0){

addMessage("ai","Searching Wikipedia...");

const response = await fetch(
"https://en.wikipedia.org/api/rest_v1/page/summary/" +
encodeURIComponent(searchText)
);

const data = await response.json();

if(data.extract){

messages.lastChild.remove();

addMessage("ai", data.extract);

speak(data.extract);

return;

}

}

}catch(error){

console.log(error);

}

/* DEFAULT */

addMessage("ai","I am processing your request.");

}

input.addEventListener("keypress",function(e){

if(e.key === "Enter"){
sendMessage();
}

});

</script>

</body>

</html>

"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)