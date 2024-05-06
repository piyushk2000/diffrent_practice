// importData.js
import mongoose from 'mongoose';
import dotenv from 'dotenv';
import { Student, Section, Subject, Teacher } from './models/model.js';
import data from './demo.js';
import connectDB from './config/db.js';

dotenv.config();

connectDB();

const importData = async () => {
    try {
      await Student.deleteMany({});
      await Section.deleteMany({});
      await Subject.deleteMany({});
      await Teacher.deleteMany({});

      await Student.insertMany(data.students);
      await Section.insertMany(data.sections);
      await Subject.insertMany(data.subjects);
      await Teacher.insertMany(data.teachers);

      console.log('Data imported successfully');
      process.exit();
    } catch (error) {
      console.log(`Failed to import data: ${error}`);
      process.exit(1);
    }
};

importData();
