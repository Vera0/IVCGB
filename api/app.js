"use strict";

const express = require('express');
const bodyParser = require('body-parser');
const http = require('http');

const app = express();
const server = http.Server(app);

const path = require('path');

const AppRouter = require('./Routers/App.router');

app.use('/api'.concat('/demo'), AppRouter);

server.listen(8080);