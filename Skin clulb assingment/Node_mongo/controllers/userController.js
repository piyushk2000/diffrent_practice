import asyncHandler from 'express-async-handler';
import User from '../models/userModel.js';

// @access  Public
const registerUser = asyncHandler(async (req, res) => {
  const { name, email, role, isActive } = req.body;

  const userExists = await User.findOne({ email });

  if (userExists) {
    res.status(400);
    throw new Error('User already exists');
  }

  const user = await User.create({
    name,
    email,
    role,
    isActive,
  });

  if (user) {
    res.status(201).json({
      _id: user._id,
      name: user.name,
      email: user.email,
      role: user.role,
      isActive: user.isActive
    });
  } else {
    res.status(400);
    throw new Error('Invalid user data');
  }
});

const getUsers = asyncHandler(async (req, res) => {
  const users = await User.find({});
  if(users) {
      res.json(users);
  } else {
      res.status(500);
      throw new Error('No users found');
  }
});


export {
  registerUser,
  getUsers,
};
