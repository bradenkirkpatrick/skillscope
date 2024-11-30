import { StatsData } from '../types/stats';

export const mockStats: StatsData = {
  languages: [
    { name: 'JavaScript', value: '95%' },
    { name: 'TypeScript', value: '90%' },
    { name: 'Python', value: '85%' },
    { name: 'Java', value: '80%' },
    { name: 'C++', value: '75%' },
  ],
  libraries: [
    { name: 'React', value: '95%' },
    { name: 'Node.js', value: '90%' },
    { name: 'Express', value: '85%' },
    { name: 'TensorFlow', value: '80%' },
    { name: 'Django', value: '75%' },
  ],
  tools: [
    { name: 'VS Code', value: '95%' },
    { name: 'Git', value: '90%' },
    { name: 'Docker', value: '85%' },
    { name: 'Kubernetes', value: '80%' },
    { name: 'Jenkins', value: '75%' },
  ],
  softSkills: [
    { name: 'Communication', value: '95%' },
    { name: 'Team Leadership', value: '90%' },
    { name: 'Problem Solving', value: '90%' },
    { name: 'Time Management', value: '85%' },
    { name: 'Adaptability', value: '85%' },
  ],
};