

    const username = document.getElementById('username')
    const password = document.getElementById('password')
   

    // Verificar el usuario y contraseña (en este caso, usuario preestablecido)
    if (username === "adm@gmail.com" && password === "adm123") {
        // Mostrar la página de inicio después de la verificación exitosa
        document.getElementById("login.html").style.display = "none";
        document.getElementById("Index.html").style.display = "block";
    } else {
        alert("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.");
    }


button.addEventListener('click', (e) => {
    e.preventDefault()
    const data = {
        username: username.value,
        password: password.value
    }

    console.log(data)
})

function logout() {
    // Ocultar la página de inicio y mostrar el formulario de inicio de sesión
    document.getElementById("Index.html").style.display = "none";
    document.getElementById("login.html").style.display = "block";

    // Limpiar campos de usuario y contraseña
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
}