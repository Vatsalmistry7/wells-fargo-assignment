import pandas as pd
from flask import Flask, jsonify, request

# Read the process/combined csv
df = pd.read_csv("Output/consolidated_output_bonus.csv")

app = Flask("Data Viewer")


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        # index page data
        data = "Hello Recruiter"
        return jsonify({'data': data})


@app.route('/material_id/<int:num>', methods=['GET'])
def disp(num):
    # filter the data based on material_id
    op = df[df.material_id == num].to_dict('records')
    return jsonify(op)


# driver function
if __name__ == '__main__':
    print("Current server helps to query data based on material_id")
    print("URL for the same is domain/material_id/num")
    app.run(debug=True)
