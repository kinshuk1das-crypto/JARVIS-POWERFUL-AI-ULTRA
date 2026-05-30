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
        :root {
            --bg: #0a0e27;
            --blue: #00d4ff;
            --green: #00ff88;
            --purple: #a855f7;
            --text: #f0f0f0;
            --sub: #94a3b8;
            --border: rgba(255, 255, 255, 0.1);
            --glass: rgba(255, 255, 255, 0.05);
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: var(--bg);
            font-family: "Poppins", sans-serif;
            color: var(--text);
            overflow: hidden;
            height: 100vh;
        }
        .bg {
            position: fixed;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: -1;
            background: radial-gradient(ellipse at 20% 50%, rgba(0,212,255,0.15) 0%, transparent 50%),
                        radial-gradient(ellipse at 80% 20%, rgba(0,255,136,0.1) 0%, transparent 50%),
                        radial-gradient(ellipse at 50% 80%, rgba(168,85,247,0.1) 0%, transparent 50%);
        }
        .login-screen {
            position: fixed;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            background: rgba(10,14,39,0.98);
            z-index: 9999;
        }
        .login-box {
            padding: 50px 40px;
            border-radius: 30px;
            background: var(--glass);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            text-align: center;
            width: 400px;
            animation: slideUp 0.6s ease;
        }
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(50px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .ai-logo {
            width: 120px;
            height: 120px;
            margin: 0 auto 30px;
            padding: 15px;
            border-radius: 50%;
            background: rgba(7,20,38,0.9);
            box-shadow: 0 0 30px var(--blue), 0 0 60px rgba(0,212,255,0.5);
            animation: pulseGlow 2s infinite;
        }
        @keyframes pulseGlow {
            0%,100% { box-shadow: 0 0 30px var(--blue), 0 0 60px rgba(0,212,255,0.5); }
            50% { box-shadow: 0 0 50px var(--green), 0 0 100px rgba(0,255,136,0.5); }
        }
        .login-title {
            font-size: 48px;
            margin: 20px 0;
            font-family: "Orbitron", sans-serif;
            background: linear-gradient(135deg, var(--blue), var(--green), var(--purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .input-group {
            position: relative;
            margin-bottom: 20px;
        }
        .input-group i {
            position: absolute;
            left: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--sub);
        }
        .login-box input {
            width: 100%;
            padding: 16px 16px 16px 45px;
            border: 2px solid transparent;
            border-radius: 15px;
            background: rgba(255,255,255,0.08);
            color: var(--text);
            outline: none;
            font-size: 16px;
            transition: all 0.3s;
        }
        .login-box input:focus {
            border-color: var(--blue);
            background: rgba(255,255,255,0.12);
        }
        .btn {
            width: 100%;
            padding: 16px;
            border: none;
            border-radius: 15px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 15px;
            background: linear-gradient(135deg, var(--blue), var(--green));
            color: #000;
            transition: all 0.3s;
            text-transform: uppercase;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(0,212,255,0.3);
        }
        .btn-outline {
            background: transparent;
            border: 2px solid var(--border);
            color: var(--text);
        }
        .error-message {
            color: #ef4444;
            font-size: 14px;
            margin-top: 10px;
            min-height: 20px;
        }
        .app {
            display: none;
            width: 100%;
            height: 100vh;
        }
        .container {
            display: flex;
            height: 100%;
        }
        .sidebar {
            width: 350px;
            background: rgba(19,24,66,0.8);
            backdrop-filter: blur(20px);
            border-right: 1px solid var(--border);
            padding: 25px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
        }
        .logo-circle {
            width: 80px;
            height: 80px;
            margin: 0 auto 15px;
            padding: 10px;
            border-radius: 50%;
            background: rgba(7,20,38,0.9);
            box-shadow: 0 0 25px rgba(0,212,255,0.4);
            animation: pulseGlow 2s infinite;
        }
        .app-title {
            font-family: "Orbitron", sans-serif;
            font-size: 28px;
            text-align: center;
            background: linear-gradient(135deg, var(--blue), var(--green));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 25px;
        }
        .profile-card {
            padding: 20px;
            border-radius: 20px;
            background: var(--glass);
            border: 1px solid var(--border);
            margin-bottom: 25px;
            text-align: center;
        }
        .profile-avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            border: 3px solid var(--blue);
            margin-bottom: 10px;
        }
        .profile-name {
            font-size: 18px;
            font-weight: 600;
            margin: 10px 0 5px;
        }
        .profile-role {
            font-size: 12px;
            color: var(--green);
            text-transform: uppercase;
        }
        .section-title {
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: var(--blue);
            margin: 20px 0 15px;
            font-weight: 600;
        }
        .nav-button {
            width: 100%;
            padding: 14px 20px;
            margin-bottom: 8px;
            border: 1px solid transparent;
            border-radius: 15px;
            background: var(--glass);
            color: var(--text);
            cursor: pointer;
            text-align: left;
            font-size: 14px;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .nav-button:hover {
            transform: translateX(8px);
            background: linear-gradient(135deg, var(--blue), var(--green));
            color: #000;
        }
        .logout-btn {
            margin-top: auto;
            background: rgba(239,68,68,0.1);
            border-color: rgba(239,68,68,0.3);
        }
        .logout-btn:hover {
            background: #ef4444;
            border-color: #ef4444;
            color: white;
        }
        .main {
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        .topbar {
            height: 80px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 30px;
            background: var(--glass);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
        }
        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--green);
            animation: statusPulse 2s infinite;
        }
        @keyframes statusPulse {
            0%,100% { box-shadow: 0 0 0 0 rgba(0,255,136,0.4); }
            50% { box-shadow: 0 0 0 15px rgba(0,255,136,0); }
        }
        .current-time {
            font-family: monospace;
            font-size: 14px;
            color: var(--sub);
        }
        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 30px;
        }
        .welcome-screen {
            text-align: center;
            margin: auto;
            padding: 50px 20px;
        }
        .welcome-screen h1 {
            font-size: 72px;
            font-family: "Orbitron", sans-serif;
            background: linear-gradient(135deg, var(--blue), var(--green), var(--purple));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }
        .command-suggestions {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            max-width: 800px;
            margin: 30px auto;
        }
        .suggestion-chip {
            padding: 12px 20px;
            background: var(--glass);
            border: 1px solid var(--border);
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 14px;
        }
        .suggestion-chip:hover {
            background: var(--blue);
            color: #000;
            border-color: var(--blue);
            transform: translateY(-3px);
        }
        .messages {
            max-width: 900px;
            margin: 0 auto;
        }
        .message {
            padding: 18px 25px;
            border-radius: 20px;
            margin-bottom: 20px;
            animation: slideIn 0.3s ease;
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .user-message {
            background: rgba(0,212,255,0.15);
            border-left: 4px solid var(--blue);
            margin-left: 20%;
        }
        .ai-message {
            background: rgba(0,255,136,0.12);
            border-left: 4px solid var(--green);
            margin-right: 20%;
        }
        .message-header {
            font-weight: 600;
            margin-bottom: 10px;
            font-size: 14px;
            text-transform: uppercase;
        }
        .input-area {
            padding: 25px;
            background: var(--glass);
            backdrop-filter: blur(20px);
            border-top: 1px solid var(--border);
        }
        .input-container {
            display: flex;
            gap: 15px;
            max-width: 900px;
            margin: 0 auto;
        }
        .input-container input {
            flex: 1;
            padding: 16px 25px;
            border: 2px solid transparent;
            border-radius: 20px;
            background: rgba(255,255,255,0.08);
            color: var(--text);
            font-size: 16px;
            outline: none;
        }
        .input-container input:focus {
            border-color: var(--blue);
            background: rgba(255,255,255,0.12);
        }
        .send-button {
            padding: 16px 30px;
            border: none;
            border-radius: 20px;
            background: linear-gradient(135deg, var(--blue), var(--green));
            color: #000;
            font-weight: 700;
            cursor: pointer;
        }
        .send-button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 30px rgba(0,212,255,0.3);
        }
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: rgba(255,255,255,0.05); }
        ::-webkit-scrollbar-thumb { background: var(--blue); border-radius: 10px; }
    </style>
