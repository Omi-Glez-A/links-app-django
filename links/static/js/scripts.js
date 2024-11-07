// Navbar burger toogle
document.addEventListener('DOMContentLoaded', ()=> {
    // Obtenemos todos los elementos dentro de navbar-burger
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
    
    // se añade un evento sobre cada uno de estos elementos
    $navbarBurgers.forEach(element => {
        element.addEventListener('click', () => {
            //obtenemos el target del atributo data-target (que tiene que coincidir
            // con la id del elemento al que hacemos referencia en el data-target)
            const target = element.dataset.target;
            const $target = document.getElementById(target);

            element.classList.toggle('is-active');
            $target.classList.toggle('is-active');
        });
    });

    // const navbarBurger = document.getElementById('navbarBurger');

    // navbarBurger.addEventListener('click', () => {
    //     const target = navbarBurger.dataset.target;
    //     const $target = document.getElementById(target);

    //     navbarBurger.className.toggle('is-active');
    //     $target.className.toggle('is-active');
    // });

});