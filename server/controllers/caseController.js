const Case = require('../models/Case');

const getCases = async (req, res) => {
  try {
    const cases = await Case.find({ owner: req.user.id }).sort({ createdAt: -1 });
    res.status(200).json(cases);
  } catch {
    res.status(500).json({ message: 'Failed to fetch cases' });
  }
};

const createCase = async (req, res) => {
  const { title, description } = req.body;
  try {
    const newCase = await Case.create({
      title,
      description,
      owner: req.user.id
    });
    res.status(201).json(newCase);
  } catch {
    res.status(500).json({ message: 'Failed to create case' });
  }
};

module.exports = { getCases, createCase };