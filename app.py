import streamlit as st
from streamlit.components.v1 import html
import base64

st.set_page_config(page_title="Valentine 💘", layout="centered")

st.markdown(
    "<h1 style='text-align:center;'>Will you be my Valentine? 💖</h1>",
    unsafe_allow_html=True
)

# Upload photo (only you see this while setting up)
uploaded_file = st.file_uploader(
    "Upload a picture of us 💑 (JPG / PNG)",
    type=["jpg", "jpeg", "png"]
)

image_base64 = ""
if uploaded_file:
    image_bytes = uploaded_file.read()
    image_base64 = base64.b64encode(image_bytes).decode()

html(
    f"""
    <style>
        body {{
            background: linear-gradient(to bottom right, #ffdde1, #ee9ca7);
            text-align: center;
            font-family: Arial, sans-serif;
        }}

        #container {{
            position: relative;
            height: 300px;
            margin-top: 40px;
        }}

        #yesBtn {{
            font-size: 22px;
            padding: 12px 26px;
            border-radius: 14px;
            border: none;
            background-color: #ff4d6d;
            color: white;
            cursor: pointer;
        }}

        #noBtn {{
            position: absolute;
            font-size: 18px;
            padding: 10px 22px;
            border-radius: 14px;
            border: none;
            background-color: #adb5bd;
            color: white;
            cursor: pointer;
        }}
    </style>

    <div id="container">
        <button id="yesBtn" onclick="yesClicked()">YES 💕</button>
        <button id="noBtn">NO 🙅‍♂️</button>
    </div>

    <div id="result"></div>

    <!-- Confetti library -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <script>
        let yesSize = 22;
        const noBtn = document.getElementById("noBtn");
        const yesBtn = document.getElementById("yesBtn");

        function moveNoButton() {{
            const x = Math.random() * 250;
            const y = Math.random() * 200;
            noBtn.style.left = x + "px";
            noBtn.style.top = y + "px";

            yesSize += 6;
            yesBtn.style.fontSize = yesSize + "px";
        }}

        noBtn.addEventListener("mouseover", moveNoButton);

        function heartConfetti() {{
            confetti({{
                particleCount: 160,
                spread: 90,
                origin: {{ y: 0.6 }},
                colors: ['#ff4d6d', '#ff758f', '#ffb3c1']
            }});
        }}

        function yesClicked() {{
            heartConfetti();
            setTimeout(heartConfetti, 400);
            setTimeout(heartConfetti, 800);

            document.getElementById("result").innerHTML = `
                <!-- Music starts ONLY after YES -->
                <iframe
                    width="0"
                    height="0"
                    src="https://www.youtube.com/embed/GxldQ9eX2wo?autoplay=1&loop=1&playlist=GxldQ9eX2wo"
                    frameborder="0"
                    allow="autoplay">
                </iframe>

                <h2>I love you ❤️😍</h2>
                {"<img src='data:image/png;base64," + image_base64 + "' width='320' style='border-radius:22px;'/>" if image_base64 else ""}
                <br><br>
                <img src="https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif" width="260">
            `;
        }}
    </script>
    """,
    height=620,
)
