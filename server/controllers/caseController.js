import Case from '../models/Case.js';

export const getAllCases = async (req, res) => {
  try {
    const cases = await Case.find({ user: req.user.id }).sort({ createdAt: -1 });
    res.json(cases);
  } catch (err) {
    res.status(500).json({ message: 'Fetch error', error: err.message });
  }
};

export const createCase = async (req, res) => {
  const { title, description } = req.body;
  try {
    const newCase = new Case({ title, description, user: req.user.id });
    await newCase.save();
    res.status(201).json(newCase);
  } catch (err) {
    res.status(500).json({ message: 'Create error', error: err.message });
  }
};