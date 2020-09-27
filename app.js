var express = require('express')
var bodyParser = require('body-parser')
var ejs = require('ejs')
var firebase = require("firebase")

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


// Get a reference to the database service
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

app.post('/login',(req,res)=>{
    var loginFormData = {
        email : req.body.email,
        pass : req.body.password
    }
    console.log(loginFormData)

    var found = 0

    for(var i=0;i<registeredKeys.length;i++){
        key = registeredKeys[i]
        if (loginFormData.email == registeredData[key].email & loginFormData.pass == registeredData[key].pass){
            res.render("dashboard",{name:registeredData[key].name , data : appointmentData , keys : appointmentKeys})
            found = 1
        }
    }

    if (found == 1 ){
        console.log("Match Found")
    }else{
        res.render('login', { data :"Please check the Email or Password."})
        console.log("Match Not Found")
    }
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

app.post('/appointment',(req,res)=>{
    var AppointmentformData ={
        patientName : req.body.patientname,
        patientEmail : req.body.patientemail,
        patientNumber : req.body.patientno,
        patientAilment : req.body.patientailment,
        patientDate : req.body.patientdate,
        patientTime : req.body.patienttime,
        patientDoctor : req.body.patientdoctor
    }
    console.log(AppointmentformData)
    appointmentDatabase.push(AppointmentformData)
})

app.listen(port , (err)=>{
    if(err){console.log(err)}
    else{
        console.log("Server successfully Started at "+port )
    }
})