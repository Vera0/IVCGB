"use strict";

const express = require('express');
const http = require('http');

const app = express();
const server = http.Server(app);

const path = require('path');

app.use(express.static(path.join(__dirname, '/public')));

app.get('*', (request, response) => {
 response.sendFile(path.resolve(__dirname, 'public', 'index.html'))
});

server.listen(8080);