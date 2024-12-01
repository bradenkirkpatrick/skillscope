import React, { useCallback, useState } from 'react';
import { Upload } from 'lucide-react';
import axios from 'axios';

export const ResumeUpload: React.FC = () => {
  const [isUploaded, setIsUploaded] = useState(false);
  const [reviewResult, setReviewResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = useCallback(async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file && file.type === 'application/pdf') {
      try {
        const formData = new FormData();
        formData.append('file', file, 'resume.pdf');
        
        await axios.post('http://localhost:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        console.log('File uploaded successfully');
        setIsUploaded(true);
      } catch (error) {
        console.error('Error uploading file:', error);
      }
    } else {
      alert('Please select a PDF file');
    }
  }, []);

  const handleReview = async () => {
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/ats-review');
      setReviewResult(response.data);
    } catch (error) {
      console.error('Error during ATS review:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">Upload Resume</h2>
      <div className="flex items-center justify-center w-full">
        <label className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100">
          <div className="flex flex-col items-center justify-center pt-5 pb-6">
            <Upload className="w-10 h-10 mb-3 text-gray-400" />
            <p className="mb-2 text-sm text-gray-500">
              <span className="font-semibold">Click to upload</span> or drag and drop
            </p>
            <p className="text-xs text-gray-500">PDF files only</p>
          </div>
          <input
            type="file"
            className="hidden"
            accept=".pdf"
            onChange={handleFileChange}
          />
        </label>
      </div>
      {isUploaded && (
        <div className="mt-4">
          <p className="text-green-500">Resume uploaded successfully!</p>
          <button
            onClick={handleReview}
            className="mt-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            {loading ? 'Reviewing...' : 'ATS Review'}
          </button>
          {reviewResult && (
            <div className="mt-4">
              {/* Display review results here */}
              <pre>{JSON.stringify(reviewResult, null, 2)}</pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
};