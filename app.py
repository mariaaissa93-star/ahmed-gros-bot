import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# التحقق من أن السيرفر يعمل
@app.route("/", methods=["GET"])
def home():
    return "Ahmed Gros Bot Server is Running Successfully!", 200

# استقبال الردود والاشعارات من فيسبوك (Webhook)
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # للتحقق من الـ Webhook مع فيسبوك
        VERIFY_TOKEN = "ahmed_gros_verify_token_123"
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        if mode and token:
            if mode == "subscribe" and token == VERIFY_TOKEN:
                return challenge, 200
            else:
                return "Verification token mismatch", 403
        return "Hello World", 200

    elif request.method == "POST":
        # استقبال التعليقات أو الرسائل من فيسبوك
        data = request.json
        print("Received webhook data:", data)
        # هنا سنقوم بإضافة منطق الرد التلقائي على التعليقات لاحقاً
        return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)