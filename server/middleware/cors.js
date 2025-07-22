const cors = require('cors');

const allowedOrigins = [
  'https://lawbridge.vercel.app', // your deployed frontend
  'http://localhost:3000'          // local dev
];

app.use(cors({
  origin: (origin, callback) => {
    // Allow requests with no origin (mobile apps, curl, etc.)
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true
}));