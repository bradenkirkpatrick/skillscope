import express from 'express';
import fileUpload from 'express-fileupload';
import path from 'path';
import fs from 'fs';
import cors from 'cors';
import { exec } from 'child_process';

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

app.post('/ats-review', (req, res) => {
  const resumePath = path.join(__dirname, 'uploads', 'resume.pdf');
  
  // Check if resume exists
  if (!fs.existsSync(resumePath)) {
    return res.status(400).json({ error: 'Resume not found. Please upload a resume first.' });
  }

  // Run the Python script
  exec(`python3 rank_jobs.py`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing script: ${error.message}`);
      return res.status(500).json({ error: 'Error processing resume.' });
    }
    if (stderr) {
      console.error(`Script stderr: ${stderr}`);
      return res.status(500).json({ error: 'Error processing resume.' });
    }

    try {
      const result = JSON.parse(stdout);
      res.json(result);
    } catch (parseError) {
      console.error(`Error parsing script output: ${parseError.message}`);
      res.status(500).json({ error: 'Invalid response from processing script.' });
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});