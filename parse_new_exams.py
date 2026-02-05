
import json
import re
import os

def parse_original_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # More robust split for the original files
    sections = re.split(r'\n\*\*|\n### ', content)
    questions_list = []
    
    for section in sections:
        lines = section.strip().split('\n')
        if not lines:
            continue
            
        # Match "문제 01. ..." or "01. ..."
        title_match = re.match(r'^(문제\s*|)(\d+)\.\s*(.*)', lines[0])
        if not title_match:
            continue
            
        question_text = title_match.group(3).strip().rstrip('*').strip()
        
        options = []
        for line in lines[1:]:
            opt_match = re.match(r'^([A-D])\.\s*(.*)', line.strip())
            if opt_match:
                options.append({
                    "code": opt_match.group(1),
                    "text": opt_match.group(2).strip()
                })
        
        if question_text and options:
            questions_list.append({
                "question": question_text,
                "options": options
            })
    return questions_list

def parse_answers_only(ans_file):
    with open(ans_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by ### 문제 or ### [Number]
    sections = re.split(r'\n### ', content)
    parsed_questions = []
    
    for section in sections[1:]:
        lines = section.strip().split('\n')
        if not lines:
            continue
            
        # Extract title/question
        question_line = lines[0]
        # Remove numbers like 01., 문제 01.
        question_text = re.sub(r'^(문제\s*\d+\.\s*|\d+\.\s*)', '', question_line).strip()
        
        options = []
        answer_code = ""
        for line in lines[1:10]: # Check first few lines for options
            ans_match = re.match(r'- \[( |x)\] (\*\*)?([A-D])\. (.*?)(\*\*)?$', line.strip())
            if ans_match:
                is_correct = ans_match.group(1) == 'x'
                code = ans_match.group(3)
                text = ans_match.group(4).strip()
                options.append({"code": code, "text": text})
                if is_correct:
                    answer_code = code
        
        # Extract explanation
        explanation = ""
        expl_start = False
        expl_lines = []
        for line in lines:
            if '> **해설**' in line:
                expl_start = True
                continue
            if expl_start and line.strip().startswith('>'):
                expl_lines.append(line.strip().lstrip('>').strip())
        explanation = "\n".join(expl_lines)
        
        parsed_questions.append({
            "question": question_text,
            "options": options,
            "answer_code": answer_code,
            "explanation": explanation
        })
            
    return parsed_questions

def save_merged_questions(data, filename):
    # Add unique sequential IDs
    for idx, q in enumerate(data):
        q['id'] = str(idx + 1)
        
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Parse New Exam Answer file directly (it has almost everything)
new_exam_data = parse_answers_only('New_Practice_Exam_Answer.md')
save_merged_questions(new_exam_data, 'new_exam_data.json')

# Parse Scenario Exam Answer file directly
scenario_exam_data = parse_answers_only('New_Practice_Exam_Scenairo_Answer.md')
save_merged_questions(scenario_exam_data, 'scenario_exam_data.json')

print(f"Parsed {len(new_exam_data)} questions for New Exam")
print(f"Parsed {len(scenario_exam_data)} questions for Scenario Exam")
