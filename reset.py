

file_content = """import { StatsData } from '../types/stats';
export const resumeStats: StatsData = {
languages: [

],libraries: [

],tools: [

],softSkills: [

],};"""

file_path = "/home/kg1/kanye/test/skillscope/skill-scope-site-2/src/data/resumeStats.ts"

with open(file_path, 'w') as file:
    file.write(file_content)

