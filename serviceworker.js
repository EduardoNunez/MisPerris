var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/formulario/',
    '/accounts/login/',
    '/listar_mascotas/',
    '/agregarMascota/',
    '/static/core/css/estilos.css',
    '/static/core/img/logo.png',
    '/media/media/descarga_4.jpg',
    '/media/media/descarga_5.jpg',
    '/media/media/descarga_8.jpg',
    '/static/core/img/social-inst.png',
    '/static/core/img/social-twitter.png',
    '/static/core/img/socialfacebook.png',
    '/static/core/img/socialplus.png',
    '/media/media/descarga_7.jpg',
    '/media/media/descarga.jpg',
    '/media/media/images_3.jpg',
    '/static/core/img/rescate.jpg',
    '/static/core/img/crowfunding.jpg',

    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    '/static/core/js/inicializacion.js'

];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
           /* r = null
            fetch(event.request)
            .then(function() {
                
            })
            .catch(function() {
                r = response;
            })

            if(response) {
                return response;
            }*/
            
            return fetch(event.request).catch(function() {
                console.log("no funciona")
                return response;
            });
        })
    );

});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyCFkFIG7zDk_QUaqAuEpZanH_daS3lcjyI",
    authDomain: "misperris-95ad7.firebaseapp.com",
    databaseURL: "https://misperris-95ad7.firebaseio.com",
    projectId: "misperris-95ad7",
    storageBucket: "misperris-95ad7.appspot.com",
    messagingSenderId: "565738962204"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();

// Programamos una funcion que estara escuchando cuando llegue una notificacion desde
// firebase.

messaging.setBackgroundMessageHandler(function(payload){

    // El payload contendrá el mensaje destinado al usuario.
    var title = "notificacion"
    var options = {

        body:"Este es el cuerpo del mensaje"

    }

    // Mostramos la notificacion al usuario.
    return self.registration.showNotification(title, options);

})