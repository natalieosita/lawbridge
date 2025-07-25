// server/server.js
import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import morgan from 'morgan';
import { config } from './config/config.js';
import { connectDB } from './config/db.js';
import { logger } from './config/logger.js';

// Optional: import routes
// import authRoutes from './routes/authRoutes.js';
// import caseRoutes from './routes/caseRoutes.js';

const app = express();

// === Middleware ===
app.use(helmet()); // Security headers
app.use(cors({ origin: config.clientOrigin, credentials: true }));
app.use(express.json()); // Parse JSON bodies
app.use(morgan('dev')); // HTTP request logging

// === Routes ===
// app.use('/api/auth', authRoutes);
// app.use('/api/cases', caseRoutes);

app.get('/', (req, res) => {
  res.send('🚀 LawBridge API is running');
});

// === Start Server ===
const startServer = async () => {
  try {
    await connectDB();
    app.listen(config.port, () => {
      logger.success(`Server running on port ${config.port} in ${config.nodeEnv} mode`);
    });
  } catch (error) {
    logger.error('Failed to start server: ' + error.message);
    process.exit(1);
  }
};

startServer();