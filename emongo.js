const express=require("express")
const app=express()
const mg=require("mongoose")
mg.connect("mongodb://localhost:27017/mydb")
.then(()=>console.log("connection successful"))
.catch((e)=>console.log("connection failed",e))
const sc=mg.Schema({username:{type:String,required:true,maxlength:15},
password:{type:String,required:true,minlength:8,maxlength:16}});
const users=mg.model("users",sc)
app.use(express.static(__dirname,{index:"eform.html"}))
app.get("/signup",async(req,res)=>{
    try{
        var u=req.query.uname;
        var p=req.query.pwd;
        var us1=new users({username:u,password:p})
        var r=await us1.save();
        console.log("Insert Success",r)
        res.send(u+ "inserted successfully")
    }
    catch(e){
        res.send("Insert failed",e)
    }
})
app.listen(5000,console.log("listning at http://localhost:5000"))