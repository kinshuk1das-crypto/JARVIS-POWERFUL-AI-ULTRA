from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>JARVIS AI</title>

<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"/>

<style>

:root{
    --bg:#020617;
    --card:rgba(255,255,255,0.05);
    --text:#ffffff;
    --sub:#94a3b8;
    --blue:#00bfff;
    --green:#00ff88;
    --purple:#9333ea;
    --pink:#ff2ea6;
    --border:rgba(255,255,255,0.08);
}

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    background:var(--bg);
    color:var(--text);
    font-family:"Poppins",sans-serif;
    overflow:hidden;
}

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
    top:-120px;
    left:-120px;
}

.c2{
    width:450px;
    height:450px;
    background:var(--green);
    bottom:-120px;
    right:-120px;
}

.c3{
    width:350px;
    height:350px;
    background:var(--purple);
    left:50%;
    top:50%;
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

.app{
    display:flex;
    width:100%;
    height:100vh;
}

.sidebar{
    width:320px;
    background:rgba(255,255,255,0.04);
    backdrop-filter:blur(15px);
    border-right:1px solid var(--border);
    padding:20px;
    overflow-y:auto;
}

.logo{
    text-align:center;
    font-size:36px;
    font-family:"Orbitron",sans-serif;
    font-weight:900;
    margin-bottom:30px;

    background:linear-gradient(90deg,var(--blue),var(--green));
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.section{
    color:var(--blue);
    margin:20px 0 10px;
    font-size:12px;
    text-transform:uppercase;
    letter-spacing:2px;
}

.sidebar button{
    width:100%;
    padding:15px;
    margin-bottom:12px;
    border:none;
    border-radius:15px;
    background:var(--card);
    color:var(--text);
    cursor:pointer;
    text-align:left;
    transition:0.3s;
    font-size:15px;
}

.sidebar button:hover{
    transform:translateX(5px);
    background:linear-gradient(90deg,var(--blue),var(--green));
    color:black;
}

.sidebar i{
    margin-right:10px;
}

.main{
    flex:1;
    display:flex;
    flex-direction:column;
}

.topbar{
    height:75px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:0 30px;
    background:rgba(255,255,255,0.04);
    border-bottom:1px solid var(--border);
}

.title{
    font-size:24px;
    color:var(--blue);
    font-family:"Orbitron",sans-serif;
}

.status{
    color:var(--green);
    font-size:14px;
}

.chat{
    flex:1;
    overflow-y:auto;
    padding:30px;
}

.welcome{
    text-align:center;
    margin-bottom:30px;
}

.welcome h1{
    font-size:75px;
    font-family:"Orbitron",sans-serif;

    background:linear-gradient(90deg,var(--blue),var(--green));
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.welcome p{
    color:var(--sub);
}

.core-box{
    width:240px;
    height:240px;
    margin:20px auto;
    position:relative;
}

.ring{
    position:absolute;
    border-radius:50%;
    border:3px solid transparent;
}

.r1{
    width:240px;
    height:240px;
    border-top:3px solid var(--blue);
    border-bottom:3px solid var(--green);
    animation:spin 6s linear infinite;
}

.r2{
    width:190px;
    height:190px;
    top:25px;
    left:25px;
    border-left:3px solid var(--purple);
    border-right:3px solid var(--pink);
    animation:spinReverse 5s linear infinite;
}

.r3{
    width:140px;
    height:140px;
    top:50px;
    left:50px;
    border:2px dashed rgba(255,255,255,0.4);
    animation:spin 10s linear infinite;
}

.core{
    width:80px;
    height:80px;
    border-radius:50%;
    position:absolute;
    top:80px;
    left:80px;

    background:radial-gradient(circle,var(--blue),var(--green));

    box-shadow:0 0 50px var(--blue);

    animation:pulse 2s infinite;
}

@keyframes spin{
    100%{
        transform:rotate(360deg);
    }
}

@keyframes spinReverse{
    100%{
        transform:rotate(-360deg);
    }
}

@keyframes pulse{
    0%,100%{
        transform:scale(1);
    }
    50%{
        transform:scale(1.1);
    }
}

.messages{
    max-width:1000px;
    margin:auto;
}

.message{
    padding:16px;
    border-radius:18px;
    margin-bottom:15px;
}

.user{
    background:rgba(0,191,255,0.15);
    border-left:4px solid var(--blue);
    margin-left:20%;
}

.ai{
    background:rgba(0,255,136,0.10);
    border-left:4px solid var(--green);
    margin-right:20%;
}

.input-area{
    padding:20px;
    background:rgba(255,255,255,0.04);
    border-top:1px solid var(--border);
}

.input-box{
    display:flex;
    gap:12px;
}

.input-box input{
    flex:1;
    padding:16px;
    border:none;
    border-radius:16px;
    background:rgba(255,255,255,0.08);
    color:white;
    outline:none;
}

.input-box button{
    padding:16px 24px;
    border:none;
    border-radius:16px;
    cursor:pointer;
    font-weight:700;
    background:linear-gradient(90deg,var(--blue),var(--green));
}

.image-box{
    text-align:center;
    margin-top:20px;
}

.image-box img{
    width:100%;
    max-width:750px;
    border-radius:22px;
    border:2px solid var(--blue);
}

</style>

</head>

<body>

<div class="bg">

<div class="circle c1"></div>
<div class="circle c2"></div>
<div class="circle c3"></div>

</div>

<div class="app">

<div class="sidebar">

<div class="logo">
<i class="fas fa-robot"></i> JARVIS AI
</div>

<button onclick="newChat()">
<i class="fas fa-plus"></i>
New Chat
</button>

<button onclick="generateImage()">
<i class="fas fa-image"></i>
AI Image
</button>

<button onclick="startVoice()">
<i class="fas fa-microphone"></i>
Voice Assistant
</button>

<button onclick="clearChat()">
<i class="fas fa-trash"></i>
Clear Chat
</button>

<div class="section">Entertainment</div>

<button onclick="openWebsite('https://youtube.com')">
<i class="fab fa-youtube"></i>
YouTube
</button>

<button onclick="openWebsite('https://netflix.com')">
<i class="fas fa-film"></i>
Netflix
</button>

<button onclick="openWebsite('https://spotify.com')">
<i class="fab fa-spotify"></i>
Spotify
</button>

<div class="section">Coding</div>

<button onclick="openWebsite('https://github.com')">
<i class="fab fa-github"></i>
GitHub
</button>

<button onclick="openWebsite('https://replit.com')">
<i class="fas fa-code"></i>
Replit
</button>

</div>

<div class="main">

<div class="topbar">

<div class="title">
JARVIS AI
</div>

<div class="status" id="clock">
ONLINE
</div>

</div>

<div class="chat">

<div class="welcome">

<div class="core-box">

<div class="ring r1"></div>
<div class="ring r2"></div>
<div class="ring r3"></div>
<div class="core"></div>

</div>

<h1>JARVIS</h1>

<p>
Advanced Artificial Intelligence Assistant
</p>

</div>

<div class="messages" id="messages"></div>

<div class="image-box" id="imageBox"></div>

</div>

<div class="input-area">

<div class="input-box">

<input type="text" id="userInput" placeholder="Ask JARVIS anything...">

<button onclick="sendMessage()">
<i class="fas fa-paper-plane"></i>
Send
</button>

</div>

</div>

</div>

</div>

<script>

const input = document.getElementById("userInput");
const messages = document.getElementById("messages");
const imageBox = document.getElementById("imageBox");

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

/* ADD MESSAGE */

function addMessage(type,text){

const div = document.createElement("div");

div.className = `message ${type}`;

div.innerHTML = `
<strong>
${type === "user" ? "👤 YOU" : "⚡ JARVIS AI"}
</strong>
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

/* WIKIPEDIA SEARCH AI */

async function aiReply(text){

text = text.toLowerCase();

/* HI */

if(text.includes("hi")){
return "Hi. JARVIS AI is online and ready.";
}

/* TIME */

if(text.includes("time")){

const now = new Date();

return "Current time is " + now.toLocaleTimeString([],{
hour:'2-digit',
minute:'2-digit',
hour12:true
});

}

/* DATE */

if(text.includes("date")){
return "Today's date is " + new Date().toDateString();
}

/* JOKE */

if(text.includes("joke")){

const jokes = [

"Why do programmers hate nature? Too many bugs.",

"Why was the computer cold? It forgot to close Windows.",

"Why did the AI become calm? Deep learning."

];

return jokes[Math.floor(Math.random()*jokes.length)];

}

/* OPEN WEBSITE COMMANDS */

if(text.includes("open youtube")){
openWebsite("https://youtube.com");
return "Opening YouTube.";
}

if(text.includes("open netflix")){
openWebsite("https://netflix.com");
return "Opening Netflix.";
}

if(text.includes("open spotify")){
openWebsite("https://spotify.com");
return "Opening Spotify.";
}

if(text.includes("open github")){
openWebsite("https://github.com");
return "Opening GitHub.";
}

if(text.includes("open replit")){
openWebsite("https://replit.com");
return "Opening Replit.";
}

/* WIKIPEDIA SEARCH COMMAND */

try{

let searchText = text
.replace("who is","")
.replace("what is","")
.replace("tell me about","")
.replace("search","")
.trim();

const response = await fetch(
`https://en.wikipedia.org/api/rest_v1/page/summary/${searchText}`
);

const data = await response.json();

if(data.extract){
return data.extract;
}

}catch(error){

return "Wikipedia search failed.";

}

/* DEFAULT */

return "I am still learning new things.";

}

/* SEND MESSAGE */

async function sendMessage(){

const text = input.value.trim();

if(!text) return;

addMessage("user",text);

input.value = "";

const response = await aiReply(text);

addMessage("ai",response);

speak(response);

}

/* ENTER */

input.addEventListener("keypress",function(e){

if(e.key === "Enter"){
sendMessage();
}

});

/* IMAGE */

function generateImage(){

const randomNum = Math.floor(Math.random()*1000);

const url = `https://picsum.photos/900/500?random=${randomNum}`;

imageBox.innerHTML = `

<h2 style="margin-bottom:15px;color:var(--blue);">
AI GENERATED IMAGE
</h2>

<img src="${url}">

`;

}

/* VOICE */

function startVoice(){

const SpeechRecognition =
window.SpeechRecognition || window.webkitSpeechRecognition;

if(!SpeechRecognition){

alert("Voice recognition not supported.");

return;

}

const recognition = new SpeechRecognition();

recognition.lang = "en-US";

recognition.start();

recognition.onresult = function(event){

const transcript = event.results[0][0].transcript;

input.value = transcript;

sendMessage();

};

}

/* CHAT */

function newChat(){

messages.innerHTML = "";

imageBox.innerHTML = "";

addMessage("ai","New conversation initialized.");

}

function clearChat(){

newChat();

}

/* OPEN WEBSITE */

function openWebsite(url){

window.open(url,"_blank");

}

/* LOAD */

window.onload = function(){

updateClock();

};

</script>

</body>

</html>

"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)