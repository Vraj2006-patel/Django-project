//1.Require Mongoose
const mg=require("mongoose")
//3. Create a schema 
     const sc=mg.Schema(
     {sname:String,
      rollno:Number,
      gender:String,
      pass:Boolean,
      doj:Date,
      marks:Array,
      division:Object   
     }
 );
//2.Connect Mongodb
mg.connect("mongodb://localhost:27017/mydb")
.then(()=>console.log("Connection Successful"))
.catch((e)=>console.log("Connection failed",e));

//4.Create a Model(table)
mg.pluralize(null)
const student=new mg.model("student",sc)

//5.Do operations
async function created()
{
    try{
        //Instance Method
    const s1=new student(
    {
        sname:"Oliver",
        rollno:1,
        gender:"Female",
        pass:true,
        doj:new Date(),
        marks:[21,23,18],
        division:{department:"SY1",class:"A8"} 
    }    
    );
const r= await s1.save()
console.log("Insert Success",r);
    }
    catch(e)
    {
        console.log("Cannot Insert",e)
    }
}
//created()
//class based method
// 1 findone
// 2 find
// 3 insertMany
// 4 updateOne
// 5 UpdateMany
// 6 deleteOne
// 7 deleteMany
// 8 countDocuments
// 9 findByIdAndUpdate
// 10 findByIdAndUpdate

var students=[
    {
        sname:"Henry",rollno:25,gender:"Male",pass:false,doj:new Date("2025-05-26"),
        marks:[17,16,21], division:{department:"SY1",class:"A2"}
    },
    {
        sname:"Jency",rollno:182,gender:"Female",pass:true,doj:new Date(),
        marks:[24,14,12], division:{department:"SY1",class:"A5"}
    },    
    {
        sname:"Riya",rollno:184,gender:"Female",pass:true,doj:new Date(),
        marks:[20,10,15], division:{department:"SY1",class:"A7"}
    },
    {
        sname:"Joy",rollno:82,gender:"Male",pass:true,doj:new Date(),
        marks:[12,23,20], division:{department:"SY1",class:"A5"}
    }    
] 
const createm=async()=>{
    try{
    const r1=await student.insertMany(students)
    console.log("Insert success",r1)
    }

catch(e)
{
    console.log("Cannot Insert",e)
}
}
//createm();
const  operations= async()=>{
      try{
    // var fs=await student.find()
    // console.log(fs)
    var res=[];
    res.push(await student.findByIdAndUpdate("6a47630b5108eb0863e519e1",
{sname:"Oliver"}))
    // res.push(await student.find({rollno:{$gt:18}}))
    // res.push(await student.updateOne({sname:"Oliver"},{$set:{sname:"olivernew"}}))
    // res.push(await student.updateMany({rollno:{$gt:18}},{$inc:{rollno:3}}))
    res.push(await student.deleteOne({sname:"Henry"}))
    res.push(await student.findByIdAndDelete("6a47630b5108eb0863e519e1"))
    res.push(await student.deleteMany({gender:"male"}))

     console.log("Result is",res);
    }

catch(e)
{
    console.log("Operation Unsuccessful",e)
}
}
operations();