import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import dotenv from 'dotenv';
import morgan from 'morgan';
import connectDB from './utils/db.js';
import authRoutes from './routes/authRoutes.js';
import caseRoutes from './routes/caseRoutes.js';
import { errorHandler, notFound } from './middleware/errorMiddleware.js';

dotenv.config();
connectDB();

const app = express();
app.use(helmet());
app.use(cors());
app.use(express.json());
app.use(morgan('dev'));

app.get('/health', (_, res) => res.status(200).json({ status: 'ok', uptime: process.uptime() }));
app.use('/auth', authRoutes);
app.use('/cases', caseRoutes);
app.use(notFound);
app.use(errorHandler);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🚀 Backend running on port ${PORT}`));