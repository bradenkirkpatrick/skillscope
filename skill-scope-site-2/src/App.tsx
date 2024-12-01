import React from 'react';
import { StatCard } from './components/StatCard';
import { ResumeUpload } from './components/ResumeUpload';
import { mockStats } from './data/mockStats';
import { resumeStats } from './data/resumeStats';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Developer Statistics Dashboard
          </h1>
          <p className="text-xl text-gray-600">
            Track your skills and expertise
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8 mb-8">
          <StatCard title="Top Languages" stats={mockStats.languages} />
          <StatCard title="Top Libraries" stats={mockStats.libraries} />
          <StatCard title="Top Tools & Software" stats={mockStats.tools} />
          <StatCard title="Top Soft Skills" stats={mockStats.softSkills} />
        </div>

        <div className="mt-12">
          <ResumeUpload />
        </div>
        <div className="text-center mb-12">
          <p className="text-xl text-gray-600">
            <br />
            Upload your resume to see track your skills and expertise against employers' desires
          </p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8 mb-8">
          <StatCard title="Top Languages" stats={resumeStats.languages} />
          <StatCard title="Top Libraries" stats={resumeStats.libraries} />
          <StatCard title="Top Tools & Software" stats={resumeStats.tools} />
          <StatCard title="Top Soft Skills" stats={resumeStats.softSkills} />
        </div>


      </div>
    </div>
  );
}

export default App;