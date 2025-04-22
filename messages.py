import random
import os

portfolio = os.getenv("PORTFOLIO_LINK", "https://excelemma.vercel.app/")
cv = os.getenv("CV_LINK", "https://docs.google.com/document/d/1seVPcpl7XCzwfP76ukQOKnNWt15Q2q9_")

messages = [
    f"This video is amazing! By the way, I'm a fullstack/mobile developer looking for opportunities. Feel free to check out my portfolio: {portfolio} and my CV: {cv}",
    f"Great content as always! Just wanted to share that I'm a developer available for freelance work. Here's my portfolio: {portfolio}",
    f"Loved this upload! If you or someone you know needs a fullstack/mobile dev, here's my portfolio: {portfolio}. Would love to connect!",
    f"Fantastic video! Quick note: I'm a React/Next/React Native developer open to new opportunities. Check out my work here: {portfolio}",
    f"This was super helpful! BTW, I'm a fullstack developer available for hire. Here's my portfolio: {portfolio} and my CV: {cv}",
    f"Really enjoyed this video! If you're ever looking for a developer, feel free to check out my portfolio: {portfolio}. I'd love to collaborate!",
    f"Awesome video! Just putting it out there—I'm a fullstack/mobile developer open to freelance or full-time roles. Portfolio: {portfolio}",
    f"This was such a great watch! If you or anyone you know needs a developer, here's my portfolio: {portfolio}. Always happy to connect!",
    f"Amazing work on this video! By the way, I'm a developer specializing in React and mobile apps. Here's my portfolio: {portfolio}. Let's connect!",
    f"Really inspiring content! Just wanted to share my portfolio in case you're looking for a developer: {portfolio}. Would love to work together!"
]

def get_random_message():
    return random.choice(messages)