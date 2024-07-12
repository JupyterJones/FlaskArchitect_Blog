import os
import json
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_code_cells_from_notebook(notebook_path):
    """
    Extract code cells from a Jupyter notebook.
    :param notebook_path: Path to the Jupyter notebook file.
    :return: List of code cells.
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as file:
            notebook_content = json.load(file)
        
        code_cells = []
        for cell in notebook_content['cells']:
            if cell['cell_type'] == 'code':
                code_cells.append(''.join(cell['source']))
        
        return code_cells
    except json.JSONDecodeError as e:
        logging.error(f'Error decoding JSON from notebook {notebook_path}: {e}')
        return []
    except Exception as e:
        logging.error(f'Unexpected error processing notebook {notebook_path}: {e}')
        return []

def save_code_cells(code_cells, output_path):
    """
    Save code cells to a file.
    :param code_cells: List of code cells.
    :param output_path: Path to the output file.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            for cell in code_cells:
                file.write(cell)
                file.write('\n\n')
    except Exception as e:
        logging.error(f'Error saving code cells to {output_path}: {e}')

def process_notebooks_in_directory(directory_path, output_directory):
    """
    Process all Jupyter notebooks in a directory to extract and save code cells.
    :param directory_path: Path to the directory containing Jupyter notebooks.
    :param output_directory: Path to the directory to save extracted code cells.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(directory_path):
        if filename.endswith('.ipynb'):
            notebook_path = os.path.join(directory_path, filename)
            logging.info(f'Processing notebook: {notebook_path}')
            
            code_cells = extract_code_cells_from_notebook(notebook_path)
            if code_cells:
                output_path = os.path.join(output_directory, f'{os.path.splitext(filename)[0]}_code_cells.py')
                save_code_cells(code_cells, output_path)
                logging.info(f'Saved code cells to: {output_path}')
            else:
                logging.info(f'No code cells found in notebook: {notebook_path}')

# Directory containing Jupyter notebooks
notebooks_directory = '/home/jack/Desktop/notebooks'

# Directory to save extracted code cells
output_directory = 'code_cells'

# Process the notebooks
process_notebooks_in_directory(notebooks_directory, output_directory)
