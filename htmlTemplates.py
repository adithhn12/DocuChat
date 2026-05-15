import base64
from pathlib import Path

def img_to_base64(image_path):
    """Convert image to base64"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except FileNotFoundError:
        return ""

css = '''
<style>
.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
    gap: 1rem;
}
.chat-message.user {
    background-color: #2b313e;
}
.chat-message.bot {
    background-color: #475063;
}
.chat-message .avatar {
    flex: 0 0 78px;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    flex: 1;
    padding: 0 1rem;
    color: #fff;
    line-height: 1.5;
}
</style>
'''

bot_avatar = img_to_base64(Path("static/AI.png"))
user_avatar = img_to_base64(Path("static/user.jpg"))

bot_template = f'''
<div class="chat-message bot">
    <div class="avatar">
        <img src="data:image/jpeg;base64,{bot_avatar}">
    </div>
    <div class="message">{{{{MSG}}}}</div>
</div>
'''

user_template = f'''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,{user_avatar}">
    </div>
    <div class="message">{{{{MSG}}}}</div>
</div>
'''