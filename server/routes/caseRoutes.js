import express from 'express';
import { getAllCases, createCase } from '../controllers/caseController.js';
import { verifyToken } from '../middleware/authMiddleware.js';

const router = express.Router();
router.get('/', verifyToken, getAllCases);
router.post('/', verifyToken, createCase);

export default router;