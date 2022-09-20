from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import datasc
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
        f.save(secure_filename(f.filename))
        # print(f.filename)
        df = datasc.data_ext(f.filename)
        df.to_excel(buffer, index=False)
        headers = {
            'Content-Disposition': 'attachment; filename=output.xlsx',
            'Content-type': 'application/vnd.ms-excel'
        }
        return Response(buffer.getvalue(), mimetype='application/vnd.ms-excel', headers=headers)


if __name__ == '__main__':
    app.run(debug=True)