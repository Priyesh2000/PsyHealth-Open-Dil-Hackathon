var express = require('express')
var bodyParser = require('body-parser')
var ejs = require('ejs')

var app = express()
var port = 3000 || process.env.port

app.set('view engine' , 'ejs')

app.use(bodyParser.urlencoded({extended: true}))
app.use(express.static('public'))

app.get('/',(req,res)=>{
    res.render('index')
})
app.get('/dashboard',(req,res)=>{
    res.render('dashboard')
})

app.get('/login',(req,res)=>{
    res.render('login',{data:""})
})
app.get('/signup',(req,res)=>{
    res.render('signup')
})
app.get('/services',(req,res)=>{
    res.render('services')
})
app.get('/appointment',(req,res)=>{
    res.render('appointment',{name:"",data : registeredData , keys:registeredKeys})
})
app.listen(port , (err)=>{
    if(err){console.log(err)}
    else{
        console.log("Server successfully Started at "+port )
    }
})
