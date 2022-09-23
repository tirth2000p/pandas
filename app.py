from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import datasc
from openpyxl import load_workbook
from flask import Response
import io
buffer = io.BytesIO()

app = Flask(__name__)



@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        print(f.filename)
        df = datasc.data_ext(f.filename)
        df.to_excel(buffer,index=False)
        df.to_excel(r'out.xlsx', index=False)

        book = load_workbook("out.xlsx")
        sheet = book.active

        # headers = {
        #     'Content-Disposition': 'attachment; filename=output.xlsx',
        #     'Content-type': 'application/vnd.ms-excel'
        # }
        #
        # return Response(buffer.getvalue(), mimetype='application/vnd.ms-excel', headers=headers)
        return render_template('s3_excel_table.html', sheet=sheet)

if __name__ == '__main__':
    app.run(debug=True)