import pandas as pd
import numpy as np
import glob
import pandas as pd
from docx import Document


def read_word_document(filepath):
    doc = Document(filepath)
    data = []
    current_section = None
    current_question = None
    current_notes = None
    current_mapping = {}

    for para in doc.paragraphs:
        text = para.text.strip()
        if text.startswith('*') and text.endswith('*'):
            current_section = text.strip('*').strip()
        elif '?' in text:
            if current_mapping:
                data[-1]['answer_value_mapping'] = str(current_mapping)
            current_question = text
            current_mapping = {}
            current_notes = None
        elif text.startswith("Note:"):
            current_notes = text
        elif ":" in text:
            code, code_explanation = text.split(':', 1)
            data.append({
                "section": current_section,
                "question": current_question,
                "answer_code": code.strip(),
                "answer_explanation": code_explanation.strip(),
                "notes": current_notes,
                "answer_value_mapping": None
            })
            current_notes = None
        elif any(text.startswith(str(n) + " ") for n in range(1, 6)):
            parts = text.split(' ', 1)
            if len(parts) == 2:
                val_key = parts[0].strip()
                val_description = parts[1].strip()
                current_mapping[val_key] = val_description

    if current_mapping and data:
        data[-1]['answer_value_mapping'] = str(current_mapping)

    return pd.DataFrame(data)


def format_codebook(input_path, output_path):
    # TODO move to a config file
    input_path = 'data/Codebook_W4.docx'
    df = read_word_document(input_path)

    output_path = 'data/codebook-df.xlsx'
    df.to_excel(output_path)