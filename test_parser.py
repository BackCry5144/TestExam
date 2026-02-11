
import json
from parse_new_exams import parse_questions_file, parse_answers_file

# Test Question Parsing
print("--- Testing Question Parsing ---")
q_map = parse_questions_file(r'c:\Users\user\Documents\Hanwha_Baek\02.Training\OutSystems\OutSystems_Sample_Exam_Program\SampleExam\SampleExam_Set1.md')
print(f"Parsed {len(q_map)} questions.")
if len(q_map) > 0:
    first_id = list(q_map.keys())[0]
    print(f"Sample Question {first_id}: {q_map[first_id]}")

# Test Answer Parsing
print("\n--- Testing Answer Parsing ---")
a_map = parse_answers_file(r'c:\Users\user\Documents\Hanwha_Baek\02.Training\OutSystems\OutSystems_Sample_Exam_Program\SampleExam_Answer\SampleExam_Set1_Answer.md')
print(f"Parsed {len(a_map)} answers.")
if len(a_map) > 0:
    first_id = list(a_map.keys())[0]
    print(f"Sample Answer {first_id}: {a_map[first_id]}")
