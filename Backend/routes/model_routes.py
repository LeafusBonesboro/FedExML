from flask import Blueprint, render_template, request
from sklearn.linear_model import LinearRegression
import numpy as np
import plotly.express as px
import pandas as pd
import random

model_bp = Blueprint('model', __name__)

@model_bp.route('/')
def model():
    """Route to select simulation type."""
    return render_template('sims/model.html')

@model_bp.route('/linear', methods=['GET', 'POST'])
def linear():
    """Route for Linear Regression simulation."""
    cartons = []
    full_percentage = []

    if request.method == 'POST':
        # Extract values from the table
        for i in range(1, 11):  # Loop through 10 rows
            cartons.append(float(request.form.get(f'cartons_{i}', 0)))
            full_percentage.append(float(request.form.get(f'full_{i}', 0)))

        # Check if inputs are valid
        if len(cartons) != 10 or len(full_percentage) != 10:
            return render_template('sims/linear.html', error="Please fill all rows.", cartons=cartons, full_percentage=full_percentage)

        # Run Linear Regression
        X = np.array(cartons).reshape(-1, 1)
        y = np.array(full_percentage)
        model = LinearRegression()
        model.fit(X, y)

        # Regression results
        slope = model.coef_[0]
        intercept = model.intercept_
        r_squared = model.score(X, y)

        # Generate plot
        df = pd.DataFrame({'Cartons': cartons, 'Full Percentage': full_percentage})
        df['Predicted'] = model.predict(X)
        fig = px.scatter(df, x='Cartons', y='Full Percentage', title='Linear Regression')
        fig.add_scatter(x=df['Cartons'], y=df['Predicted'], mode='lines', name='Regression Line')
        plot_html = fig.to_html(full_html=False)

        return render_template('sims/linear.html', slope=slope, intercept=intercept, r_squared=r_squared, plot=plot_html, cartons=cartons, full_percentage=full_percentage)

    return render_template('sims/linear.html', cartons=cartons, full_percentage=full_percentage)

import random
@model_bp.route('/multi', methods=['GET', 'POST'])
def multi():
    """Route for Multiple Regression simulation."""
    cartons = []
    weight = []
    full_percentage = []

    # Store user inputs to prefill fields later
    user_data = {
        'cartons': [None] * 10,
        'weight': [None] * 10,
        'full_percentage': [None] * 10
    }

    if request.method == 'POST':
        for i in range(1, 11):
            # Extract values and add them to the lists
            cartons_val = request.form.get(f'cartons_{i}')
            weight_val = request.form.get(f'weight_{i}')
            full_val = request.form.get(f'full_{i}')

            cartons.append(float(cartons_val or 0))
            weight.append(float(weight_val or 0))
            full_percentage.append(float(full_val or 0))

            # Store user inputs for the template
            user_data['cartons'][i - 1] = cartons_val
            user_data['weight'][i - 1] = weight_val
            user_data['full_percentage'][i - 1] = full_val

        # Combine all predictors into a DataFrame
        df = pd.DataFrame({
            'Cartons': cartons,
            'Weight': weight,
            '% Full': full_percentage
        })

        # Run Multiple Regression
        X = df[['Cartons', 'Weight']]
        y = df['% Full']
        model = LinearRegression()
        model.fit(X, y)

        # Regression results
        coefficients = dict(zip(X.columns, model.coef_))
        intercept = model.intercept_
        r_squared = model.score(X, y)

        # Generate plot
        fig = px.scatter_3d(df, x='Cartons', y='Weight', z='% Full', title='Multiple Regression')
        fig.add_scatter3d(
            x=df['Cartons'],
            y=df['Weight'],
            z=model.predict(X),
            mode='lines',
            name='Regression Plane'
        )
        plot_html = fig.to_html(full_html=False)

        return render_template(
            'sims/multi.html',
            user_data=user_data,
            coefficients=coefficients,
            intercept=intercept,
            r_squared=r_squared,
            plot=plot_html
        )

    return render_template('sims/multi.html', user_data=user_data)
