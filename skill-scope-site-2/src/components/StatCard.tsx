import React from 'react';
import { Stat } from '../types/stats';

interface StatCardProps {
  title: string;
  stats: Stat[];
}

export const StatCard: React.FC<StatCardProps> = ({ title, stats }) => {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">{title}</h2>
      <div className="space-y-4">
        {stats.map((stat, index) => (
          <div key={index} className="relative">
            <div className="flex justify-between mb-1">
              <span className="text-sm font-medium text-gray-700">{stat.name}</span>
              <span className="text-sm font-medium text-gray-500">{stat.value}</span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className="bg-blue-600 h-2 rounded-full transition-all duration-500"
                style={{ width: typeof stat.value === 'string' ? stat.value : `${stat.value}%` }}
              ></div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};