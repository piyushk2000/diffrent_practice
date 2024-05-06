// routes.js
import express from 'express';
import {
    createStudent,
    getAllStudents,
    getStudentById,
    getStudentsBySubject,
    getTeachersBySection,
    getTeachersByStudent,
    createStudy,
    createTeaching,
    updateStudent
  } from '../controllers/controller.js';

import {
  getNumbers,
  getStudentsBySectionAndSubject 
} from '../controllers/other.js'
const router = express.Router();

router.post('/student', createStudent);
router.get('/students', getAllStudents);
router.get('/student/:id', getStudentById);
router.get('/students/subject/:subjectName', getStudentsBySubject);
router.get('/teachers/section/:sectionId', getTeachersBySection);
router.get('/teachers/student/:studentName', getTeachersByStudent);
router.post('/study', createStudy);
router.post('/teaching', createTeaching);
router.put('/student/:id', updateStudent);


router.get('/numbers', getNumbers);
router.post('/students/section-subject', getStudentsBySectionAndSubject);


export default router;
