import mongoose from "mongoose"

mongoose.connect("MongoDB_URL")
    .then(() => {
        console.log("Database connected successfully.");
    }).catch((err) => {
        console.log("Database connection failed: ", err);
    })