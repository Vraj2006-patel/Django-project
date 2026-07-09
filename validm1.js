const val=require("validator")
const mg=require("mongoose");
const { isUppercase } = require("validator");
mg.connect("mongodb://localhost:27017/mydb")
.then(()=>console.log("Connection Successful"))
.catch((e)=>console.log("Connection failed",e));
const sc=mg.Schema({
    cname:{type:String,required:true,uppercase:true},
    username:{type:String,required:true,match:/[A-Za-z]+[0-9]+/},
    password:{type:String,minlength:8,maxlength:16},
    // age:{type:number,min:18,max:18},
    age:{type:Number,min:[18,"Age must be>18"],max:[80,"Age can be maximum 80"]},
    gender:{type:String,enum:["male","female","other"],
        trim:true
    },
    doj:{type:Date,default:new Date()},
    email:{type:String,
        validate:[val.isEmail,"incorrect Email id"],unique:true
    },
});
const customers=mg.model("customers",sc)
const created=async()=>{ try{const c1=new customers({cname:"Nency",username:"n120",
    password:"abcd1234",age:23,gender:"female",email:"a@7b.com"
})
var r1=await c1.save()
console.log("Insert Successful",r1)}
catch(e){
    console.log("Insert Failed",e.message)
}
}
created()