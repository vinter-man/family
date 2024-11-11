from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import pandas as pd
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'

REQUIRED_FIELDS = ['id', 'name', 'father-id', 'mother-id']

def validate_excel(dataframe):
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in dataframe.columns:
            errors.append(f"A required field is missing: {field}")
    
    for index, row in dataframe.iterrows():
        if pd.isnull(row['id']) or pd.isnull(row['name']):
            errors.append(f"String {index+1}: ID and name are required")
        if pd.isnull(row['father-id']) and pd.isnull(row['mother-id']):
            errors.append(f"String {index+1}: At least one parent must be specified")
    
    return errors

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        try:
            df = pd.read_excel(file_path)
            errors = validate_excel(df)
            if errors:
                return jsonify({"errors": errors}), 400
            
            # Converting DataFrame to JSON for Front-End
            data = df.to_dict(orient='records')
            return jsonify({"data": data}), 200

        except Exception as e:
            return jsonify({"errors": [str(e)]}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4141)
