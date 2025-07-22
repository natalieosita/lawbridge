const request = require('supertest');
const app = require('../app');
const mongoose = require('mongoose');
const User = require('../models/User');

beforeAll(async () => {
  await mongoose.connect(process.env.MONGO_URI_TEST);
});

afterAll(async () => {
  await User.deleteMany({});
  await mongoose.disconnect();
});

describe('Auth Integration Tests', () => {
  it('should register a new user', async () => {
    const res = await request(app).post('/auth/register').send({
      name: 'Test User',
      email: 'test@example.com',
      password: '123456'
    });
    expect(res.statusCode).toBe(200);
    expect(res.body.token).toBeDefined();
  });

  it('should login an existing user', async () => {
    const res = await request(app).post('/auth/login').send({
      email: 'test@example.com',
      password: '123456'
    });
    expect(res.statusCode).toBe(200);
    expect(res.body.token).toBeDefined();
  });
});