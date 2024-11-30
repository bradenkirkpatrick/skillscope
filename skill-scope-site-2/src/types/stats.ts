export interface Stat {
  name: string;
  value: number | string;
  icon?: string;
}

export interface StatsData {
  languages: Stat[];
  libraries: Stat[];
  tools: Stat[];
  softSkills: Stat[];
}