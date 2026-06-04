
// Application logic reads from environment mapping defined in Dockerfile
console.log(`Running in environment: ${process.env.APP_ENV}`);
console.log(`Database connected to: ${process.env.DB_URL}`);
