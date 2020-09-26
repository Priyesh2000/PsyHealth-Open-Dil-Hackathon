var express = require('express')
var bodyParser = require('body-parser')
var ejs = require('ejs')

var admin = require("firebase-admin");

var serviceAccount = "PsyHealth_Service_key.json"

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://psyhealth-c07b6.firebaseio.com"
});

var registeredData = {}
var registeredKeys = []
var appointmentData = {}
var appointmentKeys = []

var database = admin.database();
var signupDatabase =  database.ref("Signup_Data")
var appointmentDatabase = database.ref("Appointment_Data")

signupDatabase.on('value',(data)=>{
    registeredData = (data.val())
    registeredKeys = Object.keys(registeredData)
},(err)=>{
   console.log("Error!")
   console.log(err)
})

appointmentDatabase.on('value',(data)=>{
    appointmentData = (data.val());
    appointmentKeys = Object.keys(appointmentData);
},(err)=>{
    console.log("Error!")
    console.log(err)
})


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

app.post("/signup",(req,res)=>{
    var signupData = {
        name: req.body.name,
        email:req.body.email,
        pass:req.body.password,
        gender:req.body.gender,
        dob:req.body.dob,
        slot : req.body.slot
    }
    console.log(signupData)
    signupDatabase.push(signupData)
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
