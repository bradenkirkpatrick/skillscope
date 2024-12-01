import express from 'express';
import fileUpload from 'express-fileupload';
import path from 'path';
import fs from 'fs';
import cors from 'cors';

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(fileUpload());

app.post('/upload', (req, res) => {
  if (!req.files || Object.keys(req.files).length === 0) {
    console.error('No files were uploaded.');
    return res.status(400).send('No files were uploaded.');
  }

  const resume = req.files.file;
  const uploadPath = path.join(path.resolve(), 'uploads', 'resume.pdf');

  resume.mv(uploadPath, (err) => {
    if (err) {
      console.error('Error moving file:', err);
      return res.status(500).send(err);
    }

    res.send('File uploaded!');
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});