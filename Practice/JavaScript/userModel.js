// It is a model of a user and it will define in json formate.
//  using curly braces to define the schema

import mongoose, { Schema } from "mongoose"

const userSchema = new Schema(
    {
        name: {
            type: String,
            required: true
        },
        email: {
            type: String,
            required: true,
        },
        password: {
            type: String,
            required: true
        }
    }, { timestamps: true })

    //here we hash the password using bcrypt library
userSchema.pre('save', async function (next) {
    if (!this.isModified("password"))
    return next();
    this.password = await bcrypt.hash(this.password, 10)
    next();
})

//this bcrypt.compare by comparing the passwords
userSchema.methods.isPasswordCorrect = async function (password) {
    if (!password || !this.password) {
        throw new Error("Password and hashed password is missing")
    }
    return await bcrypt.compare(password, this.password)
}

//here we generate the tokens
userSchema.methods.generateAccessToken = async function () {
    return jwt.sign({
        _id: this._id,
        email: this.email,
        name: this.name
    }, {
        srecty_key
    },
    expreidIn)
}

export const User = mongoose.model("User", userSchema)