</head>
<body>
    <div class="bg"></div>

    <div class="login-screen" id="loginScreen">
        <div class="login-box">
            <div class="ai-logo">
                <img src="https://cdn-icons-png.flaticon.com/512/8649/8649595.png" alt="JARVIS AI" style="width:100%;height:100%;">
            </div>
            <div class="login-title">JARVIS AI</div>
            <div class="input-group">
                <i class="fas fa-user"></i>
                <input type="text" id="fullname" placeholder="Full Name" autocomplete="name">
            </div>
            <div class="input-group">
                <i class="fas fa-envelope"></i>
                <input type="email" id="username" placeholder="Email Address" autocomplete="email">
            </div>
            <div class="input-group">
                <i class="fas fa-lock"></i>
                <input type="password" id="password" placeholder="Password" autocomplete="current-password">
            </div>
            <div class="error-message" id="errorMessage"></div>
            <button class="btn" id="registerBtn">REGISTER</button>
            <button class="btn btn-outline" id="loginBtn">LOGIN</button>
        </div>
    </div>

    <div class="app" id="app">
        <div class="container">
            <div class="sidebar">
                <div class="logo-circle" style="text-align:center;">
                    <img src="https://cdn-icons-png.flaticon.com/512/8649/8649595.png" alt="JARVIS" style="width:100%;height:100%;">
                </div>
                <div class="app-title">JARVIS AI</div>
                <div class="profile-card">
                    <img src="https://cdn-icons-png.flaticon.com/512/9131/9131529.png" alt="Profile" class="profile-avatar">
                    <div class="profile-name" id="profileName">User</div>
                    <div class="profile-role">Advanced AI User</div>
                </div>

                <div class="section-title">🎞️ Entertainment</div>
                <button class="nav-button" onclick="openWebsite('https://www.youtube.com')"><i class="fab fa-youtube" style="color:#ff0000;"></i> YouTube</button>
                <button class="nav-button" onclick="openWebsite('https://www.netflix.com')"><i class="fas fa-film" style="color:#e50914;"></i> Netflix</button>
                <button class="nav-button" onclick="openWebsite('https://www.hotstar.com')"><i class="fas fa-tv" style="color:#1f80e0;"></i> Hotstar</button>
                <button class="nav-button" onclick="openWebsite('https://www.primevideo.com')"><i class="fas fa-play-circle" style="color:#00a8e1;"></i> Prime Video</button>

                <div class="section-title">🎮Games</div>
                <button class="nav-button" onclick="openWebsite('https://poki.com')"><i class="fas fa-gamepad" style="color:#ff6b6b;"></i> Poki</button>
                <button class="nav-button" onclick="openWebsite('https://www.crazygames.com')"><i class="fas fa-ghost" style="color:#a55eea;"></i> CrazyGames</button>
                <button class="nav-button" onclick="openWebsite('https://www.miniclip.com')"><i class="fas fa-puzzle-piece" style="color:#26de81;"></i> Miniclip</button>
                <button class="nav-button" onclick="openWebsite('https://www.roblox.com')"><i class="fas fa-cube" style="color:#ff9a00;"></i> Roblox</button>

                <div class="section-title">📁Microsoft Office</div>
                <button class="nav-button" onclick="openWebsite('https://www.office.com/launch/word')"><i class="fas fa-file-word" style="color:#2b579a;"></i> Microsoft Word</button>
                <button class="nav-button" onclick="openWebsite('https://www.office.com/launch/excel')"><i class="fas fa-file-excel" style="color:#217346;"></i> Microsoft Excel</button>
                <button class="nav-button" onclick="openWebsite('https://www.office.com/launch/powerpoint')"><i class="fas fa-file-powerpoint" style="color:#d24726;"></i> Microsoft PowerPoint</button>
                <button class="nav-button" onclick="openWebsite('https://www.office.com/launch/onenote')"><i class="fas fa-sticky-note" style="color:#7719aa;"></i> OneNote</button>
                <button class="nav-button" onclick="openWebsite('https://outlook.live.com')"><i class="fas fa-envelope-open-text" style="color:#0078d4;"></i> Outlook</button>

                <div class="section-title">🎨Design Tools</div>
                <button class="nav-button" onclick="openWebsite('https://www.canva.com')"><i class="fas fa-palette" style="color:#00c4cc;"></i> Canva</button>
                <button class="nav-button" onclick="openWebsite('https://www.figma.com')"><i class="fab fa-figma" style="color:#a259ff;"></i> Figma</button>
                <button class="nav-button" onclick="openWebsite('https://www.photopea.com')"><i class="fas fa-image" style="color:#00bcd4;"></i> Photopea</button>

                <div class="section-title">📊 Productivity</div>
                <button class="nav-button" onclick="openWebsite('https://docs.google.com')"><i class="fas fa-file-alt" style="color:#4285f4;"></i> Google Docs</button>
                <button class="nav-button" onclick="openWebsite('https://sheets.google.com')"><i class="fas fa-table" style="color:#34a853;"></i> Google Sheets</button>
                <button class="nav-button" onclick="openWebsite('https://slides.google.com')"><i class="fas fa-presentation" style="color:#fbbc04;"></i> Google Slides</button>
                <button class="nav-button" onclick="openWebsite('https://www.notion.so')"><i class="fas fa-clipboard-list" style="color:#ffffff;"></i> Notion</button>
                <button class="nav-button" onclick="openWebsite('https://trello.com')"><i class="fab fa-trello" style="color:#0079bf;"></i> Trello</button>

                <div class="section-title">✨AI Tools</div>
                <button class="nav-button" onclick="openWebsite('https://chat.openai.com')"><i class="fas fa-brain" style="color:#74aa9c;"></i> ChatGPT</button>
                <button class="nav-button" onclick="openWebsite('https://gemini.google.com')"><i class="fas fa-gem" style="color:#4285f4;"></i> Gemini</button>

                <div class="section-title">🔍Tools</div>
                <button class="nav-button" onclick="openWebsite('https://mail.google.com')"><i class="fas fa-envelope" style="color:#ea4335;"></i> Gmail</button>
                <button class="nav-button" onclick="openWebsite('https://www.wikipedia.org')"><i class="fas fa-book" style="color:#000;"></i> Wikipedia</button>

                <button class="nav-button logout-btn" onclick="logout()"><i class="fas fa-sign-out-alt"></i> Logout</button>
            </div>

            <div class="main">
                <div class="topbar">
                    <div style="display:flex;align-items:center;gap:15px;">
                        <div class="status-dot"></div>
                        <span style="color:var(--green);font-weight:600;">ONLINE</span>
                    </div>
                    <div class="current-time" id="clock">--:--:--</div>
                    <div style="color:var(--sub);"><i class="fas fa-wifi"></i> Connected</div>
                </div>
                <div class="chat-container">
                    <div class="welcome-screen" id="welcomeScreen">
                        <h1>JARVIS</h1>
                        <p style="color:var(--sub);font-size:18px;margin-bottom:30px;">Your Advanced AI Assistant</p>
                        <div class="command-suggestions">
                            <div class="suggestion-chip" onclick="quickCommand('Open Microsoft Word')"><i class="fas fa-file-word"></i> Open Word</div>
                            <div class="suggestion-chip" onclick="quickCommand('Open Microsoft Excel')"><i class="fas fa-file-excel"></i> Open Excel</div>
                            <div class="suggestion-chip" onclick="quickCommand('Open Canva')"><i class="fas fa-palette"></i> Open Canva</div>
                            <div class="suggestion-chip" onclick="quickCommand('Open Google Docs')"><i class="fas fa-file-alt"></i> Open Google Docs</div>
                            <div class="suggestion-chip" onclick="quickCommand('Open Roblox')"><i class="fas fa-cube"></i> Open Roblox</div>
                            <div class="suggestion-chip" onclick="quickCommand('Tell me a joke')"><i class="fas fa-laugh"></i> Tell me a joke</div>
                        </div>
                    </div>
                    <div class="messages" id="messages"></div>
                </div>
                <div class="input-area">
                    <div class="input-container">
                        <input type="text" id="userInput" placeholder="Ask JARVIS AI anything..." autocomplete="off">
                        <button class="send-button" id="sendBtn">SEND</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function storageAvailable() {
            try {
                var test = '__storage_test__';
                localStorage.setItem(test, test);
                localStorage.removeItem(test);
                return true;
            } catch(e) {
                return false;
            }
        }

        function showError(msg) {
            document.getElementById('errorMessage').textContent = msg;
            console.error('JARVIS Error:', msg);
        }

        function clearError() {
            document.getElementById('errorMessage').textContent = '';
        }

        function registerUser() {
            clearError();
            console.log('Register function called');
            
            var fullname = document.getElementById('fullname').value.trim();
            var email = document.getElementById('username').value.trim();
            var password = document.getElementById('password').value.trim();

            if (!fullname || !email || !password) {
                showError('Please fill in all fields');
                return;
            }
            if (!email.includes('@') || !email.includes('.')) {
                showError('Please enter a valid email');
                return;
            }
            if (password.length < 6) {
                showError('Password must be at least 6 characters');
                return;
            }

            if (!storageAvailable()) {
                showError('localStorage not available. Check browser settings.');
                return;
            }

            var userData = {
                fullName: fullname,
                email: email,
                password: password,
                createdAt: new Date().toISOString()
            };

            try {
                localStorage.setItem('jarvis_user', JSON.stringify(userData));
                console.log('User registered and saved:', userData);
                alert('Registration successful! Logging you in...');
                showApp(fullname);
            } catch(e) {
                showError('Failed to save user data.');
                console.error(e);
            }
        }

        function loginUser() {
            clearError();
            console.log('Login function called');
            
            var email = document.getElementById('username').value.trim();
            var password = document.getElementById('password').value.trim();

            if (!email || !password) {
                showError('Please enter email and password');
                return;
            }

            if (!storageAvailable()) {
                showError('localStorage not available. Check browser settings.');
                return;
            }

            var userStr = localStorage.getItem('jarvis_user');
            console.log('Retrieved user data:', userStr);
            
            if (!userStr) {
                showError('No user found. Please register first.');
                return;
            }

            try {
                var userData = JSON.parse(userStr);
                if (email === userData.email && password === userData.password) {
                    console.log('Login successful for', userData.fullName);
                    showApp(userData.fullName);
                } else {
                    showError('Invalid email or password');
                }
            } catch(e) {
                showError('Error reading user data. Please register again.');
                console.error(e);
            }
        }

        function showApp(fullName) {
            console.log('Showing app for', fullName);
            document.getElementById('loginScreen').style.display = 'none';
            document.getElementById('app').style.display = 'block';
            document.getElementById('profileName').textContent = fullName;
            
            try {
                localStorage.setItem('jarvis_session', JSON.stringify({
                    user: fullName,
                    loginTime: new Date().toISOString()
                }));
            } catch(e) {
                console.warn('Could not save session', e);
            }
            
            addMessage('ai', 'Welcome back, ' + fullName + '! JARVIS AI is ready to assist you. Type "help" for all commands.');
            updateClock();
        }

        window.addEventListener('load', function() {
            console.log('Page loaded, checking session...');
            
            document.getElementById('registerBtn').addEventListener('click', registerUser);
            document.getElementById('loginBtn').addEventListener('click', loginUser);
            document.getElementById('sendBtn').addEventListener('click', sendMessage);
            document.getElementById('userInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') sendMessage();
            });

            if (!storageAvailable()) {
                showError('localStorage not available. Some features may not work.');
            }

            var sessionStr = localStorage.getItem('jarvis_session');
            if (sessionStr) {
                try {
                    var session = JSON.parse(sessionStr);
                    console.log('Session found for', session.user);
                    showApp(session.user);
                } catch(e) {
                    console.error('Invalid session data');
                }
            }
            updateClock();
            setInterval(updateClock, 1000);
        });

        function logout() {
            if (confirm('Are you sure you want to logout?')) {
                localStorage.removeItem('jarvis_session');
                location.reload();
            }
        }

        function updateClock() {
            var now = new Date();
            var timeString = now.toLocaleTimeString('en-US', {
                hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true
            });
            document.getElementById('clock').textContent = timeString;
        }

        function addMessage(type, text) {
            var welcome = document.getElementById('welcomeScreen');
            if (welcome) welcome.style.display = 'none';
            var container = document.getElementById('messages');
            var div = document.createElement('div');
            div.className = 'message ' + type + '-message';
            div.innerHTML = '<div class="message-header">' + (type === 'user' ? '👤 YOU' : '⚡ JARVIS AI') + '</div><div class="message-content">' + text + '</div>';
            container.appendChild(div);
            container.scrollTop = container.scrollHeight;
        }

        function quickCommand(cmd) {
            document.getElementById('userInput').value = cmd;
            sendMessage();
        }

        function openWebsite(url) {
            window.open(url, '_blank');
            addMessage('ai', 'Opening ' + url + '...');
        }

        function speak(text) {
            if ('speechSynthesis' in window) {
                speechSynthesis.cancel();
                var utterance = new SpeechSynthesisUtterance(text);
                utterance.rate = 1;
                utterance.pitch = 1.1;
                speechSynthesis.speak(utterance);
            }
        }

        function sendMessage() {
            var input = document.getElementById('userInput');
            var text = input.value.trim();
            if (!text) return;
            addMessage('user', text);
            input.value = '';
            var lower = text.toLowerCase();
            var response = '';

            // Entertainment commands
            if (lower.includes('open youtube') || lower.includes('youtube')) {
                openWebsite('https://www.youtube.com');
                return;
            } else if (lower.includes('open netflix') || lower.includes('netflix')) {
                openWebsite('https://www.netflix.com');
                return;
            } else if (lower.includes('open hotstar') || lower.includes('hotstar')) {
                openWebsite('https://www.hotstar.com');
                return;
            } else if (lower.includes('open prime video') || lower.includes('prime video')) {
                openWebsite('https://www.primevideo.com');
                return;
            }

            // Game commands
            else if (lower.includes('open poki') || lower.includes('poki')) {
                openWebsite('https://poki.com');
                return;
            } else if (lower.includes('open crazy games') || lower.includes('crazygames') || lower.includes('crazy games')) {
                openWebsite('https://www.crazygames.com');
                return;
            } else if (lower.includes('open miniclip') || lower.includes('miniclip')) {
                openWebsite('https://www.miniclip.com');
                return;
            } else if (lower.includes('open roblox') || lower.includes('roblox')) {
                openWebsite('https://www.roblox.com');
                return;
            }

            // Microsoft Office commands
            else if (lower.includes('open microsoft word') || lower.includes('open word') || lower.includes('microsoft word')) {
                openWebsite('https://www.office.com/launch/word');
                return;
            } else if (lower.includes('open microsoft excel') || lower.includes('open excel') || lower.includes('microsoft excel')) {
                openWebsite('https://www.office.com/launch/excel');
                return;
            } else if (lower.includes('open microsoft powerpoint') || lower.includes('open powerpoint') || lower.includes('microsoft powerpoint')) {
                openWebsite('https://www.office.com/launch/powerpoint');
                return;
            } else if (lower.includes('open onenote') || lower.includes('onenote')) {
                openWebsite('https://www.office.com/launch/onenote');
                return;
            } else if (lower.includes('open outlook') || lower.includes('outlook')) {
                openWebsite('https://outlook.live.com');
                return;
            }

            // Design tools commands
            else if (lower.includes('open canva') || lower.includes('canva')) {
                openWebsite('https://www.canva.com');
                return;
            } else if (lower.includes('open figma') || lower.includes('figma')) {
                openWebsite('https://www.figma.com');
                return;
            } else if (lower.includes('open photopea') || lower.includes('photopea')) {
                openWebsite('https://www.photopea.com');
                return;
            }

            // Productivity commands
            else if (lower.includes('open google docs') || lower.includes('google docs')) {
                openWebsite('https://docs.google.com');
                return;
            } else if (lower.includes('open google sheets') || lower.includes('google sheets')) {
                openWebsite('https://sheets.google.com');
                return;
            } else if (lower.includes('open google slides') || lower.includes('google slides')) {
                openWebsite('https://slides.google.com');
                return;
            } else if (lower.includes('open notion') || lower.includes('notion')) {
                openWebsite('https://www.notion.so');
                return;
            } else if (lower.includes('open trello') || lower.includes('trello')) {
                openWebsite('https://trello.com');
                return;
            }

            // AI Tools commands
            else if (lower.includes('open chatgpt') || lower.includes('chatgpt')) {
                openWebsite('https://chat.openai.com');
                return;
            } else if (lower.includes('open gemini') || lower.includes('gemini')) {
                openWebsite('https://gemini.google.com');
                return;
            }

            // Tools commands
            else if (lower.includes('open gmail') || lower.includes('gmail')) {
                openWebsite('https://mail.google.com');
                return;
            } else if (lower.includes('open wikipedia') || lower.includes('wikipedia')) {
                openWebsite('https://www.wikipedia.org');
                return;
            }

            // Greetings
            if (lower.match(/^(hello|hi|hey|greetings)/)) {
                var hour = new Date().getHours();
                var greeting = 'Hello';
                if (hour < 12) greeting = 'Good morning';
                else if (hour < 18) greeting = 'Good afternoon';
                else greeting = 'Good evening';
                response = greeting + '! JARVIS AI at your service.';
            } else if (lower.includes('time')) {
                response = 'Current time is ' + new Date().toLocaleTimeString('en-US', {hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:true,timeZoneName:'short'}) + '.';
            } else if (lower.includes('date')) {
                response = 'Today is ' + new Date().toLocaleDateString('en-US', {weekday:'long',year:'numeric',month:'long',day:'numeric'}) + '.';
            } else if (lower.includes('joke')) {
                var jokes = [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "Why did the AI go to therapy? It had too many neural issues!",
                    "What do you call a computer that sings? A Dell!",
                    "Why do programmers prefer dark mode? Because light attracts bugs!",
                    "What's a computer's favorite beat? An algorithm!"
                ];
                response = jokes[Math.floor(Math.random() * jokes.length)];
            } else if (lower.includes('help') || lower.includes('commands')) {
                response = "Available commands:\\n\\n fa-sa-tv Entertainment: Open YouTube, Netflix, Hotstar, Prime Video\\n🎮 Games: Open Poki, CrazyGames, Miniclip, Roblox\\n📂 Microsoft Office: Open Word, Excel, PowerPoint, OneNote, Outlook\\n🎨 Design: Open Canva, Figma, Photopea\\n📊 Productivity: Open Google Docs, Sheets, Slides, Notion, Trello\\n🤖 AI: Open ChatGPT, Gemini\\n🛠️ Tools: Open Gmail, Wikipedia\\n\\nOther: Ask time, date, tell me a joke, or search any topic!";
            } else {
                var searchText = text.replace(/^(who is|what is|tell me about|define|explain)/i, '').trim();
                if (searchText) {
                    fetch('https://en.wikipedia.org/api/rest_v1/page/summary/' + encodeURIComponent(searchText))
                        .then(function(res) { return res.json(); })
                        .then(function(data) {
                            if (data.extract) {
                                addMessage('ai', data.extract);
                                speak(data.extract);
                            } else {
                                addMessage('ai', "I couldn't find information on that.");
                            }
                        })
                        .catch(function() {
                            addMessage('ai', "Error connecting to knowledge base.");
                        });
                    return;
                } else {
                    response = "I didn't understand. Type 'help' for all available commands.";
                }
            }
            addMessage('ai', response);
            speak(response);
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    print("JARVIS AI server starting...")
    print("Open http://127.0.0.1:5000 in your browser")
    app.run(debug=True)
