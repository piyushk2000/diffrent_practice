const express = require('express')

const { sequelize, User, Post } = require('./models')

const app = express()
app.use(express.json())