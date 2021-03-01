var jomas = ["---", "💃 Dejas", "🎼 Mūzika", "🎬 Teātra māksla", "⚽️ Sports", "🎨 Vizuālā māksla", "🔧 Tehniskā jaunrade", "🌿 Vides izglītība", "💻 Informācijas tehnoloģijas", "📚 Akadēmiskā izglītība", " ❗ Citas programmas"]
for (var i = 0; i < jomas.length; i++) {
    var option = document.createElement("option");
    option.value = jomas[i];
    option.textContent = jomas[i];
    document.getElementById("joma").appendChild(option);
}