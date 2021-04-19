function show_secret_key_and_form() {
    const secret_room_key_button = document.getElementById("secret_room_key_button");
    const secret_key_value = document.getElementById("generated_secret_key");
    const room_key_text = document.getElementById("room_key_text");
    const hidden_form = document.getElementById("hidden_form");
    if (secret_key_value.style.display === "none") {
        secret_key_value.style.display = "block";
        hidden_form.style.display = "block";
        room_key_text.style.display = "block";
        secret_room_key_button.style.display = "none";
        document.getElementById("generated_secret_key").innerHTML = secret_key.key;
    } else {
        secret_key_value.style.display = "none";
        hidden_form.style.display = "none";
    }
}