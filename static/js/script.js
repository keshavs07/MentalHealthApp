function startVoice() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
        alert("Your browser does not support Voice Recognition.");
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        
        fetch('/voice', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        })
        .then(res => res.json())
        .then(data => {
            alert(
                "You: " + data.text +
                "\nSentiment: " + data.sentiment +
                "\nEmotion: " + data.emotion +
                "\nBot: " + data.response
            );
        });
    };

    recognition.onerror = function(event) {
        console.error("Speech recognition error:", event.error);
        alert("Error during voice recognition: " + event.error);
    };
}