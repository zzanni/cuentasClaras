const CACHE_NAME = 'cuanto-gastamos-static-v2.2.1';
const urlsToCache = [
  './',
  './index.html',
  './manifest.json'
];

// Instala el SW y cachea los archivos iniciales
self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

// Siempre busca primero en la red; si falla, usa el caché
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Actualiza el caché con el nuevo archivo
        const responseClone = response.clone();
        caches.open(CACHE_NAME).then(cache => {
          cache.put(event.request, responseClone);
        });
        return response;
      })
      .catch(() => caches.match(event.request))
  );
});

// Limpia cachés viejos cuando se activa el nuevo SW
self.addEventListener('activate', event => {
  self.clients.claim();
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.map(key => {
          if (key !== CACHE_NAME && key.startsWith('cuanto-gastamos')) {
            return caches.delete(key);
          }
        })
      )
    )
  );
});