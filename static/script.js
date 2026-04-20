async function controllaCredenziali() {  
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    if (!username || !password) 
        return alert("Scrivi un nome e una password");
    const res = await fetch(`/login?username=${username}&password=$(password)`); //$: va prendere la variabile con il nome
    const dati = await res.json();
    document.getElementById('Risultato').innerText = dati.messaggio;
}
document.getElementById('btnregistrati').addEventListener('click', controllaCredenziali);