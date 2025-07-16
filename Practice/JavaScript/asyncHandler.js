// In Express.js, route handlers that use async / await must handle errors properly.
// If an error occurs inside an async function,
// it is rejected as a promise and needs to be caught using a try-catch block

export const asyncHandler = (requestHandler) => {
    return (req, res, next) => {
        Promise.resolve(requestHandler(req, res, next)).catch((err) => next(err))
    }
}