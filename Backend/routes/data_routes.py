from flask import Blueprint, render_template, send_file

data_bp = Blueprint('data', __name__)

# Static path to the Excel file
EXCEL_FILE = "static/data/Truck_Fullness_Prediction.xlsx"

@data_bp.route('/')
def data():
    """Route for selecting a regression type."""
    return render_template('data.html')

@data_bp.route('/simple-linear')
def simple_linear():
    """Route for displaying Simple Linear Regression visualization."""
    return render_template('simple_linear.html')

@data_bp.route('/linear-weak')
def linear_weak():
    """Route for displaying Linear Regression (Weak) visualization."""
    return render_template('linear_weak.html')

@data_bp.route('/linear-strong')
def linear_strong():
    """Route for displaying Linear Regression (Strong) visualization."""
    return render_template('linear_strong.html')

@data_bp.route('/multiple-regression')
def multiple_regression():
    """Route for displaying Multiple Regression visualization."""
    return render_template('multiple_regression.html')

@data_bp.route('/download')
def download():
    """Allow users to download the Excel file."""
    return send_file(EXCEL_FILE, as_attachment=True)
