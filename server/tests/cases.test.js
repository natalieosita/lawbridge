const request = require('supertest');
const app = require('../app');
const mongoose = require('mongoose');
const User = require('../models/User');
const Case = require('../models/Case');
const jwt = require('jsonwebtoken');

let token;

beforeAll(async () => {
  await mongoose.connect(process.env.MONGO_URI_TEST);
  const user = await User.create({
    name: 'CaseTester',
    email: 'case@example.com',
    password: 'hashed' // ideally hash this or use register route
  });
  token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
});

afterAll(async () => {
  await User.deleteMany({});
  await Case.deleteMany({});
  await mongoose.disconnect();
});

describe('Case Integration Tests', () => {
  it('should create a new case', async () => {
    const res = await request(app)
      .post('/cases')
      .set('Authorization', `Bearer ${token}`)
      .send({ title: 'Land Dispute', description: 'Conflict over Nairobi title' });

    expect(res.statusCode).toBe(201);
    expect(res.body.title).toBe('Land Dispute');
  });

  it('should fetch user cases', async () => {
    const res = await request(app)
      .get('/cases')
      .set('Authorization', `Bearer ${token}`);

    expect(res.statusCode).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
  });
});